import time
import Tkinter
import tkMessageBox

from Adafruit_PWM_Servo_Driver import PWM

from robot import LeftShoulder, RightShoulder, LeftElbow, RightElbow, LeftWrist, RightWrist, Arm, Hexapod


top = Tkinter.Tk()

left_pwm = PWM(0x40)
left_pwm.setPWMFreq(60)

right_pwm = PWM(0x41)
right_pwm.setPWMFreq(60)


shoulder_1 = LeftShoulder(left_pwm, 0)
elbow_1 = LeftElbow(left_pwm, 1)
wrist_1 = LeftWrist(left_pwm, 2)
arm_1 = Arm(shoulder_1, elbow_1, wrist_1)

shoulder_2 = LeftShoulder(left_pwm, 4)
elbow_2 = LeftElbow(left_pwm, 5)
wrist_2 = LeftWrist(left_pwm, 6)
arm_2 = Arm(shoulder_2, elbow_2, wrist_2)

shoulder_3 = LeftShoulder(left_pwm, 8)
elbow_3 = LeftElbow(left_pwm, 9)
wrist_3 = LeftWrist(left_pwm, 10)
arm_3 = Arm(shoulder_3, elbow_3, wrist_3)

shoulder_4 = RightShoulder(right_pwm, 0)
elbow_4 = RightElbow(right_pwm, 1)
wrist_4 = RightWrist(right_pwm, 2)
arm_4 = Arm(shoulder_4, elbow_4, wrist_4)

shoulder_5 = RightShoulder(right_pwm, 4)
elbow_5 = RightElbow(right_pwm, 5)
wrist_5 = RightWrist(right_pwm, 6)
arm_5 = Arm(shoulder_5, elbow_5, wrist_5)

shoulder_6 = RightShoulder(right_pwm, 8)
elbow_6 = RightElbow(right_pwm, 9)
wrist_6 = RightWrist(right_pwm, 10)
arm_6 = Arm(shoulder_6, elbow_6, wrist_6)

hexapod = Hexapod(arm_1, arm_2, arm_3, arm_4, arm_5, arm_6)

def left_shoulder_min():
    shoulder_1.move_min()
    shoulder_2.move_min()
    shoulder_3.move_min()
    
def left_shoulder_max():
    shoulder_1.move_max()
    shoulder_2.move_max()
    shoulder_3.move_max()

def left_elbow_min():
    elbow_1.move_min()
    elbow_2.move_min()
    elbow_3.move_min()

def left_elbow_max():
    elbow_1.move_max()
    elbow_2.move_max()
    elbow_3.move_max()

def left_wrist_min():
    wrist_1.move_min()
    wrist_2.move_min()
    wrist_3.move_min()

def left_wrist_max():
    wrist_1.move_max()
    wrist_2.move_max()
    wrist_3.move_max()

def right_shoulder_min():
    shoulder_4.move_min()
    shoulder_5.move_min()
    shoulder_6.move_min()
    
def right_shoulder_max():
    shoulder_4.move_max()
    shoulder_5.move_max()
    shoulder_6.move_max()

def right_elbow_min():
    elbow_4.move_min()
    elbow_5.move_min()
    elbow_6.move_min()

def right_elbow_max():
    elbow_4.move_max()
    elbow_5.move_max()
    elbow_6.move_max()

def right_wrist_min():
    wrist_4.move_min()
    wrist_5.move_min()
    wrist_6.move_min()

def right_wrist_max():
    wrist_4.move_max()
    wrist_5.move_max()
    wrist_6.move_max()


def hello_cb():
    tkMessageBox.showinfo('Hello', 'HELLO')

