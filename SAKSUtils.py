
import time

def bighint(saks, secs, sleepsecs, times):
	try:
		for i in range(times):
			saks.buzzer.on()

			for j in range(0, 8):
				if j == i % 8:
					saks.ledrow.on_for_index(j)
				else:
					saks.ledrow.off_for_index(j)
			
			time.sleep(secs)
			saks.buzzer.off()
			time.sleep(sleepsecs)
	except Exception, e:
		pass
	finally:
		saks.buzzer.off()
		saks.ledrow.off()

