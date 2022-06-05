
from os import error
from flask import Flask, render_template, request, json, redirect
from flaskext.mysql import MySQL
from flask import session

app = Flask(__name__)

mysql = MySQL()

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
app.config['MYSQL_DATABASE_DB'] = 'TodoList'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['MYSQL_DATABASE_PORT'] = 8889
mysql.init_app(app)



app.secret_key = 'secret key can be anything!'


@app.route("/")
def main():
    return render_template('index.html')

@app.route('/showSignUp')
def showSignUp():
    return render_template('signup.html')

@app.route('/showSignin')
def showSignin():
    return render_template('signin.html')

@app.route('/userHome')
def userHome():
    if session.get('user'):
        return render_template('userHome.html')
    else:
        return render_template('error.html',error = 'Unauthorized Access')

@app.route('/logout')
def logout():
    session.pop('user',None)
    return redirect('/')


@app.route('/validateLogin', methods=['POST'])
def validateLogin():
    try:
        _email = request.form['inputEmail']
        _password = request.form['inputPassword']

        con = mysql.connect()
        cursor = con.cursor()
        

        cursor.execute("SELECT * FROM tbl_user WHERE email = %s", (_email))

        data = cursor.fetchall()


        if len(data) > 0:
            if str(data[0][3]) == _password:
                session['user'] = data[0][0]
                return redirect('/userHome')
            else:
                return render_template('error.html',error = 'Wrong Email address or Password.')
        else:
            return render_template('error.html',error = 'Wrong Email address or Password.')


    except Exception as e:
        return render_template('error.html',error = str(e))
    finally:
        cursor.close()
        con.close()

    
@app.route('/signUp',methods=['POST'])
def signUp():
 
    # read the posted values from the UI
    _name = request.form['inputName']
    _email = request.form['inputEmail']
    _password = request.form['inputPassword']
 
    # validate the received values
    if _name and _email and _password:

        conn = mysql.connect()
        cursor = conn.cursor()

        cursor.execute("INSERT INTO tbl_user(name, email, password) VALUES (%s, %s, %s)", (_name, _email, _password))
        

        data = cursor.fetchall()

        if len(data) == 0:
            conn.commit()
            return json.dumps({'message':'User created successfully !'})
        else:
            return json.dumps({'error':str(data[0])})


    else:
        return json.dumps({'html':'<span>Enter the required fields!</span>'})

@app.route('/addItem',methods=['POST'])
def addItem():
            if session.get('user'):
                    _title = request.form['inputTitle']
                    _description = request.form['inputDescription']
                    _user = session.get('user')

                    conn = mysql.connect()
                    cursor = conn.cursor()

                    cursor.execute("INSERT INTO tbl_todo(title, description, userid) VALUES (%s, %s, %s)", (_title, _description, _user))
                    data = cursor.fetchall()

                    if len(data) == 0:
                        conn.commit()
                        return json.dumps({'message':'Todo item created successfully !'})
                    else:
                        return json.dumps({'error':str(data[0])})
            else:
                return render_template('error.html', error = 'An error occurred!')

@app.route("/ajax_delete",methods=["POST","GET"])
def ajax_delete():
    conn = mysql.connect()
    cursor = conn.cursor()
    if request.method == 'POST':
        getid = request.form['string']
        print(getid)
        cursor.execute('DELETE FROM tbl_todo WHERE id = {0}'.format(getid))
        conn.commit()       
        cursor.close()
        msg = 'Record deleted successfully'    
    return jsonify(msg) 

@app.route("/ajax_update",methods=["POST","GET"])
def ajax_update():
    conn = mysql.connect()
    cursor = conn.cursor()
    if request.method == 'POST':
        string = request.form['string']
        txttitle = request.form['title']
        txtdescription = request.form['description']
        
        print(string)
        cursor.execute("UPDATE tbl_todo SET id = %s, title = %s, description = %s WHERE id = %s ", [string, txttitle, txtdescription, string])
        conn.commit()       
        cursor.close()
        msg = 'Record successfully Updated'    
        
    return redirect('/showAddItem')


if __name__ == "__main__":
    app.run()   




