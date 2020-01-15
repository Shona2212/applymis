import pandas as pd
from date_picker import date_req
from job_dump import publish_dump
from tod_apply import apply_table

def consolidator():
	date = date_req()
	
	apply_f = apply_table()

	pub_dump = publish_dump()


	#filtering on the basis of Applies

	act_apply = apply_f[apply_f.FlowName == '107_applyTypeCountTracing']

	act_apply = act_apply[['CompanyId','JobId','Count']]

	act_apply.columns = ['compId','jobId','Applies']


	pub_dump = pub_dump[['compId','jobId','seamless']]

	consol_f = pub_dump.merge(act_apply, on='jobId', how='left')

	

	consol_f = consol_f.drop(['compId_y'], axis = 1)

	#consol_f.to_csv("Frame_Sample.csv", index=False)



	seamless_yes = consol_f[consol_f.seamless == 'YES']

	seamless_no = consol_f[consol_f.seamless == 'NO']


	yes_frame = seamless_yes

	no_frame = seamless_no


	yes_frame = yes_frame.drop(['seamless'], axis=1)

	no_frame = no_frame.drop(['seamless'], axis=1)


	yes_frame.columns = ['compId','jobId', 'Applies']

	yes_frame = yes_frame.fillna(0)

	no_frame.columns = ['compId','jobId', 'Applies']

	no_frame = no_frame.fillna(0)




	yes_comp_wise = yes_frame.groupby('compId')['Applies'].agg(['count','sum'])

	#yes_comp_wise = yes_comp_wise.sort_values(by ='Applies', ascending=False)

	#yes_comp_wise = yes_comp_wise.fillna(0)


	
	no_comp_wise = no_frame.groupby('compId')['Applies'].agg(['count','sum'])

	#no_comp_wise = no_comp_wise.sort_values(by ='Applies', ascending=False)
	
	#no_comp_wise = no_comp_wise.fillna(0)


	yes_comp_wise.columns = ['Seamless_Jobs','Seamless_Applies']

	no_comp_wise.columns = ['Redirection_Jobs','Redirection_Applies']


	#yes_comp_wise = yes_comp_wise.set_index('compId')

	#no_comp_wise = no_comp_wise.set_index('compId')

	final_frame = pd.concat([yes_comp_wise, no_comp_wise], axis=1)

	final_frame = final_frame.fillna(0)

	final_frame.to_csv(date+"-NI.csv")


if __name__ == '__main__':
    consolidator()


	

		

		
