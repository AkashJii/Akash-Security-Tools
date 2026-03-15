import requests

print("="*45)
print(" 🌍 AKASH OSINT - IP GEO-LOCATOR 🌍 ")
print("="*45)

# Target se IP maangna
target_ip = input("\nTarget IP daalo (ya blank chhod do apni IP ke liye): ")

# API URL jahan se data aayega
url = f"http://ip-api.com/json/{target_ip}"

try:
    print("\n[~] Locating Target... Ruko zara...")
    
    # Internet se data mangwana
    response = requests.get(url)
    data = response.json() # Data ko dictionary (list) mein badalna
    
    # Agar IP sahi hai toh result dikhao
    if data['status'] == 'success':
        print("\n[+] BOOM! Target Locked! 🎯\n")
        print(f"➤ IP Address : {data['query']}")
        print(f"➤ Country    : {data['country']}")
        print(f"➤ City       : {data['city']}")
        print(f"➤ ISP/Network: {data['isp']}")
        print(f"➤ Lat/Lon    : {data['lat']}, {data['lon']}")
    else:
        print("\n[-] Error: Fake ya Private IP daali hai!")

except Exception as e:
    print("\n[-] Network Error! Internet check karo.")

print("\n" + "="*45)
