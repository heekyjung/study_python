# 필수 라이브러리
'''
0. Flask : 웹서버를 시작할 수 있는 기능. app이라는 이름으로 플라스크를 시작한다
1. render_template : html파일을 가져와서 보여준다
'''
from flask_sqlalchemy import SQLAlchemy
import os
from flask import Flask, render_template
import random
app = Flask(__name__)

# DB 기본 코드

basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] =\
    'sqlite:///' + os.path.join(basedir, 'database.db')

db = SQLAlchemy(app)


class Rps(db.Model):  # 가위바위보 전적
    round_id = db.Column(db.Integer, primary_key=True)
    player_choice = db.Column(db.String(10), nullable=False)
    computer_choice = db.Column(db.String(10), nullable=False)
    result = db.Column(db.String(10), nullable=False)

    def __repr__(self):
        return f"[Round {self.round_id}] Player: {self.player_choice}, Computer: {self.computer_choice} > Player's result: {self.result}"


with app.app_context():
    db.create_all()


@app.route("/")
@app.route("/rps/")
@app.route("/rps/<playerChoice>/")
def rps(playerChoice=""):
    rps_list = ['Rock', 'Paper', 'Scissors']
    playerChoice = playerChoice.capitalize()
    computerChoice = random.choice(rps_list)
    result = ""
    result_print = ""

    # 승패 판정
    if playerChoice == computerChoice:
        result_print = "Tie! 🙂"
        result = "TIE"
    elif (playerChoice == "Rock" and computerChoice == 'Scissors') or (playerChoice == "Paper" and computerChoice == 'Rock') or (playerChoice == "Scissors" and computerChoice == 'Paper'):
        result_print = "You won!! 😆"
        result = "WIN"
    else:
        result_print = "You lost... 🥲"
        result = "LOSE"

    # 데이터를 DB에 저장하기 (playerChoice가 있을 때만)
    if playerChoice:
        round = Rps(player_choice=playerChoice,
                    computer_choice=computerChoice, result=result)
        db.session.add(round)
        db.session.commit()

    rps_db = Rps.query.all()
    win_count = Rps.query.filter_by(result="WIN").count()
    lose_count = Rps.query.filter_by(result="LOSE").count()
    tie_count = Rps.query.filter_by(result="TIE").count()

    context = {
        "playerChoice": playerChoice,
        "computerChoice": computerChoice,
        "result_print": result_print,
        "rps_db": rps_db,
        "win_count": win_count,
        "lose_count": lose_count,
        "tie_count": tie_count
    }

    return render_template('rps.html', data=context)


if __name__ == "__main__":
    app.run(debug=True)
