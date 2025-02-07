#!/bin/bash
echo "Script ejecutado el: $(date)" >> /mnt/d/ubuntu/python/Clima-Toronto-App/output.log
/home/iccd332/miniforge3/envs/iccd332/bin/python3 /mnt/d/ubuntu/python/Clima-Toronto-App/clima-toronto-hoy.py >> /mnt/d/ubuntu/python/Clima-Toronto-App/output.log 2>&1