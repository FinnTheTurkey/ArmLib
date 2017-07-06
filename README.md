# ArmLib
A library for controlling the MeArm from python through serial

# Setup
First, you have to download the Arduino program called "ArmlibBackend" onto your Arduino.
Make sure you have all your servos correctly wired up. (See below)
Then, install pyserial so python can communicate with the arm. Note: armlib is written for Python3
You can install pyserial by typing into a command line:
```python
python3 -m pip install pyserial
```

# Use

First, import armlib.
```python
import armlib
```
Then, find your arm:
```python
arm = armlib.findarm()
```

Now, each servo has a name:
1. **Turn:** moves the bottom of the arm. Pin 3
2. **Nod:** moves the gripper up and down. Pin 9
3. **Extend:** moves the arm forward. Pin 5
4. **Gripper:** moves the gripper towards each other. Pin 6

To control each one, type <arm.set> And then the servo's name. Each of these commands take a number from 0-1000.
Don't worry about driving the servos to far, because the program won't let you.
Example:
```python
arm.setTurn(500) # will turn the arm half way. It is like turning the arm 90 degrees
```

