balance = 5000   # starting balance
correct_pin = "1234"

def verify_pin(pin):
    return pin == correct_pin

def check_balance():
    return balance

def deposit(amount):
    global balance

    if amount <= 0:
        return False, "Invalid deposit amount!"

    balance += amount
    return True, f"Deposit successful. New Balance: ₹{balance}"

def withdraw(amount):
    global balance
    
    if amount <= 0:
        return False, "Invalid withdrawal amount!"

    if amount > balance:
        return False, "Insufficient balance!"

    balance -= amount
    return True, f"Withdrawal successful. Remaining Balance: ₹{balance}"
