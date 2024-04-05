import os
import sys

# Set up the environment to find the SUMO tools
if 'SUMO_HOME' in os.environ:
    tools = os.path.join(os.environ['SUMO_HOME'], 'tools')
    sys.path.append(tools)
else:
    sys.exit("Please set the 'SUMO_HOME' environment variable to the root directory of your SUMO installation.")

from sumolib import checkBinary  # Checks for the binary in SUMO_HOME/bin
import traci  # Interface to interact with SUMO

def run():
    while traci.simulation.getMinExpectedNumber() > 0:
        traci.simulationStep()  # Advance the simulation by one step
        vehicle_ids = traci.vehicle.getIDList()  # Get a list of all vehicle IDs in the simulation
        for v_id in vehicle_ids:
            position = traci.vehicle.getPosition(v_id)  # Get the current position of the vehicle
            speed = traci.vehicle.getSpeed(v_id)  # Get the current speed of the vehicle
            print(f"Vehicle {v_id}: Position = {position}, Speed = {speed} m/s")
    traci.close()

if __name__ == "__main__":
    sumoBinary = checkBinary('sumo')  # Use 'sumo-gui' if you want to see the simulation in SUMO's GUI
    scenario_config = "scenarios/rear_end_collision/rear_end_collision.sumocfg"  # Path to your scenario's SUMO configuration file

    # Start the TraCI connection with SUMO
    traci.start([sumoBinary, "-c", scenario_config])

    run()  # Run the simulation and extract vehicle data
