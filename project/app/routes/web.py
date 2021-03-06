# web_routes.py

from flask import render_template, request, redirect

from models import *
from app import app

# Define public routes
@app.route('/')
def index():
    recent_blogs = Blog.query.order_by(Blog.updated_at.desc()).limit(3).all()
    return render_template("public/index.html", recent_blogs=recent_blogs)

@app.route('/about')
def about():
    return render_template("public/about.html")

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
