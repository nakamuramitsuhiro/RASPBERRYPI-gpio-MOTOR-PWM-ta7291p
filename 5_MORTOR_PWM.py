import RPi.GPIO as GPIO
from time import sleep
import curses

PWM = 17
IN1 = 27
IN2 = 22

GPIO.setmode(GPIO.BCM)
GPIO.setup(IN1, GPIO.OUT)
GPIO.setup(IN2, GPIO.OUT)
GPIO.setup(PWM, GPIO.OUT)
pwmout = GPIO.PWM(PWM, 50)


# キーボード入力を受け付ける
key_in = curses.initscr()
curses.noecho()

duty = 0
pwmout.start(duty)

try:
    while True:
        key = key_in.getch()
        if key == ord('a') and duty < 100:
            duty += 10
            print(f'正転加速 duty={duty}\r')
            pwmout.ChangeDutyCycle(duty)
            GPIO.output(IN1, GPIO.HIGH)
            GPIO.output(IN2, GPIO.LOW)
            sleep(1)
 
        elif key == ord('z') and 0 < duty:
            duty -= 10
            print(f'正転減速 duty={duty}\r')
            pwmout.ChangeDutyCycle(duty)
            GPIO.output(IN1, GPIO.HIGH)
            GPIO.output(IN2, GPIO.LOW)
            sleep(1)
            
        elif key == ord('s') and duty < 100:
            duty += 10
            print(f'逆転加速 duty={duty}\r')
            pwmout.ChangeDutyCycle(duty)
            GPIO.output(IN1, GPIO.LOW)
            GPIO.output(IN2, GPIO.HIGH)
            sleep(1)
            
        elif key == ord('x') and 0 < duty:
            duty -= 10
            print(f'逆転減速 duty={duty}\r')
            pwmout.ChangeDutyCycle(duty)
            GPIO.output(IN1, GPIO.LOW)
            GPIO.output(IN2, GPIO.HIGH)
            sleep(1)
            
        elif key == ord('c') :
            duty = 0
            print(f'ストップ duty={duty}\r')
            pwmout.ChangeDutyCycle(duty)
            GPIO.output(IN1, GPIO.HIGH)
            GPIO.output(IN2, GPIO.HIGH)
            sleep(1)
           
finally:
    # 終了処理
    pwmout.stop()
    GPIO.cleanup()
    curses.echo()
    curses.endwin()
