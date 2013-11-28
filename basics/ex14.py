import pandas as pd
page = "cow.txt"

def closest_dist_from_state(data_csv, state_abv):
	state_lat = data_csv[data_csv.ISO3166A2==state_abv].latitude.values[0]
	state_lon = data_csv[data_csv.ISO3166A2==state_abv].longitude.values[0]
	data_csv['dist_from'] = ((data_csv.latitude-state_lat)**2+(data_csv.longitude-state_lon)**2)**0.5
	print state_abv + " lon/lat: " + str(state_lon) + " / " + str(state_lat)
	print "The closest state to " + data_csv[data_csv.ISO3166A2==state_abv].ISOen_name.values[0] + " is " + data_csv[data_csv.index == data_csv.dist_from.argsort()[1]].ISOen_name.values[0]

# open csv file as pandas data frame:
df = pd.read_csv(page,skiprows = 28,sep = ";")
# run closest distance from state function
closest_dist_from_state(df,"IL")