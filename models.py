from flask_sqlalchemy import flask_sqlalchemy
db = SQLAlchemy()

DEFAULT_IMAGE_URL="https://www.freeiconspng.com/uploads/icon-user-blue-symbol-people-person-generic--public-domain--21.png"

class User(db.Model):
    """site user."""

    __tablename__="users"

    id = db.Column(db.Integer,primary_key=True)
    first_name = db.Column(db.Text, nullable=False)
    Last_name = db.Column(db.Text, nullable=False)
    image_url = db.Column(db.Text, nullable=False, default=DEFAULT_IMAGE_URL)

    @property
    def full_name(self):
        """return full name of user"""
        return f"{self.first_name} {self.last_name}"

    def connect_db(app):
        """Connent this database to provide Flask app"""
        db.app = app 
        db.init_app(app)
        