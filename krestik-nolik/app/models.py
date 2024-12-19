from app import db

class GameResult(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    player1 = db.Column(db.String(100), nullable=False)
    player2 = db.Column(db.String(100), nullable=False)
    winner = db.Column(db.String(10), nullable=True)
    draw = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f'<Game {self.id} | {self.player1} vs {self.player2}>'
