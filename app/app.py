from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def registration_form():
    return render_template('register.html')

@app.route('/register', methods=['POST'])
def register():
    name = request.form.get('name')
    email = request.form.get('email')
    event = request.form.get('event')

    if not name or not email or not event:
        return "Missing data", 400

    return f"Thanks {name} for registering for {event}! Confirmation sent to {email}."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
