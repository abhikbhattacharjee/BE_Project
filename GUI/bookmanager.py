"""from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    return render_template("home.html")
  
if __name__ == "__main__":
    app.run(debug=True)
"""

import subprocess
from subprocess import Popen, PIPE
from subprocess import check_output
from flask import Flask
from flask import render_template
from flask import request
import os

def get_shell_script_output_using_communicate(k):
    session = subprocess.Popen(["./BE_Project.sh" + k])
    stdout, stderr = session.communicate()
    if stderr:
        raise Exception("Error "+str(stderr))
    return stdout.decode('utf-8')

def get_shell_script_output_using_check_output(k,l,m,n,o,p,q,r,s,t,u,v):
    stdout = check_output(['./BE_Project.sh',k,l,m,n,o,p,q,r,s,t,u,v]).decode('utf-8')
    return stdout

def get_shell_script_output_using_check_output1(a,b,c,d,e):
    stdout = check_output(['./ChIP_seq.sh',a,b,c,d,e]).decode('utf-8')
    return stdout

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def test1():
    #get_shell_script_output_using_communicate()
    return render_template("ref_page.html")

@app.route('/analysis',methods=['GET','POST'])
def test2():
    #get_shell_script_output_using_communicate()
    return render_template("index.html")

@app.route('/chip_seq',methods=['GET','POST'])
def test3():
    #get_shell_script_output_using_communicate()
    return render_template("chip_module.html")

@app.route('/run',methods=['GET', 'POST'])
def home():
	if request.method == 'POST':
		jaspar_path1 = request.form.get('jaspar_path')  # access the data inside 
		rna_path1 = request.form.get('rna_path')
		up_path1 = request.form.get('up_data')
		down_path1 = request.form.get('down_data')
		not_path1 = request.form.get('not_data')
		dmel_path1 = request.form.get('dmel')
		genome_path1 = request.form.get('genome')
		base_pair_path1 = request.form.get('basepairs')
		up_name_path1 = request.form.get('up_seq')
		down_name_path1 = request.form.get('down_seq')
		not_name_path1 = request.form.get('not_seq')
		save_path1 = request.form.get('save_res')	
    	
	get_shell_script_output_using_check_output(str(jaspar_path1),str(rna_path1),str(up_path1),str(down_path1),str(not_path1),str(dmel_path1),str(genome_path1),str(base_pair_path1),str(up_name_path1),str(down_name_path1),str(not_name_path1),str(save_path1))
    #get_shell_script_output_using_communicate()
	return render_template("index.html")

@app.route('/run1',methods=['GET', 'POST'])
def home1():
	if request.method == 'POST':
		genome_path2 = request.form.get('genome_path')  # access the data inside 
		test_fq_path1 = request.form.get('test_fq')
		input_fq_path1 = request.form.get('input_fq')
		genome_name1 = request.form.get('genome_name')
		save_path2 = request.form.get('save_results')	
    	
	get_shell_script_output_using_check_output1(str(genome_path2),str(test_fq_path1),str(input_fq_path1),str(genome_name1),str(save_path2))
    #get_shell_script_output_using_communicate()
	return render_template("chip_module.html")

app.run(debug=True)
