def constant_speed_model(vehicle_id, time_step):
    # Get the current position and velocity of the vehicle
    pos = traci.vehicle.getPosition(vehicle_id)
    vel = traci.vehicle.getSpeed(vehicle_id)
    
    # Estimate the future position using the constant speed model
    future_pos = (pos[0] + vel * time_step, pos[1])
    
    return future_pos