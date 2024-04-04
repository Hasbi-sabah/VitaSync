#!/bin/bash

# Define paths for React apps
auth_app="../frontend/auth/"
doc_app="../frontend/doc/"
nurse_app="../frontend/nurse/"
patient_app="../frontend/patient/"
pharmacy_app="../frontend/pharmacist"

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
  # Wait for SIGINT signal (Ctrl+C)
  wait
}

main
