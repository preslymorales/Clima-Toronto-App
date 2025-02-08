#!/bin/bash
echo "Script ejecutado el: $(date)" >> /home/iccd332/CityWeather/output.log
/home/iccd332/miniforge3/envs/iccd332/bin/python3 /home/iccd332/CityWeather/clima-toronto-hoy.py >> /home/iccd332/CityWeather/output.log 2>&1
