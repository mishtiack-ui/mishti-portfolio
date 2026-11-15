from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__, template_folder='../templates', static_folder='../static')

@app.route('/')
def home():
    return render_template('index.html')

# If you have a contact form route or other routes from your app.py, include them here:
@app.route('/contact', methods=['POST'])
def contact():
    # your contact form handling logic
    return redirect(url_for('home'))
