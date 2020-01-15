from date_picker import date_req
from data_extractor import fetch_data
from sheet_maker import data_to_work
from number_extractor import bifurcated_data
from mail_data import mailer
from deframing_data import consolidator


def number_tracker():

	"""
	@author : Ankit Mukherjee
	"""
	consolidator()
	
	data_to_work()

	mailer()


if __name__=='__main__':
	number_tracker()
