from app import db
import datetime

class Blog(db.Model):
    # Always need an id
    id = db.Column(db.Integer, primary_key=True)

    # User attributes
    title = db.Column(db.String(128))
    desc = db.Column(db.Text)
    body = db.Column(db.Text)
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)

    def __init__(self, title, desc, body):
        self.title = title
        self.desc = desc
        self.body = body
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

def create_blog(title, desc, body):
    blog = Blog(title, desc, body)

    # Actually add user to the database
    db.session.add(blog)

    # Save all pending changes to the database
    db.session.commit()

    return blog

def get_blog(id):
    blog = Blog.query.filter_by(id=id).first()
    return blog