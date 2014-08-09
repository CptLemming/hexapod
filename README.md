# Hexapod

A Raspberry Pi Hexapod project, using 2x I2C controllers to control 18 servos.

## Requirements

```
sudo apt-get install python-smbus
sudo apt-get install i2c-tools
sudo apt-get install smbus

git clone https://github.com/adafruit/Adafruit-Raspberry-Pi-Python-Code.git
```

## Link the libraries

```
ln -s Adafruit-Raspberry-Pi-Python-Code/Adafruit_I2C/Adafruit_I2C.py Adafruit_I2C.py
ln -s Adafruit-Raspberry-Pi-Python-Code/Adafruit_PWM_Servo_Driver/Adafruit_PWM_Servo_Driver.py Adafruit_PWM_Servo_Driver.py
```

## Detect connected I2C

```
sudo i2cdetect -y 1
```
