import RPi.GPIO as GPIO
from time import sleep
import keyboard
#from pynput.keyboard import Key, Controller

GPIO.setmode(GPIO.BOARD)   
# Pins for Motor Driver Inputs 
Motor1in1 = 16 #IN2  
Motor1in2 = 18 #IN1
Motor1E = 22 #EN

def setup():
    GPIO.setwarnings(False)
               # GPIO Numbering
    GPIO.setup(Motor1in1,GPIO.OUT)  # All pins as Outputs
    GPIO.setup(Motor1in2,GPIO.OUT)
    GPIO.setup(Motor1E,GPIO.OUT)
    global p
    p = GPIO.PWM(Motor1E, 20000)
    #p.start(0)
    
    
def loop():
    print('Press W to advance')
    keyboard.wait('w')
    p.start(100)
    #keyboard.add_hotkey('w',lambda:p.start(0))
        # Going forwards
    GPIO.output(Motor1in1,GPIO.HIGH)
    GPIO.output(Motor1in2,GPIO.LOW)
    #GPIO.output(Motor1E,GPIO.HIGH)
    print("Going forwards")
    
    sleep(3)
    
    # Stop
    GPIO.output(Motor1in1,GPIO.LOW)
    GPIO.output(Motor1in2,GPIO.LOW)
    #GPIO.output(Motor1E,GPIO.LOW)
    
    p.stop()
    print('Stopping')
    sleep(4)
    
    '''
    p.start(0)
    
    GPIO.output(Motor1in1,GPIO.LOW)
    GPIO.output(Motor1in2,GPIO.HIGH)
    GPIO.output(Motor1E,GPIO.HIGH)
    print("Going backwards")

    
    sleep(1)
    
    
    # Stop
    GPIO.output(Motor1in1,GPIO.LOW)
    GPIO.output(Motor1in2,GPIO.LOW)
    #GPIO.output(Motor1E,GPIO.LOW)
    
    p.stop()
    
    print("Stop")
'''
def destroy():  
    GPIO.cleanup()

if __name__ == '__main__':     # Program start from here
    setup()
    try:
            loop()
    except KeyboardInterrupt:
        destroy()