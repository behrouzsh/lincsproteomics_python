from flask_sqlalchemy import SQLAlchemy
from werkzeug import generate_password_hash, check_password_hash

db = SQLAlchemy()

class Lincs(db.Model):
  __tablename__ = 'lsm_ids'
  row = db.Column(db.Integer, primary_key = True)
  lsm_id = db.Column(db.String(120))
  lsm_similar_id = db.Column(db.String(120))
  similarity = db.Column(db.Numeric)
  #pwdhash = db.Column(db.String(54))

  def __init__(self, lsm_id, lsm_similar_id, similarity, password):
    self.lsm_id = lsm_id
    self.lsm_similar_id = lsm_similar_id
    self.similarity = similarity
  #  self.set_password(password)
     
  #def set_password(self, password):
  #  self.pwdhash = generate_password_hash(password)

  #def check_password(self, password):
  #  return check_password_hash(self.pwdhash, password)
