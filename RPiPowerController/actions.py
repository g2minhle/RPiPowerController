from django.shortcuts import render
import RPi.GPIO as GPIO
import logging

LOGGER = logging.getLogger(__name__)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT)

def turnOff(request):
    LOGGER.info("requested to turnOff")
    try:
        GPIO.output(7, True)
    except Exception, e:
        LOGGER.error(e.message)
    return render(request, 'turnOff.html', {})

def turnOn(request):
    LOGGER.info("requested to turnOn")
    try:
        GPIO.output(7, False)
    except Exception, e:
        LOGGER.error(e.message)
    return render(request, 'turnOn.html', {})