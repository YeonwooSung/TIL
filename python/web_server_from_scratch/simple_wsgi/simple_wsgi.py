import datetime
import io
import socket
import sys


class WSGIServer(object):
    '''
    A simple WSGI server that implements the application callable.

    It is not recommended to use this server in production.
    Please use uvicorn, gunicorn, or other production-ready WSGI servers.
    This server is intended to be used for learning purposes only.

    Attributes:
        address_family (int): Address family of the socket.
        socket_type (int): Socket type of the socket.
        request_queue_size (int): Maximum number of queued connections.
        
        listen_socket (socket): Socket object that listens for connections.
        client_connection (socket): Socket object that represents the client connection.
        request_data (str): Request data sent by the client.
        request_method (str): Request method sent by the client.
        path (str): Path sent by the client.
        request_version (str): Request version sent by the client.
        server_name (str): Server name.
        server_port (int): Server port.
        headers_set (list): List of headers to be sent to the client.
    '''

    address_family = socket.AF_INET
    socket_type = socket.SOCK_STREAM
    request_queue_size = 1

    def __init__(self, server_address:tuple) -> None:
        '''
        Initialize the WSGIServer object.

        Args:
            server_address (tuple): Server address.

        Raises:
            AssertionError: If the server_address is not applicable for running the server.
        '''
        assert len(server_address) == 2, 'Server address must be a tuple of length 2.'
        assert isinstance(server_address[0], str), 'The first element of the server address must be a string.'
        assert isinstance(server_address[1], int), 'The second element of the server address must be an integer, which represents the port.'

        # Create a listening socket
        self.listen_socket = listen_socket = socket.socket(
            self.address_family,
            self.socket_type
        )

        # Allow to reuse the same address
        listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        # Bind
        listen_socket.bind(server_address)

        # Activate
        listen_socket.listen(self.request_queue_size)

        # Get server host name and port
        host, port = self.listen_socket.getsockname()[:2]
        self.server_name = socket.getfqdn(host)
        self.server_port = port

        # Return headers set by Web framework/Web application
        self.headers_set = []


    def set_app(self, application):
        self.application = application


    def serve_forever(self):
        listen_socket = self.listen_socket
        while True:
            # New client connection
            self.client_connection, client_address = listen_socket.accept()
            # Handle one request and close the client connection.
            # Then loop over to wait for another client connection
            # This blocks the requests, which makes this wsgi not applicable for the production.
            # To make it production-ready, you should implement some thread-pooling or async I/O runtime for it.
            self.handle_one_request()


    def handle_one_request(self):
        request_data = self.client_connection.recv(1024)
        self.request_data = request_data = request_data.decode('utf-8')
        # Print formatted request data a la 'curl -v'
        print(''.join(
            f'< {line}\n' for line in request_data.splitlines()
        ))

        self.parse_request(request_data)

        # Construct environment dictionary using request data
        env = self.get_environ()

        # It's time to call our application callable and get
        # back a result that will become HTTP response body
        result = self.application(env, self.start_response)

        # Construct a response and send it back to the client
        self.finish_response(result)


    def parse_request(self, text):
        request_line = text.splitlines()[0]
        request_line = request_line.rstrip('\r\n')
        # Break down the request line into components
        (self.request_method,  # GET
         self.path,            # /hello
         self.request_version  # HTTP/1.1
         ) = request_line.split()


    def get_environ(self):
        env = {}

        # The following code snippet does not follow PEP8 conventions,
        # but it's formatted the way it is for demonstration purposes
        # to emphasize the required variables and their values.
        #
        # Required WSGI variables
        env['wsgi.version']      = (1, 0)
        env['wsgi.url_scheme']   = 'http'
        env['wsgi.input']        = io.StringIO(self.request_data)
        env['wsgi.errors']       = sys.stderr
        env['wsgi.multithread']  = False
        env['wsgi.multiprocess'] = False
        env['wsgi.run_once']     = False

        # Required CGI variables
        env['REQUEST_METHOD']    = self.request_method    # GET
        env['PATH_INFO']         = self.path              # /hello
        env['SERVER_NAME']       = self.server_name       # localhost
        env['SERVER_PORT']       = str(self.server_port)  # 8888
        return env

    def start_response(self, status, response_headers, exc_info=None):
        dt = datetime.datetime.now()
        date_str = dt.strftime('%a, %d %b %Y %H:%M:%S GMT')

        # Add necessary server headers
        server_headers = [
            ('Date', date_str),
            ('Server', 'WSGIServer 0.2'),
        ]
        self.headers_set = [status, response_headers + server_headers]
        # To adhere to WSGI specification the start_response must return a 'write' callable.
        # We simplicity's sake we'll ignore that detail for now.
        return self.finish_response


    def finish_response(self, result):
        try:
            status, response_headers = self.headers_set
            response = f'HTTP/1.1 {status}\r\n'
            for header in response_headers:
                response += '{0}: {1}\r\n'.format(*header)
            response += '\r\n'
            for data in result:
                response += data.decode('utf-8')
            # Print formatted response data a la 'curl -v'
            print(''.join(
                f'> {line}\n' for line in response.splitlines()
            ))
            response_bytes = response.encode()
            self.client_connection.sendall(response_bytes)
        finally:
            self.client_connection.close()


SERVER_ADDRESS = (HOST, PORT) = '', 8888


def make_server(server_address, application):
    server = WSGIServer(server_address)
    server.set_app(application)
    return server


if __name__ == '__main__':
    if len(sys.argv) < 2:
        sys.exit('Provide a WSGI application object as module:callable')
    app_path = sys.argv[1]
    module, application = app_path.split(':')
    module = __import__(module)
    application = getattr(module, application)
    httpd = make_server(SERVER_ADDRESS, application)
    print(f'WSGIServer: Serving HTTP on port {PORT} ...\n')
    httpd.serve_forever()
