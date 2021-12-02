from flask import Flask, render_template, request
from flask_mysqldb import MySQL
app = Flask(__name__)


app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'sakila'

mysql = MySQL(app)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        details = request.form
        name = details['names']
        companyname = details['companynames']
        UID = details['EUID']
        EmailID = details['emailid']
        names = request.form['names']
        companynames = request.form['companynames']
        EUID = request.form['EUID']
        emailid = request.form['emailid']


        dat = mysql.connection.cursor()
        dat.execute("INSERT INTO Final(Name, CompanyName, UID ,Email) VALUES (%s, %s, %s, %s)", (name, companyname, UID, EmailID))
        mysql.connection.commit()
        dat.close()
        return render_template('finaltemp2.html', q=names, w=companyname, e=EUID, r=emailid)
    return render_template('finaltemp1.html')

@app.route('/second')
def sec():
    return render_template('finaltemp2.html')


if __name__ == '__main__':
    app.run()