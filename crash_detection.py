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
    # Calculate mean absolute error (MAE)
    mae = np.mean(np.abs(actual_positions - estimated_positions))
    
    # Calculate root mean square error (RMSE)
    rmse = np.sqrt(np.mean((actual_positions - estimated_positions) ** 2))
    
    return mae, rmse

def compare_tracking_methods(sumo_config):
    # Start SUMO with the given configuration file
    traci.start(["sumo", "-c", sumo_config])
    
    # Set the time step for vehicle tracking (e.g., 0.1 seconds)
    time_step = 0.1
    
    # Initialize arrays to store actual and estimated positions
    actual_positions = {}
    estimated_positions_kalman = {}
    estimated_positions_constant_speed = {}
    
    # Initialize the Kalman filter states and covariances for each vehicle
    kalman_states = {}
    kalman_covariances = {}
    
    # Main simulation loop
    while traci.simulation.getMinExpectedNumber() > 0:
        # Advance the simulation by one step
        traci.simulationStep()
        
        # Get the current simulation time
        current_time = traci.simulation.getTime()
        
        # Get the list of vehicles in the simulation
        vehicle_ids = traci.vehicle.getIDList()
        
        # Update the actual and estimated positions for each vehicle
        for vehicle_id in vehicle_ids:
            # Get the actual position of the vehicle
            actual_pos = traci.vehicle.getPosition(vehicle_id)
            
            if vehicle_id not in actual_positions:
                actual_positions[vehicle_id] = []
                estimated_positions_kalman[vehicle_id] = []
                estimated_positions_constant_speed[vehicle_id] = []
            
            actual_positions[vehicle_id].append(actual_pos[0])
            
            # Estimate the position using the Kalman filter
            if vehicle_id not in kalman_states:
                pos = actual_pos
                vel = traci.vehicle.getSpeed(vehicle_id)
                kalman_states[vehicle_id] = np.array([[pos[0]], [vel]])
                kalman_covariances[vehicle_id] = np.eye(2)
            else:
                kalman_states[vehicle_id], kalman_covariances[vehicle_id] = kalman_filter(
                    vehicle_id, time_step, kalman_states[vehicle_id], kalman_covariances[vehicle_id])
            
            estimated_positions_kalman[vehicle_id].append(kalman_states[vehicle_id][0, 0])
            
            # Estimate the position using the constant speed model
            estimated_pos_constant_speed = constant_speed_model(vehicle_id, time_step)
            estimated_positions_constant_speed[vehicle_id].append(estimated_pos_constant_speed[0])
        
        # Perform crash detection using the Kalman filter estimates
        # ...
        
        # Perform crash detection using the constant speed model estimates
        # ...
    
    # Close the TraCI connection
    traci.close()
    
    # Calculate tracking accuracy metrics for each vehicle
    kalman_mae_sum = 0
    kalman_rmse_sum = 0
    constant_speed_mae_sum = 0
    constant_speed_rmse_sum = 0
    
    for vehicle_id in vehicle_ids:
        actual_pos = np.array(actual_positions[vehicle_id])
        estimated_pos_kalman = np.array(estimated_positions_kalman[vehicle_id])
        estimated_pos_constant_speed = np.array(estimated_positions_constant_speed[vehicle_id])
        
        kalman_mae, kalman_rmse = calculate_metrics(actual_pos, estimated_pos_kalman)
        constant_speed_mae, constant_speed_rmse = calculate_metrics(actual_pos, estimated_pos_constant_speed)
        
        kalman_mae_sum += kalman_mae
        kalman_rmse_sum += kalman_rmse
        constant_speed_mae_sum += constant_speed_mae
        constant_speed_rmse_sum += constant_speed_rmse
    
    # Calculate average tracking accuracy metrics
    num_vehicles = len(vehicle_ids)
    if num_vehicles > 0:
        kalman_mae_avg = kalman_mae_sum / num_vehicles
        kalman_rmse_avg = kalman_rmse_sum / num_vehicles
        constant_speed_mae_avg = constant_speed_mae_sum / num_vehicles
        constant_speed_rmse_avg = constant_speed_rmse_sum / num_vehicles
    else:
        kalman_mae_avg = 0
        kalman_rmse_avg = 0
        constant_speed_mae_avg = 0
        constant_speed_rmse_avg = 0
    
    print("Kalman Filter - Average MAE:", kalman_mae_avg)
    print("Kalman Filter - Average RMSE:", kalman_rmse_avg)
    print("Constant Speed Model - Average MAE:", constant_speed_mae_avg)
    print("Constant Speed Model - Average RMSE:", constant_speed_rmse_avg)
    
    # Compare crash detection results
    # ...

# Run the comparison for each scenario
compare_tracking_methods("scenarios/rear_end_collision/rear_end_collision.sumocfg")
compare_tracking_methods("scenarios/intersection_collision/intersection_collision.sumocfg")
