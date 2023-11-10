import http.server
import socketserver
import webbrowser
import os
port = 8000

html_file = "./ml_color_music_score-master/cluster-analysis.html"

web_dir = "."
os.chdir(web_dir)

handler = http.server.SimpleHTTPRequestHandler

try:
    with socketserver.TCPServer(("", port), handler) as httpd:
        print(f"Serving at http://localhost:{port}")
        webbrowser.open(f"http://localhost:{port}/{html_file}")
        httpd.serve_forever()
except OSError as e:
    print(f"Error: Port {port} is not available. Please choose a different port.")
