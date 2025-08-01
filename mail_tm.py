import requests
import time, json


BASE_URL = "https://api.mail.tm"

headers = {
    "accept": "application/json",
    "content-type": "application/json",
}


def create_account_and_get_token():
    while True:
        data = {}

        address = f"{str(int(time.time()))}@somoj.com"
        password = str(int(time.time() * 1000))[-12:]
        response = requests.post(f"{BASE_URL}/accounts", headers=headers, json={"address": address, "password": password})
        print("Response:", response.text)
        if response.status_code == 429:
            print("Error creating account:", response.text)
            continue
        else:
            try:
                response = json.loads(response.text)
                data["id"] = response["id"]
                data["address"] = response["address"]
            except Exception as e:
                continue
            break        
    
    response = requests.post(f"{BASE_URL}/token", headers=headers, json={"address": address, "password": password})
    response = json.loads(response.text)

    data["token"] = response["token"]
    print("Account created successfully:", data)
    
    return data
    

def get_otp(token):
    while True:
        otp = ""
        headers["Authorization"] = f"Bearer {token}"
        response = requests.get(f"{BASE_URL}/messages", headers=headers)
        try:
            otp = json.loads(response.text)[0]["intro"][47:47+6]
            break
        except Exception as e:
            print("Error: OTP not found in the message.", e)
            print("Response:", response.text)

    return otp

def delete_account(token, id):
    headers["Authorization"] = f"Bearer {token}"
    response = requests.delete(f"{BASE_URL}/accounts/{id}", headers=headers)
    if response.status_code == 200:
        return True
    else:
        return False


if __name__ == "__main__":
    # account = create_account_and_get_token()
    # print(account)
    messages = get_otp("eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJpYXQiOjE3NDczMTA5OTIsInJvbGVzIjpbIlJPTEVfVVNFUiJdLCJhZGRyZXNzIjoiMTc0NzMxMDk5MEBkY3BhLm5ldCIsImlkIjoiNjgyNWQ5OGZjYmMxOWFmZGMwMDNmZGI3IiwibWVyY3VyZSI6eyJzdWJzY3JpYmUiOlsiL2FjY291bnRzLzY4MjVkOThmY2JjMTlhZmRjMDAzZmRiNyJdfX0.ekqNqm_i7cwbtK1WxYiOxNg3wLbAdeHN2bjHsLKkcLaVD2GgUvjLaOoaTU7-9gi0Veh-XVyX3Uv7Bi2WFiptdQ")
    print(messages)
