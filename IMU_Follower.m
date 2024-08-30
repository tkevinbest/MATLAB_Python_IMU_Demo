function outputs = IMU_Follower(inputs)
% IMU_Follower: A function that processes raw IMU accelerometer and
% gyroscope data to calculate spatial rotation about the x axis. 

% Author: Kevin Best
% Date: August 28th, 2024
persistent fusion_filter
if isempty(fusion_filter)
    fusion_filter = imufilter('SampleRate',100, 'ReferenceFrame','NED');
end
q = fusion_filter([inputs.accel.x, inputs.accel.y, inputs.accel.z], ...
                  [inputs.gyro.x, inputs.gyro.y, inputs.gyro.z]);
euler_angles = quat2eul(q); 
outputs.knee_angle_rad = max(min(euler_angles(3), 3*pi/4), 0); 
end

