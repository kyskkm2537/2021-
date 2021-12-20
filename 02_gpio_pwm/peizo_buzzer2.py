import RPi.GPIO as GPIO
import time

BUZZER_PIN = 12
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUZZER_PIN, GPIO.OUT)

pwm = GPIO.PWM(BUZZER_PIN, 1)
pwm.start(10)

melody = [392, 392, 440, 440, 392, 392, 330, 330, 392, 392, 330, 330, 294, 294, 294, 392, 392, 440, 440, 392, 392, 330, 330, 392, 330, 294, 330, 262, 262, 262]

try:
    for i in melody:
        pwm.ChangeFrequency(i)
        time.sleep(0.5)        
finally:
    pwm.stop() 
    GPIO.cleanup()
    print('cleanup and exit')