# CrashAnalysis
# SUMO Intersection Collision Scenario

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
    Repear for rear_end_collision scenario

   You can find the XML code for these files in the `scenarios/intersection_collision/` directory of this repository.

## Running the Code

To run the code and simulate the intersection collision scenario, follow these steps:

1. Clone this repository to your local machine:
   ```
   git clone https://github.com/your-username/sumo-intersection-collision-scenario.git
   ```

2. Navigate to the repository directory:
   ```
   cd sumo-intersection-collision-scenario
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

## Acknowledgments

- The SUMO development team for providing a powerful traffic simulation software.
- The contributors to the TraCI Python library for enabling interaction with SUMO simulations.

