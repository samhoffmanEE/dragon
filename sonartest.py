import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

TRIG_FRONT = 23 
ECHO_FRONT = 24

TRIG_LEFT = 25
ECHO_LEFT = 8


print "Distance Measurment In Progress"

GPIO.setup(TRIG_FRONT,GPIO.OUT)
GPIO.setup(ECHO_FRONT,GPIO.IN)

GPIO.setup(TRIG_LEFT,GPIO.OUT)
GPIO.setup(ECHO_LEFT,GPIO.IN)

GPIO.output(TRIG_FRONT, False)
GPIO.output(TRIG_LEFT, False)
print "Waiting for sensor to settle"

##time.sleep(1)
timer = time.time()
end = timer + 10
while timer < end:
        time.sleep(1)
        GPIO.output(TRIG_FRONT, True)
        time.sleep(0.00001)
        GPIO.output(TRIG_FRONT, False)

        while GPIO.input(ECHO_FRONT)==0:
                pulse_start_F = time.time()

        while GPIO.input(ECHO_FRONT)==1:
                pulse_end_F = time.time()

        GPIO.output(TRIG_LEFT, True)
        time.sleep(0.00001)
        GPIO.output(TRIG_LEFT, False)


        while GPIO.input(ECHO_LEFT)==0:
                pulse_start_L = time.time()

        while GPIO.input(ECHO_LEFT)==1:
                pulse_end_L = time.time()

        pulse_duration_F = pulse_end_F - pulse_start_F
        pulse_duration_L = pulse_end_L - pulse_start_L

        distance_F = pulse_duration_F * 17150
        distance_L = pulse_duration_L * 17150

        distance_F = round(distance_F,2)
        distance_L = round(distance_L,2)

       ## print "Distance Front:", distance_F, "cm\tDistance Left:", distance_L, "cm"
	if distance_F < 95.0 and distance_L < 95.0:
		print "F L"
	elif distance_L < 95.0:
		print "L"
	elif distance_F < 95.0:
		print "F"
        timer = time.time()

# second time


GPIO.cleanup()

