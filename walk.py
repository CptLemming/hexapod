import time

from Adafruit-Raspberry-Pi-Python-Code.Adafruit_PWM_Servo_Driver import PWM

from robot import Shoulder, Elbow, Wrist, Arm, Hexapod


sleep_time = 2

left_pwm = PWM(0x40, debug=True)
left_pwm.setPWMFreq(60)

shoulder_1 = Shoulder(left_pwm, 0)
elbow_1 = Elbow(left_pwm, 1)
wrist_1 = Wrist(left_pwm, 2)
arm_1 = Arm(shoulder_1, elbow_1, wrist_1)

hexapod = Hexapod(arm_1, None, None, None, None, None)

while True:
    hexapod.forward()
    time.sleep(sleep_time)

    hexapod.backward()
    time.sleep(sleep_time)
