import os
from flask import Flask, render_template

# Correctly locate templates and static folders in Vercel serverless environment
base_dir = os.path.abspath(os.path.dirname(__file__))
template_dir = os.path.join(os.path.dirname(base_dir), 'templates')
static_dir = os.path.join(os.path.dirname(base_dir), 'static')

app = Flask(__name__, template_folder=template_dir, static_folder=static_dir)

@app.route('/')
def home():
    return render_template('index.html')

# If you have your contact form or other routes, add them right below here:
