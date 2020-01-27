import backend, os, time
from flask import Flask, render_template, request, send_file
from werkzeug.utils import secure_filename

app = Flask(__name__)

@app.route('/')
def index():
  return render_template("index.html")

@app.route('/success', methods=['POST'])
def success():
  global filename
  if request.method == 'POST':
    file = request.files["file"]
    filename = secure_filename("tmp_" + file.filename)
    file.save(filename)
    if backend.has_volcano_column(filename):
      html = backend.append_to_csv(filename)
      os.remove(filename)
      return render_template("success.html", text=html, btn="download.html")
    else:
      os.remove(filename)
      return render_template("index.html", text="Your .csv file must have a column named 'Volcano' or 'volcano'.")

@app.route('/download')
def download():
  try:
    file_path = "results_" + filename
    file_handle = open(file_path, "r")
    def stream_and_remove():
      yield from file_handle
      file_handle.close()
      os.remove(file_path)
    return app.response_class(stream_and_remove(), headers={'Content-Disposition': 'attachment; filename=coordinates_added_{file_path}'.format(file_path=file_path[12:]), 'Content-type': 'text/csv'})
  except:
    return render_template("index.html", text="Your file was deleted off the server after you downloaded it. Feel free to upload another for more coordinates!")

if __name__ == "__main__":
  app.run(debug=True)