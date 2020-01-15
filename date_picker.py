import datetime

def date_req():

	today=datetime.datetime.now()
	e = today.strftime("%d")
	f = int(e)-1
	if (f == 0):
		d = raw_input("Please enter previous Month Last Date in YYYY-MM-DD format\n(eg, for September 30, 2019, 'input 2019-09-30')\n")
	elif (f < 10):
		d = today.strftime("%Y-%m-")+"0"+str(f)
	else:
		d = today.strftime("%Y-%m-")+str(f)

	date = d

	return date


if __name__=='__main__':
	date_req()
