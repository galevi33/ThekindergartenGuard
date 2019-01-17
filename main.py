from flask import Flask, jsonify, render_template, request
app = Flask(__name__)
from FL1 import inroom1


 
@app.route('/signUp',methods = ['POST'])
def signUp():
    f = open("testfile.txt","w") 
    f.write("Hello World") 
    f.close() 
    return inroom1()+" "+request.form["hh"]
   
  

if __name__ == "__main__":
   app.run()
