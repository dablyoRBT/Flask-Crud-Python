from flask import Flask

app = Flask(__name__)

@app.route("/")
def primeira_rota():
    return "Essa é minha primeira rota com Flask :)"

if __name__ == "__main__":
    app.run(debug=True)