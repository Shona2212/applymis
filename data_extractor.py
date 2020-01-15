import pandas as pd
from date_picker import date_req


def fetch_data():

	date = date_req()

	data_frame = pd.read_csv(date+"-NI.csv")

	data_frame = data_frame[['compId','Redirection_Jobs','Redirection_Applies','Seamless_Jobs','Seamless_Applies']]

	data_frame = data_frame.sort_values(by ='Seamless_Applies' , ascending=False)


	return data_frame

if __name__=='__main__':
	fetch_data()
