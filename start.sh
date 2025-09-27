#!/bin/bash


# Start the Python server in the background
python /app/server.py &


# Wait a short while to ensure the server is ready to accept connections
sleep 2


# Run main.py (the process monitor)
python /app/main.py
