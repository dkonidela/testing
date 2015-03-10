from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer

class webserverHandler(BaseHTTPRequestHandler):
	def do_GET(self):
		try:
			if self.path.endswith("/hello"):
				self.send_response(200)
				self.send_header('Content-type','text/html')
				self.end_headers()

				output=""
				output +="<html><body>Hello, Dileep Konidela</body></html>"
				self.wfile.write(output)
				print output
				return
			if self.path.endswith("/halo"):
				self.send_response(200)
				self.send_header('Content-type','text/html')
				self.end_headers()

				output=""
				output +="<html><body>Hello, Dileep Konidela <a href='/hello>Back to Hello</a></body></html>'"
				self.wfile.write(output)
				print output
				return
		except IOError:
			print "Exception occured"
			self.send_error(404,"File not found %s" %self.path)

def main():

	try:
		port=8080
		server=HTTPServer(('',port),webserverHandler)
		print "Web server unning at the port %s" %port
		server.serve_forever()

	except KeyboardInterrupt:
		print "Shutting down the server"
		server.socket.close()



if __name__=='__main__':
	main()