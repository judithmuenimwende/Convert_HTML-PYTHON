from flask import Flask
app = Flask(__name__)
@app.route("/")
def index():
    return """
    <html>
    <body>
    <div>
    <p>Welcome to Akirachix</p>
    </div>
    </body>
    </html>
    """

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080)