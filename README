# MATLAB_Python_IMU_Demo
This work was performed at the University of Michigan Robotics Department with the [Locomotor Control Systems Lab](https://locolab.robotics.umich.edu/index.html) and the [Neurobionics Lab](https://neurobionics.robotics.umich.edu/).

## Summary
This repository was developed to demonstrate a framework for combining MATLAB and Python for rapid control system prototyping. 
This particular example shows how to use MATLAB to perform sensor fusion with a low-cost IMU and to use the result to control the knee joint of the Open-Source Leg. 

I presented this framework at the BioRob 2024 conference workshop entitled "Accelerating Wearable Robotics: Advancements in Mechatronic Prostheses and Exoskeletons and Rapid Control Prototyping" in Heidelberg, Germany. If possible after the conference, I will link the talk recording here. 

## Details
There are two main files: 
1) `IMU_Follower.m` implements MATLAB's IMU Kalman filtering algorithm to calculate device orientation from raw accelerometer and gyroscope signals. We clamp the output between 0 and $\pi/2$ to prevent exceeding the hardware's range of motion. We convert this MATLAB function to a compiled library using MATLAB Coder (see `IMU_Follower.prj`). 
2) `BNO055_demo.py` handles communication with the sensor and the Open Source Leg hardware. It leverages the [OSL Software Library](https://www.opensourceleg.org/control/api?package=hardware&module=actuators&class=ActpackMode) to control the knee joint of the prosthesis based on the calculated IMU angle. 