# 各種ライブラリ導入
import subprocess
import RPi.GPIO as GPIO
import time
import os

# LEDピン設定
led = 4

# IPアドレス定義
ip = 'http://10.3.100.116:8000/led'

#GPIO各種設定
GPIO.setmode(GPIO.BCM)
GPIO.setup(led, GPIO.OUT)

# While無限回し

try:
    while True:
        # prog = subprocess.Popen("curl -X GET %s" % (ip), shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        cmd = "curl -X GET %s" % (ip)
        line = str(os.system(cmd))
        line = line.replace('\n', '')
        line = line.replace('0', '')
        time.sleep(0.1)

        if line == ('led=True'):
            GPIO.output(led, GPIO.HIGH)
            print(line)
            # GPIO.output(led_2, GPIO.LOW)
        elif line == ('led=False'):
            GPIO.output(led, GPIO.LOW)
            print(line)
            # GPIO.output(led_2, GPIO.HIGH)



except KeyboardInterrupt:
    # GPIOの終了処理
    GPIO.cleanup()
    # 終わったというログ出し(改行しないと読みにくい)
    print('\n' + "Over SW test")
