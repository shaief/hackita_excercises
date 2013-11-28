#encoding: utf-8
import pandas as pd
from bottle import route, run, template, get, post, request, redirect
import string

page = "cow.txt"

# open csv file as pandas data frame:
df = pd.read_csv(page,skiprows = 28,sep = ";")
states_short_names = df.ISO3166A2.values[:]
states_full_names = df.ISOen_name.values[:]
df['html_text'] = "<option value="+df.ISO3166A2+">"+df.ISOen_name+"</option>"
states_html_text = "".join(str(df.html_text.values.tolist()))

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
 
@post('/')
def handle_list():
	user_country_name = request.forms.countries
	full_name = df[df.ISO3166A2 == user_country_name].ISOen_name.values[0]
	continent = df[df.ISO3166A2 == user_country_name].continent.values[0]
	subcontinent = df[df.ISO3166A2 == user_country_name].subcontinent.values[0]
	population = df[df.ISO3166A2 == user_country_name].population.values[0]
	lon = df[df.ISO3166A2 == user_country_name].longitude.values[0]
	lat = df[df.ISO3166A2 == user_country_name].latitude.values[0]
	gov = df[df.ISO3166A2 == user_country_name].url_gov.values[0]
	gis = df[df.ISO3166A2 == user_country_name].url_gis.values[0]
	print user_country_name
	return '''
		<title>Data for {}</title>
		<h4>Requested data for: {} </h4>
		Short name: {}</br>
		Continent: {}</br>
		Sub continent: {}</br>
		Population: {} people</br>
		Lon/Lat: {:0.3f}/{:0.3f}</br>
		Governmental url: <a href="{}">{}</a></br>
		GIS url: <a href="{}">{}</a>
		'''.format(full_name, full_name, user_country_name, continent, subcontinent, population, lon, lat, gov, gov, gis, gis)

run(host='localhost', port=8080, debug = True, reloader=True)