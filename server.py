from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def regular_board(): return render_template("index.html", rows=8)

@app.route('/<x>')
def board_x_rows(x):
    max = int(x)
    return render_template("index.html", rows=max)


if __name__=="__main__": app.run(debug=True)
