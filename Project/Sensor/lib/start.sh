#!/bin/bash
python3 main.py &
python3 sensors/Button.py &
python3 sensors/VoiceListener.py
wait