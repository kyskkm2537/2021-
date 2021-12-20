import RPi.GPIO as GPIO
import time
import picamera

path ='/home/pi/src3/08_tngod'

camera = picamera.PiCamera()
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#세븐세그먼트 설정
SEGMENT_PINS = [5,6,13,19,26,16,20]
for segment in SEGMENT_PINS:
    GPIO.setup(segment, GPIO.OUT)
    GPIO.output(segment, GPIO.LOW)

data = [[1, 1, 1, 1, 1, 1, 0],  # 0
        [0, 1, 1, 0, 0, 0, 0],  # 1
        [1, 1, 0, 1, 1, 0, 1],  # 2
        [1, 1, 1, 1, 0, 0, 1],  # 3
        [0, 1, 1, 0, 0, 1, 1],  # 4
        [1, 0, 1, 1, 0, 1, 1],  # 5
        [1, 0, 1, 1, 1, 1, 1],  # 6
        [1, 1, 1, 0, 0, 0, 0],  # 7
        [1, 1, 1, 1, 1, 1, 1],  # 8
        [1, 1, 1, 0, 0, 1, 1]]  # 9

#핀설정
SWITCH_PIN_wakeup = 23
SWITCH_PIN_sleep = 24
SWITCH_PIN_camera = 17
SWITCH_PIN_battery = 21
BUZZER_PIN = 4


#버튼설정
GPIO.setup(SWITCH_PIN_wakeup, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(SWITCH_PIN_sleep, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(SWITCH_PIN_camera, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(SWITCH_PIN_battery, GPIO.IN, pull_up_down = GPIO.PUD_UP)


GPIO.setup(BUZZER_PIN, GPIO.OUT)
pwm = GPIO.PWM(BUZZER_PIN, 1)


melody_sleep = [262, 523, 492, 392, 440, 494, 523, 262, 440, 392, 262,349, 330, 262, 294, 330, 349, 294, 294, 330, 262] #sleep 멜로디
melody_wakeup = [440, 523, 698, 659, 698, 440, 659, 698, 440, 587, 698, 440, 554, 440, 494, 523, 554, 587, 523, 494, 440, 392] #wakeup 멜로디

bt = 9 #현재 배터리

try:
    
           
    while True:
        #버튼입력
        val_sleep = GPIO.input(SWITCH_PIN_sleep)
        val_wakeup = GPIO.input(SWITCH_PIN_wakeup)
        val_battery = GPIO.input(SWITCH_PIN_battery)
        val_camera = GPIO.input(SWITCH_PIN_camera)

        if bt<1 : #배터리가 다 닳으면 끝남
            break   

        for i in range(7): #현재 배터리 출력
            GPIO.output(SEGMENT_PINS[i], data[bt][i])
        
        if val_camera == 0: #카메라
            bt-=1 #배터리 1 소모
            camera.resolution = (640,480)
            camera.start_preview()
            time.sleep(3)
            camera.capture('%s/photo.jpg'%path)
            

        if val_sleep == 0: #sleep 멜로디 출력
            bt-=1
            pwm.start(10)
            for i in melody_sleep:
                pwm.ChangeFrequency(i)
                time.sleep(0.5)  
            pwm.stop()
            
        elif val_wakeup == 0: #wakeup 멜로디 출력
            bt-=1
            pwm.start(10)
            for i in melody_wakeup:
                pwm.ChangeFrequency(i)
                time.sleep(0.5)  
            pwm.stop()
            
        
#끝
finally:
    pwm.stop() 
    camera.stop_preview()
    GPIO.cleanup()
    print('cleanup and exit')