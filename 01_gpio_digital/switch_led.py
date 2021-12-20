import RPi.GPIO as GPIO

LED_PIN = 3

SWITCH_PIN = 4

GPIO.setmode(GPIO.BCM)
GPIO.setup(SWITCH_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP
)

GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.setup(SWITCH_PIN, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)#s내부 풀다운 저항

try:
  while True:
    val = GPIO.input(SWITCH_PIN)
    print(val)
    GPIO.output(LED_PIN,val)
finally:
  GPIO.cleanup()
  print('cleanup and exit')