# CrashAnalysis

This repository contains code for simulating crash analysis scenarios using the SUMO (Simulation of Urban MObility) traffic simulation software. The code demonstrates the integration of crash detection algorithms, vehicle tracking methods, and communication loss simulation.

## Prerequisites

To run the code in this repository, you need to have the following:

- Python 3.x installed
- SUMO installed and the `SUMO_HOME` environment variable set
- TraCI Python library installed (`pip install traci`)

## Repository Structure

The repository is organized as follows:

```
sumo-intersection-collision-scenario/
├── scenarios/
│   ├── rear_end_collision/
│   │   ├── rear_end_collision.net.xml
│   │   ├── rear_end_collision.rou.xml
│   │   ├── rear_end_collision.add.xml
│   │   └── rear_end_collision.sumocfg
│   └── intersection_collision/
│       ├── intersection_collision.net.xml
│       ├── intersection_collision.rou.xml
│       ├── intersection_collision.add.xml
│       └── intersection_collision.sumocfg
├── crash_detection.py
├── kalman_filter.py
├── constant_speed_model.py
└── README.md
```

- The `scenarios/` directory contains the SUMO configuration files and network files for different collision scenarios.
- `crash_detection.py` is the main script that integrates the crash detection algorithms and vehicle tracking methods with SUMO simulations.
- `kalman_filter.py` and `constant_speed_model.py` contain the implementations of the Kalman filter and constant speed model for vehicle tracking.
- `README.md` provides an overview of the project and instructions on how to use the code.

## Setting Up SUMO

To set up SUMO for the intersection collision scenario, follow these steps:

1. Install SUMO by downloading it from the official website: [https://sumo.dlr.de/docs/Downloads.html](https://sumo.dlr.de/docs/Downloads.html)

2. Set the `SUMO_HOME` environment variable to the directory where SUMO is installed.

3. Create the necessary files for the intersection collision scenario:
   - `intersection_collision.net.xml`: Defines the road network.
   - `intersection_collision.rou.xml`: Defines the vehicle routes and types.
   - `intersection_collision.add.xml`: Defines additional simulation elements, such as traffic lights.
   - `intersection_collision.sumocfg`: Configures the simulation settings.

   You can find the XML code for these files in the `scenarios/intersection_collision/` directory of this repository.

   Repeat for rear_end_collision scenario

## Running the Code

To run the code and simulate the intersection collision scenario, follow these steps:

1. Clone this repository to your local machine:
   ```
   git clone https://github.com/your-username/CrashAnalysis.git
   ```

2. Navigate to the repository directory:
   ```
   cd CrashAnalysis
   ```

3. Run the `crash_detection.py` script:
   ```
   python crash_detection.py
   ```

   This script will start the SUMO simulation, integrate the crash detection algorithms and vehicle tracking methods, and output the results.

4. Observe the simulation results, including the detected crashes, tracking accuracy metrics, and any other relevant information.

## Modifying the Code

You can modify the code to customize the simulation or incorporate your own crash detection algorithms and vehicle tracking methods. Here are a few key files and functions to consider:

- `crash_detection.py`:
  - `detect_crashes_with_kalman_filter()`: Integrates the Kalman filter for vehicle tracking and crash detection.
  - `detect_crashes_with_constant_speed()`: Integrates the constant speed model for vehicle tracking and crash detection.
  - `compare_tracking_methods()`: Compares the performance of the Kalman filter and constant speed model.

- `kalman_filter.py`:
  - `kalman_filter()`: Implements the Kalman filter algorithm for vehicle tracking.

- `constant_speed_model.py`:
  - `constant_speed_model()`: Implements the constant speed model for vehicle tracking.

Feel free to explore and modify these files to suit your specific requirements.



## Running the Simulation

The `run_simulation.py` script demonstrates how to run a SUMO simulation with vehicle tracking, crash detection, and communication loss simulation. It retrieves trajectory information from SUMO, modifies the data based on custom requirements, and performs crash detection using the modified data.

### Prerequisites

Make sure you have the following dependencies installed:

- TraCI Python library: `pip install traci`

### Usage

To run the simulation, follow these steps:

1. Update the `path/to/sumo/config.sumocfg` in the script with the path to your SUMO configuration file (`.sumocfg`).

2. Run the script:
   ```
   python run_simulation.py
   ```

   The script will start the SUMO simulation, retrieve trajectory information for each vehicle, simulate communication losses, modify the trajectory data, update the vehicle state, and perform crash detection.

### Functionality

The `run_simulation.py` script includes the following functions:

- `run_simulation()`: Runs the SUMO simulation and performs the main simulation loop. It retrieves vehicle IDs, gets trajectory information, simulates communication losses, modifies trajectory data, updates vehicle states, and performs crash detection for each vehicle.

- `modify_position(position)`: Modifies the position data based on custom requirements. You can implement your own logic here to modify the position data as needed.

- `modify_speed(speed)`: Modifies the speed data based on custom requirements. You can implement your own logic here to modify the speed data as needed.

- `detect_crash(vehicle_id, position, speed)`: Performs crash detection using the modified trajectory data. You can implement your crash detection algorithm here, log detected crashes, or store the results as required.

### Customization

You can customize the `run_simulation.py` script according to your specific requirements:

- Implement your own logic in the `modify_position()` and `modify_speed()` functions to modify the trajectory data based on your specific needs.
- Develop your crash detection algorithm in the `detect_crash()` function, utilizing the modified trajectory data.
- Extend the script to include additional functionality or output relevant data for analysis.

### Simulation Parameters

- Communication Loss Probability: The script simulates communication losses with a 10% probability. You can adjust this value by modifying the condition `if random.random() < 0.1` in the `run_simulation()` function.

## Acknowledgments

- The SUMO development team for providing a powerful traffic simulation software.
- The contributors to the TraCI Python library for enabling interaction with SUMO simulations.

