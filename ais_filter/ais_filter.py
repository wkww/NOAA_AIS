import os
import pandas as pd

#navigating to folder location. You may have to change this.

base_dir = os.path.abspath(os.path.dirname( __file__ ))
for file in os.listdir(base_dir):
	if file.endswith(".csv"):
		df = pd.read_csv(file, sep = ",")	

		# Choose the column you want to filter by or create your own filtering conditions
		# e.g result = df[df["VesselName"] == 'POLE']
		# 1001(numeric type) finds all fishing vessels. 
		result = df[df["VesselType"] == '1001']
		print (result)
		result.to_csv('result.csv')