        from http.server import HTTPServer, BaseHTTPRequestHandler
        content = """
        <!DOCTYPE html>
        <html>
        <head>
        <title>COMPANY REVENUE</title>
        <caption><h2>TOP REVENUE TABLE </h2></caption>
        </head>
        <body>
        <table border ="2" cellpadding="2" width="600" height="300" bgcolor=yellow">
        <tr bgcolor="pink">
        <th>s.no</th>
        <th>Company Name</th>
        <th>RUPEES in Billon</th>
        <th>Country</th>
        <th>Industry</th>
        </tr>
        <tr >
        <td>1</td>
        <td>Apple</td>
        <td>961.3</td>
        <td>india</td>
        <td>Tech</td>
        </tr>
        <tr>
        <td>2</td>
        <td>Mahendra</td>
        <td>946.5</td>
        <td>japan</td>
        <td>Enma</td>
        </tr>
        <tr>
        <td>3</td>
        <td>Amazon.com</td>
        <td>916.1</td>
        <td>USA</td>
        <td>Tech</td>
        </tr>
        <tr>
        <td>4</td>
        <td>kaido</td>
        <td>863.2</td>
        <td>Wano</td>
        <td>katana</td>
        </tr>
        <tr>
        <td>5</td>
        <td>Berkshire Hathaway</td>
        <td>516.4</td>
        <td>russia</td>
        <td>Financials</td>
        </tr>
        <tr>
        <td>6</td>
        <td>Alibab</td>
        <td>480.8</td>
        <td>Arab</td>
        <td>Oil mine</td>
        </tr>
        </body>
        </html>
        """
        class myhandler(BaseHTTPRequestHandler):
            def do_GET(self):
                print("request received")
                self.send_response(200)
                self.send_header('content-type', 'text/html; charset=utf-8')
                self.end_headers()
                self.wfile.write(content.encode())
        server_address = ('',8000)
        httpd = HTTPServer(server_address,myhandler)
        print("Company Revenue  webserver is running...")
        httpd.serve_forever()