class App:
    def __init__(self, master):
        frame = Tkinter.Frame(master)
        frame.pack()
        self.button = Tkinter.Button(frame, text="Quit", fg="red", command=frame.quit)
        self.button.grid(row=0, column=0)

        self.shoulder_1_wake = Tkinter.Button(frame, text="Shoulder 1 Min", command=shoulder_1.move_min)
        self.shoulder_1_wake.grid(row=1, column=0)
        self.shoulder_1_sleep = Tkinter.Button(frame, text="Shoulder 1 Max", command=shoulder_1.move_max)
        self.shoulder_1_sleep.grid(row=1, column=1)

        self.elbow_1_wake = Tkinter.Button(frame, text="Elbow 1 Min", command=elbow_1.move_min)
        self.elbow_1_wake.grid(row=1, column=2)
        self.elbow_1_sleep = Tkinter.Button(frame, text="Elbow 1 Max", command=elbow_1.move_max)
        self.elbow_1_sleep.grid(row=1, column=3)

        self.wrist_1_wake = Tkinter.Button(frame, text="Wrist 1 Down", command=wrist_1.move_min)
        self.wrist_1_wake.grid(row=1, column=4)
        self.wrist_1_sleep = Tkinter.Button(frame, text="Wrist 1 Up", command=wrist_1.move_max)
        self.wrist_1_sleep.grid(row=1, column=5)

        self.shoulder_2_wake = Tkinter.Button(frame, text="Shoulder 2 Min", command=shoulder_2.move_min)
        self.shoulder_2_wake.grid(row=2, column=0)
        self.shoulder_2_sleep = Tkinter.Button(frame, text="Shoulder 2 Max", command=shoulder_2.move_max)
        self.shoulder_2_sleep.grid(row=2, column=1)

        self.elbow_2_wake = Tkinter.Button(frame, text="Elbow 2 Min", command=elbow_2.move_min)
        self.elbow_2_wake.grid(row=2, column=2)
        self.elbow_2_sleep = Tkinter.Button(frame, text="Elbow 2 Max", command=elbow_2.move_max)
        self.elbow_2_sleep.grid(row=2, column=3)

        self.wrist_2_wake = Tkinter.Button(frame, text="Wrist 2 Down", command=wrist_2.move_min)
        self.wrist_2_wake.grid(row=2, column=4)
        self.wrist_2_sleep = Tkinter.Button(frame, text="Wrist 2 Up", command=wrist_2.move_max)
        self.wrist_2_sleep.grid(row=2, column=5)

        self.shoulder_3_wake = Tkinter.Button(frame, text="Shoulder 3 Min", command=shoulder_3.move_min)
        self.shoulder_3_wake.grid(row=3, column=0)
        self.shoulder_3_sleep = Tkinter.Button(frame, text="Shoulder 3 Max", command=shoulder_3.move_max)
        self.shoulder_3_sleep.grid(row=3, column=1)

        self.elbow_3_wake = Tkinter.Button(frame, text="Elbow 3 Min", command=elbow_3.move_min)
        self.elbow_3_wake.grid(row=3, column=2)
        self.elbow_3_sleep = Tkinter.Button(frame, text="Elbow 3 Max", command=elbow_3.move_max)
        self.elbow_3_sleep.grid(row=3, column=3)

        self.wrist_3_wake = Tkinter.Button(frame, text="Wrist 3 Down", command=wrist_3.move_min)
        self.wrist_3_wake.grid(row=3, column=4)
        self.wrist_3_sleep = Tkinter.Button(frame, text="Wrist 3 Up", command=wrist_3.move_max)
        self.wrist_3_sleep.grid(row=3, column=5)
        
        self.left_shoulder_wake = Tkinter.Button(frame, text="Left Shoulder Min", command=left_shoulder_min)
        self.left_shoulder_wake.grid(row=4, column=0)
        self.left_shoulder_sleep = Tkinter.Button(frame, text="Left Shoulder Max", command=left_shoulder_max)
        self.left_shoulder_sleep.grid(row=4, column=1)

        self.left_elbow_wake = Tkinter.Button(frame, text="Left Elbow Min", command=left_elbow_min)
        self.left_elbow_wake.grid(row=4, column=2)
        self.left_elbow_sleep = Tkinter.Button(frame, text="Left Elbow Max", command=left_elbow_max)
        self.left_elbow_sleep.grid(row=4, column=3)

        self.left_wrist_wake = Tkinter.Button(frame, text="Left Wrist Down", command=left_wrist_min)
        self.left_wrist_wake.grid(row=4, column=4)
        self.left_wrist_sleep = Tkinter.Button(frame, text="Left Wrist Up", command=left_wrist_max)
        self.left_wrist_sleep.grid(row=4, column=5)

        self.shoulder_4_wake = Tkinter.Button(frame, text="Shoulder 4 Min", command=shoulder_4.move_min)
        self.shoulder_4_wake.grid(row=5, column=0)
        self.shoulder_4_sleep = Tkinter.Button(frame, text="Shoulder 4 Max", command=shoulder_4.move_max)
        self.shoulder_4_sleep.grid(row=5, column=1)

        self.elbow_4_wake = Tkinter.Button(frame, text="Elbow 4 Min", command=elbow_4.move_min)
        self.elbow_4_wake.grid(row=5, column=2)
        self.elbow_4_sleep = Tkinter.Button(frame, text="Elbow 4 Max", command=elbow_4.move_max)
        self.elbow_4_sleep.grid(row=5, column=3)

        self.wrist_4_wake = Tkinter.Button(frame, text="Wrist 4 Down", command=wrist_4.move_min)
        self.wrist_4_wake.grid(row=5, column=4)
        self.wrist_4_sleep = Tkinter.Button(frame, text="Wrist 4 Up", command=wrist_4.move_max)
        self.wrist_4_sleep.grid(row=5, column=5)

        self.shoulder_5_wake = Tkinter.Button(frame, text="Shoulder 5 Min", command=shoulder_5.move_min)
        self.shoulder_5_wake.grid(row=6, column=0)
        self.shoulder_5_sleep = Tkinter.Button(frame, text="Shoulder 5 Max", command=shoulder_5.move_max)
        self.shoulder_5_sleep.grid(row=6, column=1)

        self.elbow_5_wake = Tkinter.Button(frame, text="Elbow 5 Min", command=elbow_5.move_min)
        self.elbow_5_wake.grid(row=6, column=2)
        self.elbow_5_sleep = Tkinter.Button(frame, text="Elbow 5 Max", command=elbow_5.move_max)
        self.elbow_5_sleep.grid(row=6, column=3)

        self.wrist_5_wake = Tkinter.Button(frame, text="Wrist 5 Down", command=wrist_5.move_min)
        self.wrist_5_wake.grid(row=6, column=4)
        self.wrist_5_sleep = Tkinter.Button(frame, text="Wrist 5 Up", command=wrist_5.move_max)
        self.wrist_5_sleep.grid(row=6, column=5)

        self.shoulder_6_wake = Tkinter.Button(frame, text="Shoulder 6 Min", command=shoulder_6.move_min)
        self.shoulder_6_wake.grid(row=7, column=0)
        self.shoulder_6_sleep = Tkinter.Button(frame, text="Shoulder 6 Max", command=shoulder_6.move_max)
        self.shoulder_6_sleep.grid(row=7, column=1)

        self.elbow_6_wake = Tkinter.Button(frame, text="Elbow 6 Min", command=elbow_6.move_min)
        self.elbow_6_wake.grid(row=7, column=2)
        self.elbow_6_sleep = Tkinter.Button(frame, text="Elbow 6 Max", command=elbow_6.move_max)
        self.elbow_6_sleep.grid(row=7, column=3)

        self.wrist_6_wake = Tkinter.Button(frame, text="Wrist 6 Down", command=wrist_6.move_min)
        self.wrist_6_wake.grid(row=7, column=4)
        self.wrist_6_sleep = Tkinter.Button(frame, text="Wrist 6 Up", command=wrist_6.move_max)
        self.wrist_6_sleep.grid(row=7, column=5)
        
        self.right_shoulder_wake = Tkinter.Button(frame, text="Right Shoulder Min", command=right_shoulder_min)
        self.right_shoulder_wake.grid(row=8, column=0)
        self.right_shoulder_sleep = Tkinter.Button(frame, text="Right Shoulder Max", command=right_shoulder_max)
        self.right_shoulder_sleep.grid(row=8, column=1)

        self.right_elbow_wake = Tkinter.Button(frame, text="Right Elbow Min", command=right_elbow_min)
        self.right_elbow_wake.grid(row=8, column=2)
        self.right_elbow_sleep = Tkinter.Button(frame, text="Right Elbow Max", command=right_elbow_max)
        self.right_elbow_sleep.grid(row=8, column=3)

        self.right_wrist_wake = Tkinter.Button(frame, text="Right Wrist Down", command=right_wrist_min)
        self.right_wrist_wake.grid(row=8, column=4)
        self.right_wrist_sleep = Tkinter.Button(frame, text="Right Wrist Up", command=right_wrist_max)
        self.right_wrist_sleep.grid(row=8, column=5)


app = App(top)
top.mainloop()

