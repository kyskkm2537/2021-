from flask import Flask, render_template
import RPi.GPIO as GPIO

LED_PIN_RED = 22
LED_PIN_BLUE = 16
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN_RED, GPIO.OUT)
GPIO.setup(LED_PIN_BLUE, GPIO.OUT)
#Flask 객체 생성
app = Flask(__name__)

#0.0.0.0:5000
@app.route("/")
def hello():
    return render_template("led.html")

@app.route("/led/<op>/<color>")
def led_op(op,color):
    if op == "on":
        if color == "Red":
            GPIO.output(LED_PIN_RED, GPIO.HIGH)
            return "BLUE LED ON"
        if color == "Blue":
            GPIO.output(LED_PIN_BLUE, GPIO.HIGH)
            return "GREEN LED ON"
    elif op == "off":
        if color == "Red":
            GPIO.output(LED_PIN_RED, GPIO.LOW)
            return "BLUE LED OFF"
        if color == "Blue":
            GPIO.output(LED_PIN_BLUE, GPIO.LOW)
            return "GREEN LED OFF"

#터미널에서 직접 실행시킨 경우
if __name__ == "__main__":
    try:
        app.run(host="0.0.0.0")
    finally:
        GPIO.cleanup()