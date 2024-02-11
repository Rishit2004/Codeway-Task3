import random
import string
from flask import Flask, render_template

app = Flask(__name__, static_url_path='/static')

@app.route('/')
def index():
    # Generate a password
    length = 12  # You may prompt the user for the desired length
    password = generate_password(length)
    
    return render_template('gen.html', password=password)

@app.route('/new-password')
def new_password():
    # Generate a new password
    length = 12  # You may prompt the user for the desired length
    password = generate_password(length)
    
    return password

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

if __name__ == '__main__':
    app.run(debug=True)
