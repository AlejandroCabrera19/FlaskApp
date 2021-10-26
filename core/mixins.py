from datetime import datetime
from app import db

# Creating the customer model
class BaseModelMixin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    # Nullable default is true, Unique default is False

    def save(self):
        # Used to save data
        db.session.add(self)
        db.session.commit()

    def delete(self):
        # Used to delete data
        db.session.delete(self)
        db.session.commit()

    def to_dict(self):
        # Collects all values and returns a dictionary
        return {"id": f"{self.id}", "date_created": f"{self.date_created}"}
