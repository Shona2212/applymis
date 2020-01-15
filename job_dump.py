#daily_jobs_accumulator_from_source

import pandas as pd

from date_picker import date_req

def publish_dump():

	temp_frame = []

	date = date_req()
	data_daily = pd.read_csv("http://192.168.2.123/dump/publishedWebJobs.csv.zip")
	

	frame_required = data_daily[['jobCompanyId','jobFile','crawlerType','jobAddDate','jobSitePostedDate','jobRefreshDate','Seamless Apply']]

	frame_required.columns = ['compId','jobId','crawlerType','addedDate','sitePostedDate','refreshDate','seamless']

	frame_required.to_csv("Publish_Dump_"+date+".csv", index=False)

	return frame_required

if __name__ == '__main__':
    publish_dump()
