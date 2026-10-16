"""
Coliseum of Iron - Local Web Game Server
Zero-dependency local HTTP server to launch and run the 3D WebGL engine.
"""

import os
import sys
import webbrowser
from http.server import HTTPServer, SimpleHTTPRequestHandler

PORT = 8080

class NoCacheHTTPRequestHandler(SimpleHTTPRequestHandler):
    """Simple HTTP handler with no-cache headers for smooth local asset development."""
    def end_headers(self):
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate, max-age=0')
        super().end_headers()

def main():
    root_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(root_dir)

    server_address = ('127.0.0.1', PORT)
    httpd = HTTPServer(server_address, NoCacheHTTPRequestHandler)
    url = f"http://localhost:{PORT}/index.html"

    print("=" * 60)
    print("   COLISEUM OF IRON // 3D GLADIATOR COMBAT")
    print("=" * 60)
    print(f"Local server running at: {url}")
    print("Press Ctrl+C to stop the server.")
    print("=" * 60)

    webbrowser.open(url)

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nServer terminated.")

if __name__ == '__main__':
    main()
