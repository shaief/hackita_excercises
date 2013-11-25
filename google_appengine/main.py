#from server.lib.bottle import route, run, default_app, error
from bottle import route, run, default_app, error, get, post, request


@route('/')
def hello():
    return "Hello from bottle! :-)"

#application = default_app()

@error(404)
def error_404(error):
    """Return a custom 404 error."""
    return 'Sorry, Nothing at this URL.'
    
@get('/list')
def list_form():
 
	return """
	<form method="post">
	<textarea name=user_list></textarea>
	<br>
	<input type="checkbox" name="orderedlist" value="yes">Should it be ordered?<br>
	<input type=submit value="Yalla">
	</form>
	"""
 
@post('/list')
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

@get('/multi')
def list_form():
 
	return """
	<form method="post">
	Enter a number:
	<input name="multi_num"><br>
	<input type=submit value="Yalla">
	</form>
	"""

@post('/multi')
def handle_list():
	user_request = request.forms.multi_num
	n = int(user_request)
	multi = ""
	for i in range(1,n+1):
		multi+=("<tr>")
		for j in range(1,n+1):
			m = i*j
			multi+=("<td align=right>%d</td>" % m)
		multi+=("</tr>")
	final = '<table border="1">'+multi+'</table>'
	return final		

application = default_app()
