import requests
import mail_tm


BASE_URL = "https://api.glbgpt.com/api/login"


def send_otp(email):
    response = requests.post(f"{BASE_URL}/email/send-verfiy-mail", json={"email": email})
    if response.status_code == 200:
        return True
    else:
        return False

def verify_otp(email, otp):
    response = requests.post(f"{BASE_URL}/email", json={"code": otp, "deviceType": "pc", "email": email, "inviter": "0x671e2cce425a4f5adedad46f10217fa9a2cb766e"})
    print(response.json())
    
    if response.json()["code"] != 401:
        return True
    else:
        return False


if __name__ == "__main__":
    # send_otp("1747310990@dcpa.net")
    verify_otp("1747310990@dcpa.net", "313128")