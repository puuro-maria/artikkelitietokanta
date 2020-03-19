from application import db

class Artikkeli(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
    onupdate=db.func.current_timestamp())

    name = db.Column(db.String(144), nullable=False)
    publisher = db.Column(db.String(144), nullable=False)
    source = db.Column(db.String(144), nullable=False)
    year = db.Column(db.Integer, nullable=False)


    def __init__(self, name, publisher="kustantaja", source="HY:n kirjasto", year=2020):
        self.name = name
        self.publisher = publisher
        self.source = source
        self.year = year
