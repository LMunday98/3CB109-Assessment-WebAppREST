# web_routes.py

from flask import render_template

from app import app

# Define user routes
@app.route('/')
def index():
    return render_template("public/index.html")

@app.route('/about')
def about():
    return render_template("public/about.html")

@app.route('/blog')
def blog():
    return render_template("public/blog.html")

@app.route('/training')
def training():
    return render_template("public/training.html")

@app.route('/contact')
def contact():
    return render_template("public/contact.html")

# Define auth routes
@app.route('/auth/login')
def user_login():
    return render_template("auth/login.html")

@app.route('/auth/register')
def user_register():
    return render_template("auth/register.html")

# Define admin routes
@app.route('/admin/blog')
def admin_blog():
    return render_template("admin/blog.html")