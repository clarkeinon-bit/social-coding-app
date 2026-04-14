import ipaddress

print("--- Welcome to our Team IP Tool! ---")

def check_ip():
    user_input = input("Enter an IP address (e.g., 192.168.1.1): ")
    try:
        # This one line does all the hard math for us!
        obj = ipaddress.ip_address(user_input)
        
        print(f"✅ Valid IP: {user_input}")
        print(f"🌐 Type: IPv{obj.version}")
        print(f"🏠 Is it Private? {'Yes' if obj.is_private else 'No, it is Public'}")
        
    except ValueError:
        print("❌ Oops! That's not a real IP address. Try again.")

check_ip()
