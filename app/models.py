from app import db
import random

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    decisions = db.relationship('Decision', backref='owner', lazy='dynamic')

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.id)  # python 2
        except NameError:
            return str(self.id)  # python 3

    def __repr__(self):
        return '<User %r>' % (self.nickname)

class Decision(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(140))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    choices = db.relationship('Choice', backref='decision', lazy='dynamic')

    def randChoice(self):
      random_list = self.choices
      size = len(random_list)
      index = random.randint(0,size-1)
      return random_list[index]

    def __repr__(self):
        return '<Decision %r>' % (self.title)

class Choice(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(140))
    decision_id = db.Column(db.Integer, db.ForeignKey('decision.id'))

    def __repr__(self):
      return '<Choice %r>' % (self.title)