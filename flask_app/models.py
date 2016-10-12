from App import db

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False, index=True)
    detail = db.Column(db.String(5000))
    timestamp = db.Column(db.DateTime)

    def __repr__(self):
        return '<Todo %r>' % (self.title)


class Hyoka(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False, index=True)
    detail = db.Column(db.String(5000))
    choice = db.Column(db.String(100))
    timestamp = db.Column(db.DateTime)

    def __repr__(self):
        return '<Hyoka %r>' % (self.title)

db.create_all()
