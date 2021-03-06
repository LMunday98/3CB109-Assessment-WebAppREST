from app import db
import datetime

class Event(db.Model):
    __tablename__ = 'events'
    __table_args__ = {'extend_existing': True}

    # Always need an id
    id = db.Column(db.Integer, primary_key=True)

    # Event attributes
    title = db.Column(db.String(128))
    event_type = db.Column(db.String(128))
    event_date = db.Column(db.Date)
    event_start = db.Column(db.Time)
    event_end = db.Column(db.Time)
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)

    def __init__(self, title, event_type, event_date, event_start, event_end):
        self.title = title
        self.event_type = event_type
        self.event_date = event_date
        self.event_start = event_start
        self.event_end = event_end
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

    @staticmethod
    def get(id):
        event = Event.query.filter_by(id=id).first()
        return event

    @staticmethod
    def get_all():
        events = Event.query.all()
        return events
    
    @classmethod
    def create(cls, title, event_type, event_date=datetime.date.today(), event_start=datetime.datetime.now().time(), event_end=datetime.datetime.now().time()):
        event = Event(title, event_type, event_date, event_start, event_end)

        # Actually add event to the database
        db.session.add(event)

        # Save all pending changes to the database
        db.session.commit()

        return event

    def update(self, title, event_type, event_date, event_start, event_end):
        self.title = title
        self.event_type = event_type
        self.event_date = event_date
        self.event_start = event_start
        self.event_end = event_end
        self.updated_at = datetime.datetime.now()
        db.session.commit()

    @staticmethod
    def delete(id):
        event = Event.query.filter_by(id=id).first()
        db.session.delete(event)
        db.session.commit()

    @classmethod
    def seed(cls, fake):
        title = fake.sentence()
        event_type = fake.sentence()
        event_date = datetime.date.today()
        event_start = datetime.datetime.now().time()
        event_end = datetime.datetime.now().time()
        cls.create(title, event_type, event_date, event_start, event_end)