from flask import Flask, jsonify, render_template, request
from FL1 import checkin


app = Flask(__name__)
 
# @app.route('/signUp',methods = ['POST'])
# def signUp():
#     f = open("testfile.txt","w") 
#     f.write("Hello World") 
#     f.close() 
#     return " f "+request.form["hh"]
   
   
@app.route('/checkin',methods = ['POST'])
def Mcheckin():
    checkin()
    return "checkin-good"
   

if __name__ == "__main__":
   app.run()
