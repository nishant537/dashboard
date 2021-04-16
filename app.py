from flask import Flask,render_template,url_for,request,redirect,jsonify
import os
import sqlite3
import pymysql as mdb
import numpy as np
import cgi
import json

app=Flask(__name__)

headings=('Id','alert_object','camera_name','alert_timestamp','status')
# data=(('Nishant','delhi','9999441808'),('AG','delhi','9999775243'))

@app.route('/',methods=['GET','POST'])
def home():
    if request.method=='POST':
        selected=request.form["cameras"]
        with open('hi.txt','w') as file:
            file.write(selected)
    return render_template('home.html')

@app.route('/update',methods=['GET','POST'])    
def update():
    selection=request.get_data('selection')
    print(selection)
    db=mdb.connect(host='localhost', user= 'root', passwd='nishant1234',db='alerts_db')
    cur=db.cursor()
    cur.execute('select table_1.id,table_1.alert_object,table_2.json,table_1.alert_timestamp,table_1.status from alerts_db.alertstable table_1 join camdb.camtable table_2 on table_1.camera_id=table_2.id;')
    a=cur.fetchall()
    data=[list(i) for i in list(a)]
    for i in range(len(data)):
        data[i][2]=json.loads(data[i][2])['camera_name']

    return jsonify('',render_template('ajax.html',data=data,headings=headings))