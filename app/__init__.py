import requests
from flask import Flask, render_template, request, redirect, flash, session

app = Flask(__name__)

app.secret_key = 'dhf98dfydhudy8945hu54894y45h4u4rh49ujfe598454uj'


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/start")
def start():
    headers = {
        'Content-type': 'application/json',
    }
    data = open('/var/www/mesos-marathon-web-client/app/api-test.json')
    requests.post('http://node1.mesoscluster.net:8080/v2/apps',
                  headers=headers, data=data)
    return redirect('')


@app.route("/stop")
def stop():
    requests.delete('http://node1.mesoscluster.net:8080/v2/apps/api-test')
    return redirect('')


if __name__ == "__main__":
    app.run(debug=True)
