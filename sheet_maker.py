import datetime
import pandas as pd
import unicodecsv as csv
import numpy
import operator
from os import listdir
import os
from pandas import merge
import itertools
import time
from date_picker import date_req
from data_extractor import fetch_data

def data_to_work():

	date = date_req()

	file_handler=open(date+"_final_data.csv", "wb")
	writer_obj=csv.writer(file_handler)
	writer_obj.writerow(['Company_Id','Seamless_Jobs','Redirected_Jobs','Total_Jobs','Seamless_Applies','Redirected_Applies','Total_Applies'])


	working_data = fetch_data()

	temp = []

	for row, index in working_data.iterrows():
		compId = index['compId']
		red_jobs = index['Redirection_Jobs']
		seam_jobs = index['Seamless_Jobs']
		red_applies = index['Redirection_Applies']
		seam_applies = index['Seamless_Applies']

		temp.append(compId)
		temp.append(seam_jobs)
		temp.append(red_jobs)
		temp.append(seam_applies)
		temp.append(red_applies)


	pool = temp

	temp = []


	cid_temp = []
	for m in pool[::5]:
		cid_temp.append(m)

	sj_temp = []
	for n in pool[1::5]:
		sj_temp.append(n)


	rj_temp = []
	for o in pool[2::5]:
		rj_temp.append(o)

	sa_temp = []
	for p in pool[3::5]:
		sa_temp.append(p)


	ra_temp = []
	for q in pool[4::5]:
		ra_temp.append(q)


	tjobs = []
	tapplies = []
	fsheet = []
	for each, item in enumerate(cid_temp):

		tjobs.append(sj_temp[each])
		tjobs.append(rj_temp[each])
		tapplies.append(sa_temp[each])
		tapplies.append(ra_temp[each])


		fsheet.append(item)
		fsheet.append(sj_temp[each])
		fsheet.append(rj_temp[each])
		fsheet.append(sum(tjobs))
		fsheet.append(sa_temp[each])
		fsheet.append(ra_temp[each])
		fsheet.append(sum(tapplies))

		tjobs = []
		tapplies = []


		writer_obj.writerow(fsheet)

		fsheet = []

if __name__=='__main__':
	data_to_work()
