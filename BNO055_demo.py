from opensourceleg.sensors.imu import BNO055
from opensourceleg.time.time import SoftRealtimeLoop
from opensourceleg.control.compiled_controller import CompiledController
from opensourceleg.actuators.dephy import DephyActuator, CONTROL_MODES
from pathlib import Path

controller = CompiledController(library_name="IMU_Follower",
                                main_function_name="IMU_Follower",
                                library_path=Path.home()/"MATLAB_ws/R2023a")
controller.define_type("vector3", [("x", controller.types.c_double),
                                   ("y", controller.types.c_double),
                                   ("z", controller.types.c_double)])
controller.define_inputs([("accel", controller.types.vector3),
                          ("gyro", controller.types.vector3)])
controller.define_outputs([('knee_angle_rad',controller.types.c_double)])
imu = BNO055()
imu.start()

# knee = DephyActuator(tag="Knee", gear_ratio=9*83/18, offline=True)
# with knee:
#     knee.home()
#     knee.set_control_mode(CONTROL_MODES.POSITION)
for t in SoftRealtimeLoop(1/100, True):
    imu.update()
    controller.inputs.accel.x = imu.acc_x
    controller.inputs.accel.y = imu.acc_y
    controller.inputs.accel.z = imu.acc_z
    controller.inputs.gyro.x = imu.gyro_x
    controller.inputs.gyro.y = imu.gyro_y
    controller.inputs.gyro.z = imu.gyro_z
    controller.run()
    print(controller.outputs.knee_angle_rad)
        # knee.set_output_position(controller.outputs.knee_angle_rad)

imu.stop()