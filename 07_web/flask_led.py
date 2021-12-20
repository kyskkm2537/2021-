from flask import Flask
import RPi.GPIO as GPIO

RED_LED_PIN = 22
GREEN_LED_PIN  = 27

app = Flask(__name__)

GPIO.setmode(GPIO.BCM)
GPIO.setup(RED_LED_PIN, GPIO.OUT)
GPIO.setup(GREEN_LED_PIN, GPIO.OUT)



@app.route("/")
def hello():
    return '''
    <p>Hello, Flask!</p>
    <a href="/LED/RED/ON/">RED LED ON</a>
    <a href="/LED/RED/OFF/">RED LED OFF</a>
    <a href="/LED/GREEN/ON/">GREEN LED ON</a>
    <a href="/LED/GREEN/OFF/">GREEN LED OFF</a>
    '''

@app.route("/LED/<col>/<op>/")
def led_op(col,op):
    if col == "RED":
        if op == "ON":
            GPIO.output(RED_LED_PIN, GPIO.HIGH)
            return'''
                <p>RED LED ON</p>
                <a href="/">Go home</a>
            '''
        elif op == "OFF":
            GPIO.output(RED_LED_PIN, GPIO.LOW)
            return'''
                <p>RED LEF OFF</p>
                <a href="/">Go home</a>
            '''
    elif col == "GREEN":
        if op == "ON":
            GPIO.output(GREEN_LED_PIN, GPIO.HIGH)
            return'''
                <p>GREEN LED ON</p>
                <a href="/">Go home</a>
            '''
        elif op == "OFF":
            GPIO.output(GREEN_LED_PIN, GPIO.LOW)
            return'''
                <p>GREEN LED OFF</p>
                <a href="/">Go home</a>
            '''

if __name__ == "__main__":
    try:
        app.run(host="0.0.0.0")
    finally:
        GPIO.cleanup()

from flask import Flask
import RPi.GPIO as GPIO

RED_LED_PIN = 22
GREEN_LED_PIN  = 27

app = Flask(__name__)

GPIO.setmode(GPIO.BCM)
GPIO.setup(RED_LED_PIN, GPIO.OUT)
GPIO.setup(GREEN_LED_PIN, GPIO.OUT)



@app.route("/")
def hello():
    return '''
    <p>Hello, Flask!</p>
    <a href="/LED/RED/ON/">RED LED ON</a>
    <a href="/LED/RED/OFF/">RED LED OFF</a>
    <a href="/LED/GREEN/ON/">GREEN LED ON</a>
    <a href="/LED/GREEN/OFF/">GREEN LED OFF</a>
    '''

@app.route("/LED/<col>/<op>/")
def led_op(col,op):
    if col == "RED":
        if op == "ON":
            GPIO.output(RED_LED_PIN, GPIO.HIGH)
            return'''
                <p>RED LED ON</p>
                <a href="/">Go home</a>
            '''
        elif op == "OFF":
            GPIO.output(RED_LED_PIN, GPIO.LOW)
            return'''
                <p>RED LEF OFF</p>
                <a href="/">Go home</a>
            '''
    elif col == "GREEN":
        if op == "ON":
            GPIO.output(GREEN_LED_PIN, GPIO.HIGH)
            return'''
                <p>GREEN LED ON</p>
                <a href="/">Go home</a>
            '''
        elif op == "OFF":
            GPIO.output(GREEN_LED_PIN, GPIO.LOW)
            return'''
                <p>GREEN LED OFF</p>
                <a href="/">Go home</a>
            '''

if __name__ == "__main__":
    try:
        app.run(host="0.0.0.0")
    finally:
        GPIO.cleanup()

