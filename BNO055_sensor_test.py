from opensourceleg.sensors.imu import BNO055
from opensourceleg.time.time import SoftRealtimeLoop

loop = SoftRealtimeLoop(1/100, True)
imu = BNO055()
imu.start()
for t in loop:
    imu.update()
    print(imu.acc_x)

imu.stop()