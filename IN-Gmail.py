import requests
import time
print("""
  

██╗███╗░░██╗░██████╗░███╗░░░███╗░█████╗░██╗██╗░░░░░
██║████╗░██║██╔════╝░████╗░████║██╔══██╗██║██║░░░░░
██║██╔██╗██║██║░░██╗░██╔████╔██║███████║██║██║░░░░░
██║██║╚████║██║░░╚██╗██║╚██╔╝██║██╔══██║██║██║░░░░░
██║██║░╚███║╚██████╔╝██║░╚═╝░██║██║░░██║██║███████╗
╚═╝╚═╝░░╚══╝░╚═════╝░╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝╚══════╝
 
 
 
                                     """)
time.sleep(2)

print("[!] The tool is under development\n[*]GitHub :- github.com/kanekikon\n[*]Telegram :- T.me/SSScw")
print(">>>>>>>>>>>>>>>>>>>>>\n")
time.sleep(2)
print("[!] Enter the end of email @gmail.com")
email = input("[?] Enter E-mail:")
def gmail():
 url = "https://mmo69.com/_check_live_email/api.php?email=" +email
 headers = {
 "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
 "Accept-Encoding": "gzip, deflate, br",
 "Accept-Language": "ar",
 "Connection": "keep-alive",
 "Host": "mmo69.com",
 "User-Agent": "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36"
 }
 data = {"email":email}
 rr = requests.get(url, headers=headers, data=data)
 if rr.text.find("LIVE") >= 0:
     print("[√] Found account in gmail:", email)
 else:
     print("[×] Not Found account in gmail:", email)
def instagram():
    url = "https://www.instagram.com/accounts/account_recovery_send_ajax/"
    headers = {
        "accept": "*/*",
        "accept-encoding": "gzip,deflate,br",
        "accept-language": "ar,en-US;q=0.9,en;q=0.8",
        "content-length": "49",
        "content-type": "application/x-www-form-urlencoded",
        "origin": "https://www.instagram.com",
        "referer": "https://www.instagram.com/accounts/password/reset/",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36",
        "x-csrftoken": "j4u26vxxC6D7eE63HhBde0ahZeN4mVfK",
        "x-ig-app-id": "936619743392459"
    }
    data = {"email_or_username":email, "recaptcha_challenge_field": ""}
    rr = requests.post(url, headers=headers, data=data)
    if rr.status_code == 200:
        print("[√] Found account in instagram:",email)
    else:
        print("[×] Not Found account in instagram:", email)
gmail()
instagram()
input("\n[x] Enter To exit")
exit()