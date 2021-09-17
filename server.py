from flask import Flask , request
import json
from main import *

app = Flask(__name__)


@app.route('/api/solveBoard', methods=['GET','POST'])
def solve():
    data = json.loads(request.data)
    board = data["board"]
    solveBoard(board)
    data["board"] = board
    return data

if __name__ == "__main__":
    app.run(debug=True)