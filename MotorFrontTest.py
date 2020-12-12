import RPi.GPIO as GPIO
from time import sleep
import keyboard
from pynput.keyboard import Key, Listener



'''
Set up + Mappings
'''

GPIO.setmode(GPIO.BOARD)   

# Set up GPIO to L293d Mapping 
Motor1in1 = 16 #IN2  
Motor1in2 = 18 #IN1
Motor1E = 22 #EN1
Motor2in1 = 13 #IN3  
Motor2in2 = 11 #IN4
Motor2E = 15 #EN2

#def setup():

    #Setup L293d Pins
GPIO.setwarnings(False)
GPIO.setup(Motor1in1,GPIO.OUT)
GPIO.setup(Motor1in2,GPIO.OUT)
GPIO.setup(Motor1E,GPIO.OUT)
GPIO.setup(Motor2in1,GPIO.OUT)
GPIO.setup(Motor2in2,GPIO.OUT)
GPIO.setup(Motor2E,GPIO.OUT)

    #Setup the Speed (PWR / Freq)

    #Motor 1 Back / Acceleration
global m1p
global m1pwr
m1p = GPIO.PWM(Motor1E, 10000)
m1pwr = 100
m1p.start(m1pwr)
   
    #Motor 2 Front / Steering
global m2p
global m2pwr
m2p = GPIO.PWM(Motor2E, 10000)
m2pwr = 100
m2p.start(m2pwr)
'''
Power To Motors
'''
def moveforward():
    # Going forwards
    m1p.start(m1pwr)
    GPIO.output(Motor1in1,GPIO.HIGH)
    GPIO.output(Motor1in2,GPIO.LOW)
    print("Going forwards")

def moveback():
    # Going backwards
    m1p.start(m1pwr)
    GPIO.output(Motor1in1,GPIO.LOW)
    GPIO.output(Motor1in2,GPIO.HIGH)
    print("Going backwards")

def moveright():
    # Going right
    m2p.start(m2pwr)
    GPIO.output(Motor2in1,GPIO.HIGH)
    GPIO.output(Motor2in2,GPIO.LOW)
    print("Turning forward / right")

def moveleft():
    # Going left
    m2p.start(m2pwr)
    GPIO.output(Motor2in1,GPIO.LOW)
    GPIO.output(Motor2in2,GPIO.HIGH)
    print("turning backward / left")

def stopm1():
    # Stop Back Motors (Stop Motors Only) 
    GPIO.output(Motor1in1,GPIO.LOW)
    GPIO.output(Motor1in2,GPIO.LOW)
    print('Stopping')

def stopm2():
    # Stop Front Motors (Stop Motors Only)
    GPIO.output(Motor2in1,GPIO.LOW)
    GPIO.output(Motor2in2,GPIO.LOW)
    print('Stopping')

def emerstop():
    # EmergencyStop (Remove Speed)
    GPIO.output(Motor1in1,GPIO.LOW)
    GPIO.output(Motor1in2,GPIO.LOW)
    GPIO.output(Motor2in1,GPIO.LOW)
    GPIO.output(Motor2in2,GPIO.LOW)
    m1p.stop()
    m2p.stop()
    print('Emergency Stop')

def on_press(key):
    #print('{0}is pressed'.format(key))
    
    if key == Key.up:
        moveforward();
    if key == Key.down:
        moveback();
    if key == Key.right:
        moveright();
    if key == Key.left:
        moveleft();
    
    
def on_release(key):
    stopm1();
    
# When Button is pressed Run the Function
with Listener(on_press=on_press,
              on_release=on_release,
              ) as listener:
    listener.join()

'''
Program Start
'''

def loop():

    print('Ignition Started!')
    sleep(2)
    print('Ready To Move')
    print('UP button to move Forwards')
    print('Down button to move Backwards')
    print('Space button to Emergency Stop')
    raw_input("MOVE NOW")
    
    
    
'''

    moveleft()
    sleep(.5)
    stopm2()
    sleep(2)
    moveright()
    sleep(.5)
    stopm2()
    sleep(2)
 
'''

 
def destroy():  
    GPIO.cleanup()

if __name__ == '__main__':     # Program start from here
    setup()
    try:
            loop()
    except KeyboardInterrupt:
        destroy()