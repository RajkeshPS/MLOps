from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return"""
    <h1>Welcome to my API!</h1>
    <p>Try these endpoints:</p>
    <ul>
        <li><a href="/tips">/tips</a> - See all tips</li>
        <li><a href="/tips/random">/tips/random</a> - Get a random tip</li>
    </ul>
    """
@app.route('/tips', methods=['GET'])

   
@app.route('/tips/random', methods=['GET'])


@app.route('/tips/<int:tip_id>', methods=['GET'])


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

# link address in readme