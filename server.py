import os
from pyftpdlib.servers import FTPServer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.authorizers import DummyAuthorizer

address = ("127.0.0.1",21)
handler = FTPHandler
authorizer = DummyAuthorizer()
handler.authorizer = authorizer

authorizer.add_user('user', '12345', '.', perm='elradfmwMT')
authorizer.add_anonymous(os.getcwd())

handler.banner = "Welcome to the server"

server = FTPServer(address,handler)
server.serve_forever()
authorizer.add_user()
