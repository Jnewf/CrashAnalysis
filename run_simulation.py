import traci
import random

def modify_position(position):
    # Placeholder for position modification logic
    return position

def modify_speed(speed):
    # Placeholder for speed modification logic
    return speed

def detect_crash(vehicle_id, position, speed):
    # Placeholder for crash detection logic

def run_simulation(scenario_name):
    config_file = f"scenarios/{scenario_name}/{scenario_name}.sumocfg"
    traci.start(["sumo", "-c", config_file])

    while traci.simulation.getMinExpectedNumber() > 0:
        traci.simulationStep()
        vehicle_ids = traci.vehicle.getIDList()

        for vehicle_id in vehicle_ids:
            position = traci.vehicle.getPosition(vehicle_id)
            speed = traci.vehicle.getSpeed(vehicle_id)
            if random.random() < 0.1:  # Simulating 10% probability of communication loss
                traci.vehicle.setParameter(vehicle_id, "communication_loss", "true")
            else:
                traci.vehicle.setParameter(vehicle_id, "communication_loss", "false")
            modified_position = modify_position(position)
            modified_speed = modify_speed(speed)
            traci.vehicle.setSpeed(vehicle_id, modified_speed)
            detect_crash(vehicle_id, modified_position, modified_speed)

    traci.close()

# Example usage for both scenarios
run_simulation("rear_end_collision")
run_simulation("lane_change_collision")