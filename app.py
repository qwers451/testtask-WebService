from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def hello():
    name = request.args.get('name', 'Recruto')
    message = request.args.get('message', 'Давай дружить')
    response = f"Hello {name}! {message}!"
    return response

if __name__ == '__main__':
    app.run()