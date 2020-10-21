

class BackendServer:

	def __init__(self):
		self.sep = "&"

	def _parse_qs(self, query):
		out = {}
		options = query.split(self.sep)
		for option in options:
			data = option.split("=")
			if len(data) >= 2:
				key, val = data[0], data[1]
				out[key] = val
		return out

	def process(self, environ, start_response):
		d = self._parse_qs(environ['QUERY_STRING'])
		s = ""
		for key in d.keys():
			if len(s):
				s += "\n"
			s += key + "=" + d[key] 
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


