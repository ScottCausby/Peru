from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
  return render_template("index.html")

@app.route('/Lima')
def lima():
  return render_template("lima.html")  

@app.route('/LocalCuisines')
def food():
  return render_template("food.html")

@app.route('/FootballTeam')  
def football():
  return render_template("football.html")

if __name__ == '__main__':
    app.run(debug=True)