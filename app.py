from modules import adduser
from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

@app.route('/', methods=["POST","GET"])
def index():
    if request.method == "POST":
        user = request.form["nm"]
        mail = request.form["ml"]
        phone = request.form["ph"]
        adduser(user,mail,phone)
        return redirect(url_for('user', usr=user))
    else:
        return render_template('login.html')

@app.route('/<usr>')
def user(usr):
    return render_template('user.html', user=usr)

if __name__ == '__main__':
    app.run(debug=True)
 