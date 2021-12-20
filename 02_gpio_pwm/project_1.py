import RPi.GPIO as GPIO
import time
import random

LED_PIN = 11
SWITCH_PIN = 9
BUZZER_PIN = 10
SEGMENT_PINS = [13, 14, 15, 16, 17, 18, 21]

GPIO.setmode(GPIO.BCM)

GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.setup(BUZZER_PIN, GPIO.OUT)
GPIO.setup(SWITCH_PIN, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

for segment in SEGMENT_PINS:
  GPIO.setup(segment, GPIO.OUT)
  GPIO.output(segment, GPIO.LOW)

data = [[1, 1, 1, 1, 1, 1, 0], 
        [0, 1, 1, 0, 0, 0, 0], 
        [1, 1, 0, 1, 1, 0, 1], 
        [1, 1, 1, 1, 0, 0, 1], 
        [0, 1, 1, 0, 0, 1, 1],
        [1, 0, 1, 1, 0, 1, 1],
        [1, 0, 1, 1, 1, 1, 1], 
        [1, 1, 1, 0, 0, 0, 0], 
        [1, 1, 1, 1, 1, 1, 1], 
        [1, 1, 1, 0, 0, 1, 1]]




pwm = GPIO.PWM(BUZZER_PIN, 1)
pwm.start(10)

R = random.randrange(1, 6)
time.sleep(R)
start_Time = time.time()

GPIO.output(LED_PIN, True)
pwm.ChangeFrequency(330)



while True:
  if GPIO.input(SWITCH_PIN)==True:
    
    end_Time = time.time()
    pwm.stop()
    print(end_Time-start_Time)
    GPIO.output(LED_PIN, False)
    tmp=end_Time-start_Time
    if tmp<=0.1:
      for i in range(7):
       GPIO.output(SEGMENT_PINS[i], data[1][i])
    elif tmp<=0.2:
      for i in range(7):
        GPIO.output(SEGMENT_PINS[i], data[2][i])
    elif tmp<=0.4:
      for i in range(7):
        GPIO.output(SEGMENT_PINS[i], data[3][i])
    elif tmp<=0.6:
      for i in range(7):
        GPIO.output(SEGMENT_PINS[i], data[4][i])
    elif tmp<=0.8:
      for i in range(7):
        GPIO.output(SEGMENT_PINS[i], data[5][i])
    elif tmp<=1.0:
      for i in range(7):
       GPIO.output(SEGMENT_PINS[i], data[6][i])
    elif tmp<=1.5:
      for i in range(7):
        GPIO.output(SEGMENT_PINS[i], data[7][i])
    elif tmp<=2.0:
      for i in range(7):
        GPIO.output(SEGMENT_PINS[i], data[8][i])
    else:
      for i in range(7):
        GPIO.output(SEGMENT_PINS[i], data[9][i])
    
    time.sleep(5)
    
    GPIO.cleanup()
    print('cleanup and exit')

    break


  