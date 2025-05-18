import mail_tm
import glbgpt
import time, os

def get_credit():
    os.system("rm -rf __pycache__")

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


if __name__ == "__main__":
    get_credit()