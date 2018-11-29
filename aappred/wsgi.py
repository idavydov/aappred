#!/usr/bin/env python
from aappred import *


if __name__ == "__main__": 
    app = web.application(urls, globals())
    web.wsgi.runwsgi = lambda func, addr=None: web.wsgi.runfcgi(func, addr)
    app.run()
