import backend
from flask import Flask, render_template, request, send_file
from werkzeug.utils import secure_filename

app = Flask(__name__)
db = backend.Database()

@app.route('/')
def index():
  return render_template("index.html")

@app.route('/success', methods=['POST'])
def success():
  global cake
  if request.method == 'POST':
    email = request.form["email_name"]
    height = request.form["height_value"]
    cake = request.files["file"]
    print(cake.filename)
    cake.save(secure_filename("uploaded-" + cake.filename))
    with open(secure_filename("uploaded-" + cake.filename), "a") as file:
      file.write("\nthis was added later!")
    db.insert(email, height)
    backend.send_email(email, db.return_average_height())
    return render_template("success.html", btn="download.html")

@app.route('/download')
def download():
  return send_file(secure_filename("uploaded-" + cake.filename), attachment_filename="yourfile.txt", as_attachment=True)

if __name__ == "__main__":
  app.run(debug=True)