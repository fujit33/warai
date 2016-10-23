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

class Survey(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    boke0 = db.Column(db.Integer)
    boke1 = db.Column(db.Integer)
    boke2 = db.Column(db.Integer)
    boke3 = db.Column(db.Integer)
    boke4 = db.Column(db.Integer)
    boke5 = db.Column(db.Integer)
    boke6 = db.Column(db.Integer)
    boke7 = db.Column(db.Integer)
    boke8 = db.Column(db.Integer)
    boke9 = db.Column(db.Integer)
    boke10 = db.Column(db.Integer)
    boke11 = db.Column(db.Integer)
    boke12 = db.Column(db.Integer)
    boke13 = db.Column(db.Integer)
    boke14 = db.Column(db.Integer)
    boke15 = db.Column(db.Integer)
    boke16 = db.Column(db.Integer)
    boke17 = db.Column(db.Integer)
    boke18 = db.Column(db.Integer)
    boke19 = db.Column(db.Integer)
    boke20 = db.Column(db.Integer)
    boke21 = db.Column(db.Integer)
    boke22 = db.Column(db.Integer)
    boke23 = db.Column(db.Integer)
    boke24 = db.Column(db.Integer)
    boke25 = db.Column(db.Integer)
    boke26 = db.Column(db.Integer)

    boke27 = db.Column(db.Integer)
    boke28 = db.Column(db.Integer)
    boke29 = db.Column(db.Integer)

    comp0 = db.Column(db.String(20))
    comp1 = db.Column(db.String(20))
    comp2 = db.Column(db.String(20))
    comp3 = db.Column(db.String(20))

    hito0 = db.Column(db.String(20))
    hito1 = db.Column(db.String(20))
    hito2 = db.Column(db.String(20))
    hito3 = db.Column(db.String(20))
    hito4 = db.Column(db.String(20))
    hito5 = db.Column(db.String(20))
    hito6 = db.Column(db.String(20))

    botti = db.Column(db.Integer)

    bokete = db.Column(db.String(5000))
    twitter = db.Column(db.String(500))

    timestamp = db.Column(db.DateTime)
    def __repr__(self):
        return '<Survey %r>' % (self.timestamp)

db.create_all()
