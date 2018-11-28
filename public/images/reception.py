# 各種ライブラリ導入
import subprocess
import RPi.GPIO as GPIO
import time

# LEDピン設定
led = 27
led_2 = 17

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

        if 'led_1=True' in result and 'led_2=True' in result:
            GPIO.output(led, GPIO.HIGH)
            GPIO.output(led_2, GPIO.HIGH)
            # if文入っているかのデバック用
            print("\n" + "hoge_3")
        # LED発光のためのif文
        # if (A) in B:のような書き方で,Bの中にAが含まれているかを判定し,Trueの場合,if文以下インデントのコードを実行
        elif 'led_1=True' in result:
            GPIO.output(led, GPIO.HIGH)
            GPIO.output(led_2, GPIO.LOW)
            # if文入っているかのデバック用
            print("\n" + "hoge_1")
        # LED発光のためのif文
        elif 'led_2=True' in result:
            GPIO.output(led, GPIO.LOW)
            GPIO.output(led_2, GPIO.HIGH)

            # if文入っているかのデバック用
            print("\n" + "hoge_2")

        # それ以外の操作で、LEDを切る
        else:
            GPIO.output(led, GPIO.LOW)
            GPIO.output(led_2, GPIO.LOW)
            # if文入っているかのデバック用
            print("\n" + "hoge_4")

# Curl + Cで終了させた時の処理
except KeyboardInterrupt:
    # GPIOの終了処理
    GPIO.cleanup()
    # 終わったというログ出し(改行しないと読みにくい)
    print('\n' + "Over SW test")
