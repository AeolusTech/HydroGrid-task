import json
import unittest

HALF_HOUR_IN_MILLISECONDS = 1800000


def main():
    with open('./TimeseriesEqualizer_Input.json', 'r') as f:
        data = json.load(f)


    # first_timestamp = int(data['timeseries'][0]['timestamp'])
    timeseries_data = data['timeseries']

    for element_index in range(len(data['timeseries'][1:-2])):
        time_diff = int(timeseries_data[element_index]['timestamp']) - int(timeseries_data[element_index - 1]['timestamp'])
        time_diff_in_half_hours = time_diff / HALF_HOUR_IN_MILLISECONDS
        print(f'{time_diff_in_half_hours} hour')


class TestMyModule(unittest.TestCase):
    def test_dummy(self):
        assert 3 == 3


if __name__ == '__main__':
    main()