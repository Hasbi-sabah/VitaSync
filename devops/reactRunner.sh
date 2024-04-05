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
  cd "$auth_app" && npm start | grep -v "Compiled successfully" &
  pids+=($!)
  echo "Auth app started on port 3000"
  pids+=($!)
  echo "Doc app started on port 3001"
  pids+=($!)
  echo "Nurse app started on port 3002"
  pids+=($!)
  echo "Patient app started on port 3003"
  pids+=($!)
  echo "Pharmacy app started on port 3004"

# Function to stop all background processes
stop_processes() {
  echo "Stopping all processes..."
  for pid in "${pids[@]}"; do
    kill "$pid"
  done
  exit 0
}

trap stop_processes SIGINT SIGQUIT

# Main function
main() {
  start_apps
  # Wait for SIGINT or SIGQUIT signal (Ctrl+C or Ctrl+D)
  wait
}

main
