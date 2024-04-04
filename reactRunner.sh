#!/bin/bash

# Define paths for React apps
auth_app="/home/yassine/Desktop/alx/VitaSync/frontend/auth/"
doc_app="/home/yassine/Desktop/alx/VitaSync/frontend/doc/"
nurse_app="/home/yassine/Desktop/alx/VitaSync/frontend/nurse/"
patient_app="/home/yassine/Desktop/alx/VitaSync/frontend/patient/"
pharmacy_app="/home/yassine/Desktop/alx/VitaSync/frontend/pharmacist"

# Path for pagekite.py
pagekite_py="/home/yassine/Desktop/pagekite.py"

# Array to hold background process IDs
pids=()

# Function to start React apps
start_apps() {
  echo "Starting React apps..."
  cd "$auth_app" && npm start &
  pids+=($!)
  cd "$doc_app" && npm start &
  pids+=($!)
  cd "$nurse_app" && npm start &
  pids+=($!)
  cd "$patient_app" && npm start &
  pids+=($!)
  cd "$pharmacy_app" && npm start &
  pids+=($!)
}

# Function to start pagekite.py
start_pagekite() {
  echo "Starting pagekite.py..."
  python3 "$pagekite_py"
}

# Function to stop all background processes
stop_processes() {
  echo "Stopping all processes..."
  for pid in "${pids[@]}"; do
    kill "$pid"
  done
  exit 0
}

# Trap SIGINT signal (Ctrl+C) and call stop_processes function
trap stop_processes SIGINT

# Main function
main() {
  start_apps
  start_pagekite
  # Wait for SIGINT signal (Ctrl+C)
  wait
}

main
