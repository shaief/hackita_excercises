#encoding: utf-8
import pandas as pd
from bottle import route, run, template, get, post, request, redirect
import string

page = "cow.txt"

def closest_dist_from_state(data_csv, state_abv):
	state_lat = data_csv[data_csv.ISO3166A2==state_abv].latitude.values[0]
	state_lon = data_csv[data_csv.ISO3166A2==state_abv].longitude.values[0]
	data_csv['dist_from'] = ((data_csv.latitude-state_lat)**2+(data_csv.longitude-state_lon)**2)**0.5
	return data_csv[data_csv.index == data_csv.dist_from.argsort()[1]].ISOen_name.values[0]


# open csv file as pandas data frame:
df = pd.read_csv(page,skiprows = 28,sep = ";")
#Arrange pandas data frame as lists
states_short_names = df.ISO3166A2.values[:]
states_full_names = df.ISOen_name.values[:]
# Create an html series in pandas data frame
df['html_text'] = "<option value="+df.ISO3166A2+">"+df.ISOen_name+"</option>"
# Create a long html string from lists
states_html_text = "".join(str(df.html_text.values.tolist()))

@route('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='static')

# Drop down menu of countries names
@get('/')
def list_form():
	return """
	<h4>Please choose a country you would like to get some information about:</h4>
	<form method="post">
	<select name="countries">
	%s
	</select>
	<input type=submit value="Yalla">
	</form>
	""" % states_html_text

# Show user request as html page
@post('/')
def handle_list():
	user_country_name = request.forms.countries
	full_name = df[df.ISO3166A2 == user_country_name].ISOen_name.values[0]
	continent = df[df.ISO3166A2 == user_country_name].continent.values[0]
	subcontinent = df[df.ISO3166A2 == user_country_name].subcontinent.values[0]
	capital = df[df.ISO3166A2 == user_country_name].UNen_capital.values[0]
	population = df[df.ISO3166A2 == user_country_name].population.values[0]
	lon = df[df.ISO3166A2 == user_country_name].longitude.values[0]
	lat = df[df.ISO3166A2 == user_country_name].latitude.values[0]
	gov = df[df.ISO3166A2 == user_country_name].url_gov.values[0]
	gis = df[df.ISO3166A2 == user_country_name].url_gis.values[0]
	post = df[df.ISO3166A2 == user_country_name].url_post.values[0]
	stats = df[df.ISO3166A2 == user_country_name].url_stats.values[0]
	closest = closest_dist_from_state(df,user_country_name)
	print user_country_name
	return '''
		<title>Data for {}</title>
		<h4>Requested data for: {} </h4>
		Short name: {}</br>
		Continent: {}</br>
		Sub continent: {}</br>
		Capital: {}</br>
		Population: {:0,d} people</br>
		Lon/Lat: {:0.3f}/{:0.3f}</br>
		Closest state: {}</br>
		Governmental url: <a href="{}">{}</a></br>
		GIS url: <a href="{}">{}</a></br>
		Post agency url: <a href="{}">{}</a></br>
		Statistics bureau url: <a href="{}">{}</a></br>
		<img src="http://flagpedia.net/data/flags/normal/{}.png" height="200"></br>
		<a href="http://localhost:8080">Choose different country</a>
		'''.format(full_name, full_name, user_country_name, continent, subcontinent, capital, population, lon, lat, closest, gov, gov, gis, gis, post, post, stats, stats, user_country_name.lower())

run(host='localhost', port=8080, debug = True, reloader=True)