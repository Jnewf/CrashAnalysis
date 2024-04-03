import traci

def run_simulation():
    traci.start(["sumo", "-c", "path/to/sumo/config.sumocfg"])
    
    while traci.simulation.getMinExpectedNumber() > 0:
        traci.simulationStep()
        
        vehicle_ids = traci.vehicle.getIDList()
        
        for vehicle_id in vehicle_ids:
            # Get trajectory information
            position = traci.vehicle.getPosition(vehicle_id)
            speed = traci.vehicle.getSpeed(vehicle_id)
            
            # Simulate communication losses
            if random.random() < 0.1:  # 10% probability of communication loss
                traci.vehicle.setParameter(vehicle_id, "communication_loss", "true")
            else:
                traci.vehicle.setParameter(vehicle_id, "communication_loss", "false")
            
            # Modify trajectory data
            modified_position = modify_position(position)
            modified_speed = modify_speed(speed)
            
            # Update vehicle state based on modified data
            traci.vehicle.setSpeed(vehicle_id, modified_speed)
            
            # Perform crash detection
            detect_crash(vehicle_id, modified_position, modified_speed)
    
    traci.close()

def modify_position(position):
    # Modify position data based on your requirements
    # ...
    return modified_position

def modify_speed(speed):
    # Modify speed data based on your requirements
    # ...
    return modified_speed

def detect_crash(vehicle_id, position, speed):
    # Perform crash detection using the modified trajectory data
    # ...
    # Log detected crashes or store results
    # ...

run_simulation()