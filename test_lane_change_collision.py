import os
import sys

# Ensure that SUMO_HOME environment variable is set
if 'SUMO_HOME' in os.environ:
    tools = os.path.join(os.environ['SUMO_HOME'], 'tools')
    sys.path.append(tools)
else:
    sys.exit("Please declare the environment variable 'SUMO_HOME'")

import traci  # Import TraCI module to interact with SUMO

def run_simulation():
    while traci.simulation.getMinExpectedNumber() > 0:
        traci.simulationStep()  # Proceed to the next time step in the simulation
        vehicle_ids = traci.vehicle.getIDList()  # Retrieve a list of all vehicle IDs currently in the simulation
        
        # Iterate through each vehicle and print its ID, position, and speed
        for vehicle_id in vehicle_ids:
            position = traci.vehicle.getPosition(vehicle_id)
            speed = traci.vehicle.getSpeed(vehicle_id)
            print(f"Vehicle {vehicle_id}: Position = {position}, Speed = {speed} m/s")

    traci.close()  # Close the TraCI connection

if __name__ == "__main__":
    sumoBinary = traci.checkBinary('sumo')  # Use 'sumo-gui' if you want to visualize the simulation
    config_file = "scenarios/lane_change_collision/lane_change_collision.sumocfg"  # Path to the configuration file

    # Start the TraCI connection with the specified SUMO configuration file
    traci.start([sumoBinary, "-c", config_file])

    run_simulation()  # Run the simulation
