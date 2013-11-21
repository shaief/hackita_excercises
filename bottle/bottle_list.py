#encoding: utf-8
from bottle import route, run, template, get, post, request, redirect
import string

@get('/list/')
def list_form():
 
	return """
	<form method="post">
	<textarea name=user_list></textarea>
	<br>
	<input type="checkbox" name="orderedlist" value="yes">Should it be ordered?<br>
	<input type=submit value="Yalla">
	</form>
	"""
 
@post('/list/')
def handle_list():
	split_list = request.forms.user_list
	l = split_list.splitlines()
	print type(l)
	li_list = ""
	for line1 in l:
		line = str(line1)
		li_list += "<li>"+ line + "</li>"
	li_list = str(li_list)
	if request.forms.orderedlist == "yes":
		return """
			<h4>Here is your ordered list:</h4>
			<ol>
			%s
			</ol>
		""" % li_list
	return """
		<h4>Here is your unordered list:</h4>
		<ul>
		%s
		</ul>
		""" % li_list

run(host='localhost', port=8080, debug = True, reloader=True)