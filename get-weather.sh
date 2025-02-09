#!/bin/bash
echo "Script ejecutado el: $(date)" >> /home/iccd332/TorontoWeather/output.log
/home/iccd332/miniforge3/envs/iccd332/bin/python3 /home/iccd332/TorontoWeather/main.py >> /home/iccd332/TorontoWeather/output.log 2>&1
