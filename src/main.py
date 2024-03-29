from API import API
import sys

API.OnProgramStart.Initialize(
    "APP NAME", "APP SECRET", "APP VERSION")

print("\n[1] Login")
print("[2] Login (license only)")
print("[3] Register")
if not API.ApplicationSettings.freeMode:
    print("[4] Extend Subscription")
print("\nOption:")
option = input()

if option == "1":
    print("\nUsername:")
    username = input()
    print("Password:")
    password = input()
    print("2FA code (if enabled):")
    twoFactorCode = input()

    if API.login(username=username, password=password, twoFactorCode=twoFactorCode):
        print("Successfully Logged In!")
        API.log(username=API.User.username, action="User logged in")
        print("ID:", API.User.id)
        print("Username:", API.User.username)
        print("Email:", API.User.email)
        print("Subscription Expiry:", API.User.expiry)
        print("HWID:", API.User.hwid)
        print("Last Login:", API.User.lastLogin)
        print("IP:", API.User.ip)
        # Do code you want
        print("Press 1 to enable 2FA, press 2 to disable 2FA:")
        option = input()
        if option == "1":
            API.createQRCode()
            print("QR Code:")
            code = input()
            API.verify2FA(code)
        if option == "2":
            print("QR Code:")
            code = input()
            API.disable2FA(code)

    else:
        sys.exit(0)

elif option == "2":
    print("\License:")
    license = input()

    if API.loginLicenseOnly(license=license):
        print("Successfully Logged In!")
        API.log(username=API.User.username, action="User logged in")
        print("ID:", API.User.id)
        print("Username:", API.User.username)
        print("Email:", API.User.email)
        print("Subscription Expiry:", API.User.expiry)
        print("HWID:", API.User.hwid)
        print("Last Login:", API.User.lastLogin)
        print("IP:", API.User.ip)
        input()
        # Do code you want
    else:
        sys.exit(0)

elif option == "3":
    print("\nUsername:")
    username = input()
    print("Password:")
    password = input()
    print("Email:")
    email = input()
    license = "N/A"
    if not API.ApplicationSettings.freeMode:
        print("License:")
        license = input()

    if API.register(username=username, password=password, email=email, license=license):
        print("Successfully Registered!")
        API.log(username=API.User.username, action="User registered")
        input()
        # Do code you want
    else:
        sys.exit(0)

if not API.ApplicationSettings.freeMode:
    if option == "4":
        print("\nUsername:")
        username = input()
        print("Password:")
        password = input()
        print("License:")
        license = input()

        if API.extendSub(username=username, password=password, license=license):
            print("Successfully Extended Your Subscription!")
            API.log(username=API.User.username, action="User extended")
            input()
            # Do code you want
        else:
            sys.exit(0)
