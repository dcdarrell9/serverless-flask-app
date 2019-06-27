from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def main():
    return json.dumps(
        {
            "test": "json"
        }
    )


if __name__ == "__main__":
    app.run()
