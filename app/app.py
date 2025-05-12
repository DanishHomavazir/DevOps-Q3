from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def registration_form():
    return render_template('register.html')

@app.route('/register', methods=['POST'])
def register():
    name = request.form['name']
    email = request.form['email']
    event = request.form['event']
    return f"Thanks {name} for registering for {event}! Confirmation sent to {email}."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
