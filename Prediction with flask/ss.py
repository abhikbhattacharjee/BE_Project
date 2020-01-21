import os
from flask import Flask
from flask import render_template


app = Flask(__name__,static_folder="static",template_folder="templates")

@app.route('/',methods=["GET","POST"])
def home():
	return render_template("home.html")
	
	

@app.route('/human',methods=["GET","POST"])
def processing():	
	#os.system("bash shells.sh")
	return render_template("home1.html")

app.run(debug=True)
