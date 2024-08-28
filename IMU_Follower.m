function outputs = IMU_Follower(inputs)
persistent fusion_filter
if isempty(fusion_filter)
    fusion_filter = imufilter('SampleRate',100, 'ReferenceFrame','NED');
end
q = fusion_filter([inputs.accel.x, inputs.accel.y, inputs.accel.z], ...
                  [inputs.gyro.x, inputs.gyro.y, inputs.gyro.z]);
euler_angles = quat2eul(q); 
outputs.knee_angle_rad = max(min(euler_angles(3), pi/2), 0); 
end