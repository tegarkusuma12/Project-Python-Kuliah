accounts = {
    "aplpha" : "5122", "beta" : "2531", "charlie" : "1245"
}
login_status = False

def login(username, pin):
    if username.lower() in accounts:
        if accounts[username.lower()] == pin:
            print(f"selamat datang {username}")
            return True
        else:
            print(f"pin tidak sesuai")
    else:
        print(f"User {username} tidak ditemuank")

def is_pin_valid(pin):
    if not(len(pin) == 4 and pin.isdigit()):
        print("Pin harus terdiri dari 4 angka")
        return False
    return True

def display_accounts():
    cencored_values = (map(lambda x : x.replace("1", "*").replace("2", "*").replace("3", "*"), accounts.values()))
    cencored_accounts = dict(zip(accounts.key(), cencored_values))
    for i, (name, password) in enumerate(cencored_accounts.value()):
        print(f"{i+1}. {name} : {password}")

while True:
    username = input("Masukkan username: ")
    pin = input("Masukkan pin: ")
    if is_pin_valid(pin):
        login_status = login(username, pin)
    if login_status:
        display_accounts()
        break