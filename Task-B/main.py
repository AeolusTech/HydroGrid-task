import json
import unittest

HALF_HOUR_IN_MILLISECONDS = 1800000


def process_json(input_json):
    # first_timestamp = int(data['timeseries'][0]['timestamp'])
    timeseries_data = input_json['timeseries']

    amount_of_timestamps_without_last_and_first = len(input_json['timeseries'][1:-2])

    for element_index in range(amount_of_timestamps_without_last_and_first):
        current_time = int(timeseries_data[element_index]['timestamp'])
        previous_time = int(timeseries_data[element_index - 1]['timestamp'])
        time_diff = current_time - previous_time
        time_diff_in_half_hours = time_diff / HALF_HOUR_IN_MILLISECONDS
        print(f'{time_diff_in_half_hours} hour')

    return json.loads('{"turbine": null}')


def main():
    with open('./TimeseriesEqualizer_Input.json', 'r') as f:
        data = json.load(f)

    process_json(data)

class TestMyModule(unittest.TestCase):
    def compare(self, a, b):
        assert self.ordered(a) == self.ordered(b)

    def ordered(self, obj):
        if isinstance(obj, dict):
            return sorted((k, self.ordered(v)) for k, v in obj.items())
        if isinstance(obj, list):
            return sorted(self.ordered(x) for x in obj)
        else:
            return obj

    def test_dummy_should_pass(self):
        input_json = json.loads("""
        {
            "timeseries": [
                {
                    "timestamp": 1581609600000,
                    "value": 20.0
                }
            ],
            "turbine": "B",
            "power_unit": "MW"
        }
        """)
        expected_output_same_as_input_different_order = json.loads("""
        {
            "turbine": "B",
            "power_unit": "MW",
            "timeseries": [
                {
                    "timestamp": 1581609600000,
                    "value": 20.0
                }
            ]
        }
        """
        )
        self.compare(input_json, expected_output_same_as_input_different_order)

    def test_A(self):
        input_json = json.loads("""
        {
            "turbine": "A",
            "power_unit": "MW",
            "timeseries": [
                {
                    "timestamp": 1581609600000,
                    "value": 16
                },
                {
                    "timestamp": 1581610500000,
                    "value": null
                }
            ]
        }
        """
        )
        expected_output = json.loads("""
        {
            "turbine": "A",
            "power_unit": "MW",
            "timeseries": [
                {
                    "timestamp": 1581609600000,
                    "value": 16.0
                }
            ]
        }
        """
        )
        self.compare(process_json(input_json), expected_output)

    def test_B(self):
        input_json = json.loads("""
        {
            "turbine": "B",
            "power_unit": "MW",
            "timeseries": [
                {
                    "timestamp": 1581609600000,
                    "value": 16
                },
                {
                    "timestamp": 1581610500000,
                    "value": 0
                },
                {
                    "timestamp": 1581611400000,
                    "value": 4
                },
                {
                    "timestamp": 1581612300000,
                    "value": 60
                },
                {
                    "timestamp": 1581613200000,
                    "value": null
                }
            ]
        }
        """)
        expected_output = json.loads("""
        {
            "turbine": "B",
            "power_unit": "MW",
            "timeseries": [
                {
                    "timestamp": 1581609600000,
                    "value": 20.0
                }
            ]
        }
        """
        )
        self.compare(process_json(input_json), expected_output)


if __name__ == '__main__':
    main()