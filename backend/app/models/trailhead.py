from ..extensions import db


class Trailhead(db.Model):
    __tablename__ = "trailhead"

    id = db.Column(db.Integer, primary_key=True)
    park_name = db.Column(db.String(80), nullable=False)
    trailhead_name = db.Column(db.String(80), nullable=False)
    am_capacity = db.Column(db.Integer, nullable=False)
    pm_capacity = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return '<Trailhead %s, %s, %r, %r>' % self.park_name, self.trailhead_name, self.am_capacity, self.pm_capacity

    @classmethod
    def get_trialhead_by_id(cls, id):
        return cls.filter(id=id).one_or_none()

    @classmethod
    def get_all_trailheads_by_park_name(cls, park_name):
        return cls.filter(park_name=park_name).all()
