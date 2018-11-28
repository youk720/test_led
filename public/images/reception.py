# 各種ライブラリ導入
import subprocess
import RPi.GPIO as GPIO
import time
import os
import sys

# LEDピン設定
led = 17
led_2 = 27

#GPIO各種設定
GPIO.setmode(GPIO.BCM)
GPIO.setup(led, GPIO.OUT)
GPIO.setup(led_2, GPIO.OUT)

# LED初期発光防止用
GPIO.output(led, GPIO.LOW)
GPIO.output(led_2, GPIO.LOW)

# IPアドレス定義
ip = 'http://10.3.100.116:8000/led'
# コマンド定義
cmd = "curl -X GET %s" % (ip)

try:
    # While無限回し
    while True:
        # 上記で定義したコマンドをsubprocessで実行(コマンドラインで動かすのと同一のやり方)
        prog = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
       # result =  str(sys.stdout.buffer.write(prog.stdout))

        # 標準出力を文字列扱いでresultへ代入
        result =  str(prog.stdout)
        # resultのデバック用出力
        # print('\n' + "result: " + result)

        # LED発光のためのif文
        # if (A) in B:のような書き方で,Bの中にAが含まれているかを判定し,Trueの場合if文以下のコードを実行
        if 'led=True' in result:
            GPIO.output(led, GPIO.HIGH)

            # if文入っているかのデバック用
            # print("\n" + "hoge_1")
        # LED発光のためのif文
        elif 'led=False' in result:
            GPIO.output(led, GPIO.LOW)

            # if文入っているかのデバック用
            # print("\n" + "hoge_2")

        # 特に書くこともないので通過
        else:
            pass

# Curl + Cで終了させた時の処理
except KeyboardInterrupt:
    # GPIOの終了処理
    GPIO.cleanup()
    # 終わったというログ出し(改行しないと読みにくい)
    print('\n' + "Over SW test")
