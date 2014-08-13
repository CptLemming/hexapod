import time

from Adafruit_PWM_Servo_Driver import PWM

from robot import Shoulder, Elbow, Wrist, Arm, Hexapod


left_pwm = PWM(0x40, debug=True)
left_pwm.setPWMFreq(60)

right_pwm = PWM(0x41, debug=True)
right_pwm.setPWMFreq(60)


shoulder_1 = Shoulder(left_pwm, 0)
elbow_1 = Elbow(left_pwm, 1)
wrist_1 = Wrist(left_pwm, 2)
arm_1 = Arm(shoulder_1, elbow_1, wrist_1)

shoulder_2 = Shoulder(left_pwm, 4)
elbow_2 = Elbow(left_pwm, 5)
wrist_2 = Wrist(left_pwm, 6)
arm_2 = Arm(shoulder_2, elbow_2, wrist_2)

shoulder_3 = Shoulder(left_pwm, 8)
elbow_3 = Elbow(left_pwm, 9)
wrist_3 = Wrist(left_pwm, 10)
arm_3 = Arm(shoulder_3, elbow_3, wrist_3)

shoulder_4 = Shoulder(right_pwm, 0)
elbow_4 = Elbow(right_pwm, 1)
wrist_4 = Wrist(right_pwm, 2)
arm_4 = Arm(shoulder_4, elbow_4, wrist_4)

shoulder_5 = Shoulder(right_pwm, 4)
elbow_5 = Elbow(right_pwm, 5)
wrist_5 = Wrist(right_pwm, 6)
arm_5 = Arm(shoulder_5, elbow_5, wrist_5)

shoulder_6 = Shoulder(right_pwm, 8)
elbow_6 = Elbow(right_pwm, 9)
wrist_6 = Wrist(right_pwm, 10)
arm_6 = Arm(shoulder_6, elbow_6, wrist_6)

hexapod = Hexapod(arm_1, arm_2, arm_3, arm_4, arm_5, arm_6)
