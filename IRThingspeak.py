import thingspeak
import RPi.GPIO as GPIO
from time import sleep

channel_id=1505477
write_key="YP506T9Z7STPIZWU"

ir=8
#count=0
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(ir, GPIO.IN)

				
if __name__=="__main__":
	count=0
	#print("inside main")
	channel = thingspeak.Channel(id = channel_id , api_key = write_key)
	while True:
		sensorValue=GPIO.input(ir)
		print(sensorValue)
		if sensorValue:
			print("nobody is passing by:")
			count=count
		else:
			print("counter incresed")
			count+=1
		print("count")
		channel.update({'field3':count})
		
		sleep(1)
