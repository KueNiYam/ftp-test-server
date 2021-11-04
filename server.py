import os
import sys

from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

HOST = 'localhost'
FILE_DIR = os.path.join(os.getcwd(), 'files')


def main():
    port = 9021

    if len(sys.argv) >= 2:
        port = int(sys.argv[1])

    authorizer = DummyAuthorizer()
    authorizer.add_user('peoplefund', 'abcd1234', FILE_DIR, perm='elr')

    handler = FTPHandler
    handler.banner = 'Peoplefund FTP Simple Test Server'
    handler.authorizer = authorizer
    handler.passive_ports = range(60000, 65535)

    address = HOST, port

    server = FTPServer(address, handler)
    server.max_cons = 256
    server.max_cons_per_ip = 5

    server.serve_forever()


if __name__ == '__main__':
    main()
