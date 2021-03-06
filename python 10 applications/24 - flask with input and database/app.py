from flask import Flask, render_template, request
import backend

app = Flask(__name__)
db = backend.Database()

@app.route('/')
def index():
  return render_template("index.html")

@app.route('/success', methods=['POST'])
def success():
  if request.method == 'POST':
    email = request.form["email_name"]
    height = request.form["height_value"]
    db.insert(email, height)
    backend.send_email(email, db.return_average_height())
    return render_template("success.html")

if __name__ == "__main__":
  app.run(debug=True)