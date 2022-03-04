"""Models for Blogly."""

from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()


def connect_db(app):
    db.app = app
    db.init_app(app)

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.integer, primary_key=True,)

    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)
    image_url = db.Column(db.Text, nullable = False)
    feedback = db.relationship("Feedback", backref="user", cascade="all,delete")
    posts = db.relationship('posts')

    @property 
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

class Post(db.Model):
    __tablename__ = 'posts'

    id = db.Column(db.integer, primary_key=True,)

    title = db.Column(db.Text, nullable = False)
    content = db.Column(db.Text, nullable - False)
    created = db.Column(db.DateTime, nullable = False, default = datetime.datetime.now)
    user = db.Column(db.integer, db.foreignKey('users.id'), nullable =False)

    @property
    def friendly_date(self):
        """Return nicely-formatted date."""

        return self.created_at.strftime("%a %b %-d  %Y, %-I:%M %p")

class Tag(db.Model):
    __tablename__ = 'tag'

    id = db.Column(db.integer, primary_key=True,)
    name = db.Column(db.Text, nullable = False)

class PostTag(db.Model):
    __tablename__ = 'post tags'

    tag_id = db.Column(db.interger, db.foreignKey('tag.id'), primary_key = False)
    post_id = db.Column(db.interger, db.foreignKey('post.id'), primary_key = False)
