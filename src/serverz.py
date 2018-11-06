# @Author: George Onoufriou <georgeraven>
# @Date:   2018-11-05
# @Filename: serverz.py
# @Last modified by:   georgeraven
# @Last modified time: 2018-11-05
# @License: Please see LICENSE in project root.
# @Copyright: George Onoufriou



class serverz():



    from http.server import HTTPServer, BaseHTTPRequestHandler
    import ssl



    def __init__(self):
        None



    def start(self):
        httpd = self.HTTPServer(('localhost', 4443), self.BaseHTTPRequestHandler)
        httpd.socket = self.ssl.wrap_socket(
            httpd.socket,
            keyfile="",
            certfile="",
            server_side=True
        )
        raise NotImplementedError



    def stop(self):
        raise NotImplementedError



    def getState(self):
        raise NotImplementedError
