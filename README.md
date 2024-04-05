CrashAnalysis

This repository is dedicated to simulating and analyzing vehicular crash scenarios using SUMO (Simulation of Urban MObility), with a particular focus on rear-end collisions and lane-changing incidents. It showcases the integration of crash detection algorithms, vehicle tracking techniques, and the simulation of variable traffic conditions.

Prerequisites

Ensure you have the following installed to use this repository effectively:

	•	Python 3.x
	•	SUMO, with the SUMO_HOME environment variable correctly set
	•	TraCI Python library (pip install traci)

Repository Structure

CrashAnalysis/
├── scenarios/
│   ├── rear_end_collision/
│   │   ├── rear_end_collision.net.xml
│   │   ├── rear_end_collision.rou.xml
│   │   └── rear_end_collision.sumocfg
│   └── lane_change_collision/
│       ├── lane_change_collision.net.xml
│       ├── lane_change_collision.rou.xml
│       └── lane_change_collision.sumocfg
├── crash_detection.py
├── run_simulation.py
├── kalman_filter.py
└── constant_speed_model.py

	•	scenarios/: Contains SUMO configurations and network files for the crash scenarios.
	•	crash_detection.py: Main script for running crash detection simulations.
	•	run_simulation.py: Utility script for running SUMO simulations with custom behavior.
	•	kalman_filter.py & constant_speed_model.py: Implement vehicle tracking algorithms.

Quick Start

	1.	Clone this repository:

git clone https://github.com/<your-username>/CrashAnalysis.git


	2.	Navigate to the repository folder:

cd CrashAnalysis


	3.	To run crash detection simulations, execute:

python crash_detection.py


	4.	To run standard SUMO simulations with custom vehicle behavior:

python run_simulation.py <scenario_name>



Replace <scenario_name> with either rear_end_collision or lane_change_collision.

Customization and Extension

Feel free to modify the scripts to incorporate your crash detection algorithms, adjust vehicle tracking models, or simulate different traffic conditions. Key points of interest might include:

	•	Enhancing kalman_filter.py and constant_speed_model.py for more accurate vehicle tracking.
	•	Extending crash_detection.py to include additional crash scenarios or detection mechanisms.
	•	Adapting run_simulation.py to simulate more complex vehicle behaviors or interactions.

Installing SUMO on macOS

	•	Install Homebrew: /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
	•	Install XQuartz (for SUMO’s GUI): brew install --cask xquartz and restart your machine.
	•	Tap SUMO Repository: brew tap dlr-ts/sumo.
	•	Install SUMO: brew install sumo.
	•	Set SUMO_HOME: Find SUMO’s path with brew info sumo, then add export SUMO_HOME=/path/to/sumo to your shell configuration file.
	•	Test GUI: Launch XQuartz, and in its terminal, run sumo-gui.

For a detailed guide, refer to the Homebrew SUMO repository.

Acknowledgments

	•	SUMO developers for their comprehensive traffic simulation suite.
	•	Contributors to the TraCI library for enabling seamless interaction with SUMO.