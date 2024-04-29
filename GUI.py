import tkinter as tk
from tkinter import simpledialog, messagebox

class BankSystemApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Bank of America")
        self.create_widgets()

        # Example: A dictionary to store username-password pairs (for demonstration)
        self.user_credentials = {
            "user1": "password1",
            "user2": "password2"
        }

        # Example: Initialize account balance (for demonstration)
        self.account_balance = {}

    def create_widgets(self):
        # Welcome label
        welcome_label = tk.Label(self.root, text="Welcome to Bank of America!!!", font=("Helvetica", 16))
        welcome_label.pack(pady=20)

        # Username and password entry fields
        self.username_entry = tk.Entry(self.root, width=20)
        self.username_entry.insert(0, "Enter username")
        self.username_entry.pack()

        self.password_entry = tk.Entry(self.root, width=20, show="*")
        self.password_entry.insert(0, "Enter password")
        self.password_entry.pack()

        # Login button
        login_button = tk.Button(self.root, text="Login", command=self.login)
        login_button.pack()

        # Create Account button
        create_account_button = tk.Button(self.root, text="Create an Account", command=self.create_account)
        create_account_button.pack()

        # Deposit button
        deposit_button = tk.Button(self.root, text="Deposit", command=self.deposit)
        deposit_button.pack()

        # Withdraw button
        withdraw_button = tk.Button(self.root, text="Withdraw", command=self.withdraw)
        withdraw_button.pack()

        # Modify Account button (placeholder)
        modify_account_button = tk.Button(self.root, text="Modify Account", command=self.modify_account)
        modify_account_button.pack()

        # Logout button
        logout_button = tk.Button(self.root, text="Logout", command=self.logout)
        logout_button.pack()

    def login(self):
        # Logic for login (similar to previous version)
        pass

    def create_account(self):
        # Get account name and PIN from user input
        username = self.username_entry.get()
        password = self.password_entry.get()

        if username not in self.user_credentials:
            self.user_credentials[username] = password
            self.account_balance[username] = 0
            messagebox.showinfo("Account Created", "Account successfully created!")
        else:
            messagebox.showerror("Account Creation Failed", "Username already exists. Please choose a different username.")

    def deposit(self):
        # Get logged-in user's account name
        account_name = self.username_entry.get()

        # Get deposit amount from user input
        deposit_amount = simpledialog.askfloat("Deposit", "Enter the deposit amount:")
        if deposit_amount:
            self.account_balance[account_name] += deposit_amount
            messagebox.showinfo("Deposit", f"Deposit of ${deposit_amount:.2f} successful!")
        else:
            messagebox.showerror("Error", "Invalid deposit amount. Please enter a valid number.")

    def modify_account(self):
        # Placeholder for modifying account (you can add more details here)
        pass

    def withdraw(self):
        # Get logged-in user's account name
        account_name = self.username_entry.get()

        # Get withdrawal amount from user input
        withdrawal_amount = simpledialog.askfloat("Withdraw", "Enter the withdrawal amount:")
        if withdrawal_amount and self.account_balance[account_name] >= withdrawal_amount:
            self.account_balance[account_name] -= withdrawal_amount
            messagebox.showinfo("Withdrawal", f"Withdrawal of ${withdrawal_amount:.2f} successful!")
        else:
            messagebox.showerror("Error", "Insufficient balance or invalid withdrawal amount.")

    def logout(self):
        # Clear session data and return to login screen
        self.username_entry.delete(0, tk.END)
        self.password_entry.delete(0, tk.END)
        self.create_widgets()

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = BankSystemApp()
    app.run()


