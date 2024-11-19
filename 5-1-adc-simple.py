import RPi.GPIO as GPIO
import time 
dac=[26, 19, 13, 6, 5, 11, 9, 10]
comp=4
troyka=17
GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(troyka, GPIO.OUT, initial=GPIO.HIGH)         
GPIO.setup(comp, GPIO.IN)
def b(x):
    return [int(i) for i in bin(x)[2:].zfill(8)]
def adc(U):
    signal=b(U)
    GPIO.output(dac, signal)
    return signal
try:
    while True:
        for U in range(256):
            signal = adc(U)
            time.sleep(0.0009)
            voltage = U/256*3.3
            compValue=GPIO.input(comp)
            if compValue==0:
                print("ADC value = {:^3} -> {}, input voltage = {:.2f}".format(U, signal, voltage))
                break
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()

