from app import app, db
from app.models import GameResult
from app.game import TicTacToeGame
from flask import render_template, request, redirect, url_for, session

# Global variable to hold the game state (temporary, consider using DB/session)
current_game = TicTacToeGame()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/game', methods=['GET', 'POST'])
def game():
    global current_game

    if request.method == 'POST':
        position = request.form['position']
        row, col = map(int, position.split('-'))

        if current_game.play(row, col):
            if current_game.winner:
                winner = current_game.winner
                game_result = GameResult(player1="Player 1", player2="Player 2", winner=winner)
                db.session.add(game_result)
                db.session.commit()
                return render_template('game_over.html', winner=winner)
            elif current_game.is_draw():
                game_result = GameResult(player1="Player 1", player2="Player 2", draw=True)
                db.session.add(game_result)
                db.session.commit()
                return render_template('game_over.html', winner="Draw")

    return render_template('game.html', game=current_game)