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

	#Setup L293d Pins
    GPIO.setwarnings(False)
    GPIO.setup(Motor1in1,GPIO.OUT)
    GPIO.setup(Motor1in2,GPIO.OUT)
    GPIO.setup(Motor1E,GPIO.OUT)


	#Setup the Speed (PWR / Freq)
    global p
    global pwr
    p = GPIO.PWM(Motor1E, 20000)
    pwr = 0
    p.start(pwr)
   

def moveforward():
	# Going forwards
    p.start(pwr)
    GPIO.output(Motor1in1,GPIO.HIGH)
    GPIO.output(Motor1in2,GPIO.LOW)
    print("Going forwards")

def moveback():
	# Going backwards
    p.start(pwr)
    GPIO.output(Motor1in1,GPIO.HIGH)
    GPIO.output(Motor1in2,GPIO.LOW)
    print("Going backwards")

def stop():
	# Stop (Stop Motors Only)
    GPIO.output(Motor1in1,GPIO.LOW)
    GPIO.output(Motor1in2,GPIO.LOW)
    print('Stopping')

def emerstop():
	# EmergencyStop (Remove Speed)
    GPIO.output(Motor1in1,GPIO.LOW)
    GPIO.output(Motor1in2,GPIO.LOW)
    p.stop()
    print('Emergency Stop')

def on_press('up'):
    moveforward()

def on_release('up'):
    stop()

def on_press('down'):
    moveback()

def on_release('down'):
    stop()

def on_press('space'):
    emerstop()

# When Button is pressed Run the Function
with keyboard.Listener(on_press=on_press,     on_release=on_release) as listener:
    listener.join()

def loop():

    print('Ignition Started!')
    sleep(2)
    print('Ready To Move')
    print('UP button to move Forwards')
    print('Down button to move Backwards')
    print('Space button to Emergency Stop')

    

def destroy():  
    GPIO.cleanup()

if __name__ == '__main__':     # Program start from here
    setup()
    try:
            loop()
    except KeyboardInterrupt:
        destroy()