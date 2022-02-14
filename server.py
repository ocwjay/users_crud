from dataclasses import dataclass
from flask import Flask, render_template, redirect, request
from user import User
app = Flask(__name__)
app.secret_key = "Yo, hello?"

@app.route('/')
def show_all_users():
    users = User.get_all()
    print(users)
    return render_template('read(all).html', all_users = users)

@app.route('/user/<int:id>')
def show_one_user(id):
    data = {
        'id':id
    }
    return render_template('read(one).html', user = User.get_one(data))

@app.route('/edit/<int:id>')
def edit_user_page(id):
    data = {
        'id':id
    }
    return render_template('edit.html', user = User.get_one(data))

@app.route('/edit_submission/<int:id>', methods=['POST'])
def edit_submission(id):
    data = {
        'id' : id,
        'fname' : request.form['fname'],
        'lname' : request.form['lname'],
        'email' : request.form['email']
    }
    User.update_user(data)
    return redirect('/user/' + str(id))

@app.route('/create')
def create_user():
    return render_template('create.html')

@app.route('/submit', methods=['POST'])
def create_user_submit():
    data = {
        'fname' : request.form['fname'],
        'lname' : request.form['lname'],
        'email' : request.form['email']
    }
    user_id = User.add_new_user(data)
    # print("type test: ", User.add_new_user(data))
    return redirect(f'/user/{user_id}')

@app.route('/delete/<int:id>')
def delete_user(id):
    data = {
        'id':id
    }
    User.delete_user(data)
    return redirect ('/')

if __name__ == '__main__':
    app.run(debug=True)