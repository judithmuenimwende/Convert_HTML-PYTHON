from flask import Flask
from flask import render_template
app = Flask(__name__)
@app.route("/")
def index():
    return render_template("index.html")


@app.route("/welcome")
@app.route("/welcome/<name>")
def welcome(name = "Guest"):
    context = {'name':name}
    return render_template("welcome.html")

@app.route("/music")
@app.route("/music/<songA>/<songB>/<songC>")
def music(songA = "songA", songB = "songB", songC = "songC"):
    context = {'songA':songA, 'songB':songB, 'songC':songC}
    return render_template("music.html", **context)


@app.route('/add/<int:num1>/<int:num2>')
@app.route('/add/<float:num1>/<float:num2>')
@app.route('/add/<int:num1>/<float:num2>')
@app.route('/add/<float:num1>/<int:num2>')
def add(num1 = 0, num2 = 0):
  total = num1 + num2
  context = {'num1':num1, 'num2':num2, 'total':total}
  return render_template("add_results.html", **context)
if __name__ == '__main__':
  app.run(debug = True,host='0.0.0.0', port=8080)