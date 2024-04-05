import os
import sys

# Ensure that SUMO_HOME environment variable is set
if 'SUMO_HOME' in os.environ:
    tools = os.path.join(os.environ['SUMO_HOME'], 'tools')
    sys.path.append(tools)
else:
    sys.exit("Please declare the environment variable 'SUMO_HOME'")

from sumolib import checkBinary  # Corrected import for checkBinary
import traci

def run_simulation():
    while traci.simulation.getMinExpectedNumber() > 0:
        traci.simulationStep()
        vehicle_ids = traci.vehicle.getIDList()
        
        for vehicle_id in vehicle_ids:
            position = traci.vehicle.getPosition(vehicle_id)
            speed = traci.vehicle.getSpeed(vehicle_id)
            print(f"Vehicle {vehicle_id}: Position = {position}, Speed = {speed} m/s")

    traci.close()

if __name__ == "__main__":
    sumoBinary = checkBinary('sumo')  # Use 'sumo-gui' if you want to visualize the simulation
    config_file = "scenarios/lane_change_collision/lane_change_collision.sumocfg"

    traci.start([sumoBinary, "-c", config_file])
    run_simulation()
