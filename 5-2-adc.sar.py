import RPi.GPIO as GPIO
import time 
dac=[8, 11, 7, 1, 0, 5, 12, 6]
comp=14
troyka=13
GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(troyka, GPIO.OUT, initial=GPIO.HIGH)         
GPIO.setup(comp, GPIO.IN)
def b(x):
    return [int(i) for i in bin(x)[2:].zfill(8)]
def adc():
    a = [0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(8):
        a[i]=1
        GPIO.output(dac, a)
        time.sleep(0.002)
        compValue=GPIO.input(comp)
        if compValue==0:
            a[i]=0
    return (128*a[0]+64*a[1]+32*a[2]+16*a[3]+8*a[4]+4*a[5]+2*a[6]+a[7])
try:
    while True:
        signal = adc()
        voltage = signal/256*3.3
        print("ADC value = {:^3}, input voltage = {:.2f}".format(signal, voltage))
finally:
    GPIO.output(dac, GPIO.LOW)
    GPIO.cleanup(dac)
