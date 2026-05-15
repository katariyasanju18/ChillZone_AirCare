from flask import Flask, render_template,request,redirect,flash

from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.secret_key = 'coolair_secret_key'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False
db = SQLAlchemy(app)

# Creating Table with help of Flask
class Contact(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    phone = db.Column(db.String(100))
    message = db.Column(db.String(100))


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/contact', methods=['POST'])
def contact():
    name = request.form['name']
    email = request.form['email']
    phone = request.form['Phone']  # request.form['field_name'] and name="phone" Both names MUST match exactly.
    message = request.form['message']

    new_contact = Contact(
        name = name,
        email = email,
        phone = phone,
        message = message
    )
    db.session.add(new_contact) # Used in Flask with SQLALchemy to store a new object temporarilly in the database sessio before saving it permanently.
   # Add this new_contact  record into the database session so it can be saved.

    db.session.commit()

    flash("Message Sent Successfully!") # flash() is used to show temporary messages to the user after an action happens.

    return redirect('/')
with app.app_context():

    db.create_all()


if __name__ == '__main__':
    app.run(debug=True)