from flask import *
from flask_cors import CORS
import glbgpt
import mail_tm
import time

app = Flask(__name__)
CORS(app)


@app.route("/")
def index():
    return "Server is up and running!!!"

@app.route("/once")
def once():
    account = mail_tm.create_account_and_get_token()
    id = account["id"]
    token = account["token"]
    email = account["address"]
    print(id, email)

    glbgpt.send_otp(email)
    print("Waiting for OTP...")
    time.sleep(7)
    otp = mail_tm.get_otp(token)
    print(otp)
    glbgpt.verify_otp(email, otp)

    return jsonify({"sucess": True})


if __name__ == '__main__':
    app.run("0.0.0.0", port=5000, debug=True)