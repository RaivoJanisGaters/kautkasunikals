from flask import Flask, render_template, request
from file_proc import read_file, write_file

app = Flask(__name__)

@app.route('/')
@app.route("/index")

@app.route("/params")
def params():
  return request.args

@app.route("/post_req", methods = ['POST'])
def post_req():
  return request.args

@app.route('/read_file')
def read_from_file():
  content = read_file()
  return content

@app.route('/home')
def getHome():
  return render_template('home.html', active_page = 'home')

@app.route('/about')
def about():
  return render_template('about.html')

@app.route('/write_file', methods = ['POST'])
def write_to_file():
  if request.content_type == 'application/json':
    contentJSON = request.get_json()
    write_file(contentJSON['data'])
    return f"Add line {contentJSON['data']} to file"
  else:
    return f"Invalid request {request.content_type} not supported!"

@app.route("/file", methods =['GET', 'POST'])
def fileWork():
  if request.method == 'GET':
    return read_from_file()
  elif request.method == 'POST':
    return write_to_file()
  else:
    return f"Method {request.method} not supported!"

@app.route('/contact')
def contact():
  return render_template('contact.html', phone = "99887766")

@app.route('/json')
def json_get():
  list = []
  list.append("value1")
  list.append("value2")
  list.append("value3")
  return justify({"data":list})

if __name__ == '__main__':
  app.run(host="0.0.0.0", threaded=True, port=5000, debug=True)