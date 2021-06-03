# -*- coding: utf-8 -*-
"""
Created on Mon Oct 29 12:44:06 2018

@author: z003zafb
# this version is made for the new design of the webpage
"""
from flask import Flask
from flask import render_template,request,jsonify
import math
import numpy as np
import pandas as pd
import json
import numpy.random
import sqlite3

import lib1
from passlib.hash import pbkdf2_sha256

#from flaskr import libtest
app = Flask(__name__)


@app.route('/')
def index():
    #return render_template('trial_button_plot_tab.html')
    return render_template('login.html')

@app.route('/handle_data', methods = ['POST'])
def login():
    username=request.form['username']
    password=request.form['password']    
#    flash('error')
    conn=sqlite3.connect('username.db')
    c=conn.cursor() 
    user=c.execute("SELECT * FROM INFORMATION WHERE name = '%s'" % username).fetchone()
   # password_r=c.execute("SELECT * FROM INFORMATION WHERE pasword = '%s'" % username).fetchone()
    c.close() 
    result=pbkdf2_sha256.verify(password, user[1])
    
    if user:
#        return jsonify(state='successful log in')
        if result:
            message="correct"
            return render_template('template.html')
        else:
            message="The user name or password is incorrect. Try again."
        return render_template('login.html',my_string=message)
    else:
        message="user unfound"        
        return render_template('login.html',my_string=message)    
  



@app.route('/test1', methods = ['POST'])
def func1():
    amp=float(request.form['amp']) # is now str type
    #amp=float(request.form['amp']) 
    typ=int(request.form['typ'])
    t=np.arange(100)/10
#    t=float(amp)
#    dataset=float(typ)
    if typ==1:
        data=amp*np.sin(t)
    else:
        data=amp*np.ones_like(t)
    random_set=lib1.fun1() 
    random_set=random_set.tolist()
    t=t.tolist()
    dataset=data.tolist()
        
    return jsonify(t=t,y1=dataset,random_set=random_set)

@app.route('/loadtable1', methods = ['POST'])
def table1():
    table=pd.read_excel('table1.xls', sheetname='Sheet1',header=None)
    table=np.array(table)
    table=table.tolist()
    return jsonify(table1=table)

@app.route('/loadtable2', methods = ['POST'])
def table2():
    
    table=pd.read_excel('table2.xls',header=None)
    table=np.array(table)
    table=table.tolist()
    return jsonify(table2=table)

@app.route('/replot1', methods = ['POST'])
def replot1():
    #row_index=float(request.form['row_index'])
    num=int(request.form['num'])   
    y1=np.array(json.loads(request.form['y1']))
    table=pd.read_excel('table1.xls',header=None)
    index=np.array(table)[num,:]
    t=np.arange(100)/10
    y2=index[0]*np.sin(index[1]*t)+y1

    y2=y2.tolist()    
    return jsonify(y2=y2)

@app.route('/replot2', methods = ['POST'])
def replot2():
    #row_index=float(request.form['row_index'])
    num=int(request.form['num'])   
    y1=np.array(json.loads(request.form['y1']))
    table=pd.read_excel('table2.xls',header=None)
    index=np.array(table)[num,:]
    t=np.arange(100)/10
    y2=index[0]*np.sin(index[1]*t)+y1

    y2=y2.tolist()    
    return jsonify(y2=y2)

     
@app.route('/route2', methods = ['POST'])
def func2():
    waveform_complex=np.array(json.loads(request.form['waveform_complex']))
    waveform_complex=waveform_complex[0,:]+complex(0,1)*waveform_complex[1,:]
    
    if True :
        #return jsonify({'waveform':waveform})
        return jsonify(waveform_complex=waveform_complex)
    else:
        return jsonify(error='Missing data!')
    

    


    
if __name__ == '__main__':
    app.run()
