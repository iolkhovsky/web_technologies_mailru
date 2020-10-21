

class BackendServer:

	def __init__(self):
		self.sep = "&"

	def _parse_qs(self, query):
		return query.split(self.sep)

	def process(self, environ, start_response):
		options = self._parse_qs(environ['QUERY_STRING'])
		s = ""
		for option in options:
			s += option + "\n"
		data = s.encode("utf-8")
		status = '200 OK'
		response_headers = [
			('Content-type', 'text/plain'),
			('Content-Length', str(len(data)))
		]
		start_response(status, response_headers)
		return iter([data])

	def __call__(self, *args, **kwargs):
		return self.process(*args)


def make_server():
	return BackendServer()


