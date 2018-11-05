# @Author: George Onoufriou <georgeraven>
# @Date:   2018-11-05
# @Filename: serverz.py
# @Last modified by:   georgeraven
# @Last modified time: 2018-11-05
# @License: Please see LICENSE in project root.
# @Copyright: George Onoufriou



class serverz():



    def __init__(self):
        from http.server import HTTPServer, BaseHTTPRequestHandler
        import ssl



    def startServer(self):
        httpd = self.HTTPServer(('localhost', 4443), self.BaseHTTPRequestHandler)
        httpd.socket = self.ssl.wrap_socket(
            httpd.socket,
            keyfile="",
            certfile="",
            server_side=True
        )
        raise NotImplementedError



    def stopServer(self):
        raise NotImplementedError



    def getServerState(self):
        raise NotImplementedError
