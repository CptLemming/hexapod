

class Joint(object):
    pwm = None
    connector = None
    min_rotation = 0
    max_rotation = 100

    def __init__(self, pwm, connector, min=None, max=None):
        self.pwm = pwm
        self.connector = connector

        if min is not None:
            self.min_rotation = min

        if max is not None:
            self.max_rotation = max

    def move_min(self):
        self.pwm.setPWM(self.connector, 0, self.min_rotation)

    def move_max(self):
        self.pwm.setPWM(self.connector, 0, self.max_rotation)


class Shoulder(Joint):
    min_rotation = 250
    max_rotation = 400


class Elbow(Joint):
    min_rotation = 250
    max_rotation = 400


class Wrist(Joint):
    min_rotation = 250
    max_rotation = 400


class Arm(object):
    shoulder = None
    elbow = None
    wrist = None

    def __init__(self, shoulder, elbow, wrist):
        self.shoulder = shoulder
        self.elbow = elbow
        self.wrist = wrist

    def forward(self):
        self.shoulder.move_min()
        self.elbow.move_max()
        self.wrist.move_min()

    def backward(self):
        self.shoulder.move_max()
        self.elbow.move_min()
        self.wrist.move_max()


class Hexapod(object):
    arm_1 = None
    arm_2 = None
    arm_3 = None
    arm_4 = None
    arm_5 = None
    arm_6 = None

    def __init__(self, arm_1, arm_2, arm_3, arm_4, arm_5, arm_6):
        self.arm_1 = arm_1
        self.arm_2 = arm_2
        self.arm_3 = arm_3
        self.arm_4 = arm_4
        self.arm_5 = arm_5
        self.arm_6 = arm_6

    def forward(self):
        self.arm_1.forward()

    def backward(self):
        self.arm_1.backward()

    def strafe_left(self):
        pass

    def strafe_right(self):
        pass

    def left(self):
        pass

    def right(self):
        pass

    def raise_body(self):
        pass

    def lower_body(self):
        pass
