from flask import Flask,render_template,request
import mysql.connector
app = Flask(__name__)

@app.route('/')
def student():
    return render_template('index.html')

@app.route('/result',methods=['POST','GET'])
def result():
    mydb=mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="register"
    )
    mycursor=mydb.cursor()
    if request.method=='POST':
        signup=request.form
        username=signup['user']
        password=signup['pass']
        mycursor.execute("select * from reg where user='"+username+"' and pass='"+password+"'")
        r=mycursor.fetchall()
        count=mycursor.rowcount
        if count==1:
            return render_template('test.html')
        else:
            return render_template('index.html')
        mydb.commit()
        mycursor.close()
        return "Registeration Successfull"

app.run(debug=True)