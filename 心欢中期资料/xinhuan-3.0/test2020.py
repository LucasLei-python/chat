
from flask import jsonify,Flask

app01=Flask(__name__)

@app01.route("/")
def test():
    data=jsonify(("1","2","3","4"))
    print(data)
    return ""

if __name__ == "__main__":
    app01.run(debug=True,port=6005)
    