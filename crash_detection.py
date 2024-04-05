import os
import sys
import numpy as np
from kalman_filter import kalman_filter
from constant_speed_model import constant_speed_model

# Add SUMO_HOME to the system path
if 'SUMO_HOME' in os.environ:
    tools = os.path.join(os.environ['SUMO_HOME'], 'tools')
    sys.path.append(tools)
else:
    sys.exit("Please declare the environment variable 'SUMO_HOME'")

import traci

def calculate_metrics(actual_positions, estimated_positions):
    mae = np.mean(np.abs(actual_positions - estimated_positions))
    rmse = np.sqrt(np.mean((actual_positions - estimated_positions) ** 2))
    return mae, rmse

def compare_tracking_methods(sumo_config):
    traci.start(["sumo", "-c", sumo_config])
    time_step = 0.1
    actual_positions = {}
    estimated_positions_kalman = {}
    estimated_positions_constant_speed = {}
    kalman_states = {}
    kalman_covariances = {}

    while traci.simulation.getMinExpectedNumber() > 0:
        traci.simulationStep()
        current_time = traci.simulation.getTime()
        vehicle_ids = traci.vehicle.getIDList()

        for vehicle_id in vehicle_ids:
            actual_pos = traci.vehicle.getPosition(vehicle_id)
            if vehicle_id not in actual_positions:
                actual_positions[vehicle_id] = []
                estimated_positions_kalman[vehicle_id] = []
                estimated_positions_constant_speed[vehicle_id] = []
            actual_positions[vehicle_id].append(actual_pos[0])
            if vehicle_id not in kalman_states:
                pos = actual_pos
                vel = traci.vehicle.getSpeed(vehicle_id)
                kalman_states[vehicle_id] = np.array([[pos[0]], [vel]])
                kalman_covariances[vehicle_id] = np.eye(2)
            else:
                kalman_states[vehicle_id], kalman_covariances[vehicle_id] = kalman_filter(
                    vehicle_id, time_step, kalman_states[vehicle_id], kalman_covariances[vehicle_id])
            estimated_positions_kalman[vehicle_id].append(kalman_states[vehicle_id][0, 0])
            estimated_pos_constant_speed = constant_speed_model(vehicle_id, time_step)
            estimated_positions_constant_speed[vehicle_id].append(estimated_pos_constant_speed[0])

    traci.close()
    # Metric calculations and comparisons would be here...

# Example usage for both scenarios
compare_tracking_methods("scenarios/rear_end_collision/rear_end_collision.sumocfg")
compare_tracking_methods("scenarios/lane_change_collision/lane_change_collision.sumocfg")