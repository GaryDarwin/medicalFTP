#importing necessary modules
import os
from pyftpdlib.servers import FTPServer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.authorizers import DummyAuthorizer

#the address of the server, also specifies the port
#so local host, can only communicate with itself
address = ("127.0.0.1",21)
handler = FTPHandler
authorizer = DummyAuthorizer()
handler.authorizer = authorizer

authorizer.add_user('user', '12345', './files', perm='elradfmwMT')
#authorizer.add_anonymous('./files')

#simple banner to welcome user
handler.banner = "Welcome to the server"

#passing the address along
server = FTPServer(address,handler)
server.serve_forever()
#adds the user
authorizer.add_user()
