import RPi.GPIO as GPIO

LED_PIN_GREEN = 5
LED_PIN_RED = 6
LED_PIN_YELLOW = 4

SWITCH_PIN_GREEN = 15
SWITCH_PIN_RED = 16
SWITCH_PIN_YELLOW = 14


GPIO.setmode(GPIO.BCM)

GPIO.setup(LED_PIN_GREEN, GPIO.OUT)
GPIO.setup(LED_PIN_RED, GPIO.OUT)
GPIO.setup(LED_PIN_YELLOW, GPIO.OUT)

GPIO.setup(SWITCH_PIN_GREEN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(SWITCH_PIN_RED, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(SWITCH_PIN_YELLOW, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

try:
  while True:
    val_g = GPIO.input(SWITCH_PIN_GREEN)
    val_r = GPIO.input(SWITCH_PIN_RED)
    val_y = GPIO.input(SWITCH_PIN_YELLOW)

    GPIO.output(LED_PIN_GREEN,val_g)
    GPIO.output(LED_PIN_RED,val_r)
    GPIO.output(LED_PIN_YELLOW,val_y)

finally:
  GPIO.cleanup()
  print('cleanup and exit')