from flask import Flask, render_template, request
from atm_logic import verify_pin, withdraw, deposit, check_balance

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    message = None

    if request.method == "POST":
        pin = request.form["pin"]

        if not verify_pin(pin):
            return render_template("index.html", message="❌ Incorrect PIN!")

        action = request.form["action"]

        # Deposit
        if action == "deposit":
            amount = int(request.form["amount"])
            success, msg = deposit(amount)
            message = msg

        # Withdraw
        elif action == "withdraw":
            amount = int(request.form["amount"])
            success, msg = withdraw(amount)
            message = msg

        # Check balance
        elif action == "balance":
            bal = check_balance()
            message = f"💰 Your Current Balance is: ₹{bal}"

    return render_template("index.html", message=message)

if __name__ == "__main__":
    app.run(debug=True)
