from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def regular_board(): 
    return render_template("index.html", rows=8, columns=8, 
        color1="red", color2="black")

@app.route('/<x>')
def board_x_rows(x):
    max_rows = int(x)
    return render_template("index.html", 
        rows=max_rows, columns=8, color1="red", color2="black")

@app.route('/<x>/<y>')
def board_adjust_size(x, y):
    max_rows = int(x)
    max_columns = int(y)
    return render_template("index.html", 
        rows=max_rows, columns=max_columns, color1="red", color2="black")

@app.route('/<x>/<y>/<color1>/<color2>')
def board_adjust_size_color(x, y, color1, color2):
    max_rows = int(x)
    max_columns = int(y)
    color1_str = str(color1)
    color2_str = str(color2)
    return render_template("index.html", 
        rows=max_rows, columns=max_columns, color1=color1_str, color2=color2_str)


if __name__=="__main__": app.run(debug=True)
