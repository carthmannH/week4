import pytest
from flask import Flask, render_template, request

@pytest.fixture
def client():
    app = Flask(__name__)

    @app.route("/")
    @app.route("/home")
    def home():
        return render_template("home.html")

    @app.route("/account", methods=["POST", "GET"])
    def account():
        usr = "<User Not Defined>"
        if request.method == "POST":
            usr = request.form["name"]
            if not usr:
                usr = "<User Not Defined>"
        return render_template("account.html", username=usr)

    with app.test_client() as client:
        yield client

def test_home(client):
    response = client.get("/")
    assert response.status_code == 200
   

def test_account(client):
    response = client.get("/account")
    assert response.status_code == 200
   

def test_account_post(client):
    response = client.post("/account", data={"name": "John"})
    assert response.status_code == 200
   
