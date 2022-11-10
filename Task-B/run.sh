#!/bin/bash

docker run --rm --name test-run test-image "main.py" "./TimeseriesEqualizer_Input.json"