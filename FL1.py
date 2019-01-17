from flask import Flask, jsonify, render_template, request
import datetime
def checkin():
   aaa=datetime.datetime.now()
   f = open("G_"+request.form["garden"]+" C_"+request.form["class"]+"_checkinDB.txt","a") 
   f.write(request.form["kid"]+"_"+request.form["direction"]+"_"+aaa.strftime("%m-%d-%Y.%H:%M:%S")+"\n") 
   f.close() 