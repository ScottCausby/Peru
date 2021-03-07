from flask import Flask, render_template

# Initialize an instance of the Flask class
app = Flask(__name__)

# Define a path: "/" is the "root"
@app.route('/')
def home():
  return render_template("index.html")

# Run the app when the program starts!
if __name__ == '__main__':
    app.run(debug=True)