#encoding: utf-8
from bottle import route, run, template, get, post, request, redirect
import string

@get('/list/')
def list_form():
 
	return """
	<form method="post">
	Enter a number:
	<input name="multi_num"><br>
	<input type=submit value="Yalla">
	</form>
	"""
 
@post('/list/')
def handle_list():
	user_request = request.forms.multi_num
	n = int(user_request)
	multi = ""
	for i in range(1,n+1):
		multi+=("<tr>")
		for j in range(1,n+1):
			m = i*j
			multi+=("<td>%d</td>" % m)
		multi+=("</tr>")
	final = '<table>'+multi+'</table>'
	return final

run(host='localhost', port=8080, debug = True, reloader=True)