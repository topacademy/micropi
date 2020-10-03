import pigpio
import time

p1 = pigpio.pi() #use defaults

p1.set_mode(16, pigpio.OUTPUT)

for i in range(5):
	p1.set_PWM_frequency(16,2000)
	p1.set_PWM_dutycycle(16,128)
	time.sleep(0.3)
#	p1.set_PWM_dutycycle(16,0)
	p1.set_PWM_frequency(16,1000)
	p1.set_PWM_dutycycle(16,128)
	time.sleep(0.3)
#	p1.set_PWM_dutycycle(16,0)

p1.set_PWM_dutycycle(16,0)
p1.stop()

