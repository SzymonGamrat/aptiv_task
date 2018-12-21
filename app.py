# -*- coding: utf-8 -*-
from flask import Flask
from flask_socketio import SocketIO

#enable on real rpi:
#import RPi.GPIO as GPIO
#import time

app = Flask(__name__)
socketio = SocketIO(app)

from views import index

from flask_socketio import send, emit

@socketio.on('client_connected')
def handle_client_connect_event(json):
    print('received json: {0}'.format(str(json)))

@socketio.on('enable_led')
def handle_led_enabling(json):

    #GPIO.setmode(GPIO.BCM)
    #GPIO.setwarnings(False) #setup GPIO
    #GPIO.setup(18,GPIO.OUT) #ustawienie trybu pinu
    #GPIO.output(18,GPIO.HIGH)
    #ustawienie stanu wysokiego, czyli wlaczenie LED
    print('LED is enable'.format(json))
    emit ('alert', 'LED enabled')

@socketio.on('disable_led')
def handle_alert_event(json):
    #GPIO.setmode(GPIO.BCM)
    #GPIO.setwarnings(False) #setup GPIO
    #GPIO.setup(18,GPIO.OUT) #ustawienie trybu pinu
    #GPIO.output(18,GPIO.LOW)
    #ustawienie stanu niskiego, czyli wylaczenie LED
    print('LED is disable'.format(json))
    emit('alert', 'LED disable')


@socketio.on('blink')
def blink_button(json):
    #a = 1
    #while a < 2 
    #GPIO.setmode(GPIO.BCM)
    #GPIO.setup(18,GPIO.OUT)
    #GPIO.output(18, GPIO.HIGH)
    #time.sleep(2)
    #GPIO.output(18, GPIO.LOW)

    print('LED is blinking'.format(json))
    emit('LED blinking')

@socketio.on('STOP')
def stop_button(json):
    #a = 2
    print('LED STOP blinking'.format(json))
    emit('STOP blinking')
if __name__ == "__main__":
    socketio.run(app, debug=True)
