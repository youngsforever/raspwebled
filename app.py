#!D:\UP\Python python
# -*- encoding: utf-8 -*-
"""
@File    : app.py.py
@Time    : 2020/11/3 15:24
@Author  : young
@Email   : youngsforever@sina.com
@Remark  : 
"""
from flask import Flask,render_template
import RPi.GPIO as GPIO
import time

class Led():
    def __init__(self):
        self.led_pin = 4
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(self.led_pin,GPIO.OUT)
        GPIO.output(self.led_pin,GPIO.LOW)

    def on(self):
        GPIO.output(self.led_pin,GPIO.HIGH)
        print('LED-ON')

    def off(self):
        GPIO.output(self.led_pin,GPIO.LOW)
        print('LED-OFF')

led = Led()
led.off()


app = Flask(__name__)
@app.route("/")
def main():
    return render_template("main.html")

@app.route("/on")
def on():
    led.on()
    return render_template("main.html")

@app.route("/off")
def off():
    led.off()
    return render_template("main.html")

@app.route("/shining")
def shining():
    i=0
    while i < 5:
        led.on()
        time.sleep(.5)
        led.off()
        time.sleep(.5)
        i=i+1;
    return render_template("main.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0')