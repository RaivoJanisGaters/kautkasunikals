from flask import *
app=Flask(__name__)
@app.route('/',methods=["GET"])

def getIndex():
  return "<a href='/about'><h1>About</h1></a> <a href='/contact'><h1>Contacts</h1></a> </a>"

@app.route('/about')
def getAbout():
  return render_template('about.html')

@app.route('/contact')
def getContact():
  return render_template('contact.html', phone= 12341234)

app.run(host="0.0.0.0",port=8020)