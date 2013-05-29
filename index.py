
def application(environ, start_response):
	 
	#	output = '<html><head><link style="text/css" rel="stylesheet" href="css/bootstrap.css"></head><body><h2>Hello</h2></body></html>'
	output = environ['PATH_INFO']

	headers = [('Content-type', 'text/html')]
	start_response('200 OK', headers)
	return [output]

