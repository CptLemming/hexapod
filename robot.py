import time


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

    def move_mid(self):
        if self.min_rotation > self.max_rotation:
            mid_rotation = ((self.min_rotation - self.max_rotation) / 2) + self.max_rotation
        else:
            mid_rotation = ((self.max_rotation - self.min_rotation) / 2) + self.min_rotation
        self.pwm.setPWM(self.connector, 0, mid_rotation)

    def move_max(self):
        self.pwm.setPWM(self.connector, 0, self.max_rotation)

    def sleep(self):
        raise NotImplementedError

    def wake_up(self):
        raise NotImplementedError


class Shoulder(Joint):
    min_rotation = 250
    max_rotation = 400

    def sleep(self):
        self.move_max()

    def wake_up(self):
        self.move_mid()


class LeftShoulder(Shoulder):
    min_rotation = 400
    max_rotation = 250


class RightShoulder(Shoulder):
    min_rotation = 250
    max_rotation = 400


class Elbow(Joint):
    min_rotation = 250
    max_rotation = 400

    def sleep(self):
        self.move_max()

    def wake_up(self):
        self.move_min()


class LeftElbow(Elbow):
    min_rotation = 250
    max_rotation = 400


class RightElbow(Elbow):
    max_rotation = 250
    min_rotation = 400


class Wrist(Joint):
    min_rotation = 250
    max_rotation = 400

    def sleep(self):
        self.move_min()

    def wake_up(self):
        self.move_max()


class LeftWrist(Wrist):
    min_rotation = 400
    max_rotation = 250


class RightWrist(Wrist):
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

    def sleep(self):
        self.shoulder.sleep()
        self.elbow.sleep()
        self.wrist.sleep()

    def wake_up(self):
        self.shoulder.wake_up()
        self.elbow.wake_up()
        self.wrist.wake_up()

    def up(self):
        self.elbow.move_min()
        self.wrist.move_max()

    def down(self):
        self.elbow.move_max()
        self.wrist.move_min()

    def forward(self):
        self.shoulder.move_min()

    def backward(self):
        self.shoulder.move_max()


class Hexapod(object):
    arm_1 = None
    arm_2 = None
    arm_3 = None
    arm_4 = None
    arm_5 = None
    arm_6 = None

    sleep_time = 2

    def __init__(self, arm_1, arm_2, arm_3, arm_4, arm_5, arm_6, sleep_time=None):
        """
        Hexapod skeleton
        @type arm_1: Arm
        @type arm_2: Arm
        @type arm_3: Arm
        @type arm_4: Arm
        @type arm_5: Arm
        @type arm_6: Arm
        """
        self.arm_1 = arm_1
        self.arm_2 = arm_2
        self.arm_3 = arm_3
        self.arm_4 = arm_4
        self.arm_5 = arm_5
        self.arm_6 = arm_6

        if sleep_time is not None:
            self.sleep_time = sleep_time

    def sleep(self):
        self.arm_1.sleep()

    def wake_up(self):
        self.arm_1.wake_up()

    def forward(self):
        self.arm_1.up()
        time.sleep(self.sleep_time)

        self.arm_1.forward()
        time.sleep(self.sleep_time)

        self.arm_1.down()
        time.sleep(self.sleep_time)

        self.arm_1.wake_up()
        time.sleep(self.sleep_time)

    def backward(self):
        self.arm_1.up()
        time.sleep(self.sleep_time)

        self.arm_1.backward()
        time.sleep(self.sleep_time)

        self.arm_1.down()
        time.sleep(self.sleep_time)

        self.arm_1.wake_up()
        time.sleep(self.sleep_time)

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

