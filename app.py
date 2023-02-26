import requests
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def main():
    return render_template("index.html")


# @app.route('/detail/<keyword>')
# def detail(keyword):
#     return render_template("detail.html", keyword=keyword)


@app.route('/jobs')
def jobs():
    people = requests.get('https://my-json-server.typicode.com/jjjosephhh/test-db-002/people').json()
    print(people)
    return render_template("detail.html", people=people)

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
