import tkinter as tk
from tkinter import ttk, messagebox
from main import PayChatApp

class PayChatGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("PayChat Application")
        self.root.geometry("800x600")
        self.app = PayChatApp()
        
        # Configure style
        style = ttk.Style()
        style.configure("TButton", padding=6, relief="flat", background="#2196F3")
        style.configure("TLabel", padding=6, font=('Helvetica', 10))
        style.configure("TEntry", padding=6)
        
        # Create main container
        self.main_frame = ttk.Frame(root, padding="10")
        self.main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Create notebook for tabs
        self.notebook = ttk.Notebook(self.main_frame)
        self.notebook.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Create tabs
        self.create_account_tab()
        self.create_transfer_tab()
        self.create_messages_tab()
        
        # Configure grid weights
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)
        self.main_frame.columnconfigure(0, weight=1)
        self.main_frame.rowconfigure(0, weight=1)

    def create_account_tab(self):
        account_frame = ttk.Frame(self.notebook, padding="10")
        self.notebook.add(account_frame, text="Account")
        
        # Create Account Section
        ttk.Label(account_frame, text="Create New Account", font=('Helvetica', 12, 'bold')).grid(row=0, column=0, columnspan=2, pady=10)
        
        ttk.Label(account_frame, text="Username:").grid(row=1, column=0, sticky=tk.W)
        self.username_entry = ttk.Entry(account_frame, width=30)
        self.username_entry.grid(row=1, column=1, pady=5)
        
        ttk.Button(account_frame, text="Create Account", command=self.create_account).grid(row=2, column=0, columnspan=2, pady=10)
        
        # View Balance Section
        ttk.Label(account_frame, text="View Balance", font=('Helvetica', 12, 'bold')).grid(row=3, column=0, columnspan=2, pady=10)
        
        ttk.Label(account_frame, text="Username:").grid(row=4, column=0, sticky=tk.W)
        self.balance_username_entry = ttk.Entry(account_frame, width=30)
        self.balance_username_entry.grid(row=4, column=1, pady=5)
        
        ttk.Button(account_frame, text="Check Balance", command=self.view_balance).grid(row=5, column=0, columnspan=2, pady=10)
        
        # Balance Display
        self.balance_label = ttk.Label(account_frame, text="")
        self.balance_label.grid(row=6, column=0, columnspan=2, pady=5)

    def create_transfer_tab(self):
        transfer_frame = ttk.Frame(self.notebook, padding="10")
        self.notebook.add(transfer_frame, text="Transfer")
        
        # Transfer Money Section
        ttk.Label(transfer_frame, text="Transfer Money", font=('Helvetica', 12, 'bold')).grid(row=0, column=0, columnspan=2, pady=10)
        
        ttk.Label(transfer_frame, text="From Username:").grid(row=1, column=0, sticky=tk.W)
        self.sender_entry = ttk.Entry(transfer_frame, width=30)
        self.sender_entry.grid(row=1, column=1, pady=5)
        
        ttk.Label(transfer_frame, text="To Username:").grid(row=2, column=0, sticky=tk.W)
        self.recipient_entry = ttk.Entry(transfer_frame, width=30)
        self.recipient_entry.grid(row=2, column=1, pady=5)
        
        ttk.Label(transfer_frame, text="Amount ($):").grid(row=3, column=0, sticky=tk.W)
        self.amount_entry = ttk.Entry(transfer_frame, width=30)
        self.amount_entry.grid(row=3, column=1, pady=5)
        
        ttk.Button(transfer_frame, text="Transfer", command=self.transfer_money).grid(row=4, column=0, columnspan=2, pady=10)
        
        # Transaction History
        ttk.Label(transfer_frame, text="Transaction History", font=('Helvetica', 12, 'bold')).grid(row=5, column=0, columnspan=2, pady=10)
        
        # Create a text widget for transaction history
        self.transaction_text = tk.Text(transfer_frame, height=10, width=50)
        self.transaction_text.grid(row=6, column=0, columnspan=2, pady=5)
        
        # Add scrollbar
        scrollbar = ttk.Scrollbar(transfer_frame, orient="vertical", command=self.transaction_text.yview)
        scrollbar.grid(row=6, column=2, sticky=(tk.N, tk.S))
        self.transaction_text.configure(yscrollcommand=scrollbar.set)
        
        # Button to refresh transaction history
        ttk.Button(transfer_frame, text="Refresh History", command=self.refresh_transactions).grid(row=7, column=0, columnspan=2, pady=10)

    def create_messages_tab(self):
        messages_frame = ttk.Frame(self.notebook, padding="10")
        self.notebook.add(messages_frame, text="Messages")
        
        # Send Message Section
        ttk.Label(messages_frame, text="Send Message", font=('Helvetica', 12, 'bold')).grid(row=0, column=0, columnspan=2, pady=10)
        
        ttk.Label(messages_frame, text="From Username:").grid(row=1, column=0, sticky=tk.W)
        self.message_sender_entry = ttk.Entry(messages_frame, width=30)
        self.message_sender_entry.grid(row=1, column=1, pady=5)
        
        ttk.Label(messages_frame, text="To Username:").grid(row=2, column=0, sticky=tk.W)
        self.message_recipient_entry = ttk.Entry(messages_frame, width=30)
        self.message_recipient_entry.grid(row=2, column=1, pady=5)
        
        ttk.Label(messages_frame, text="Message:").grid(row=3, column=0, sticky=tk.W)
        self.message_text = tk.Text(messages_frame, height=4, width=30)
        self.message_text.grid(row=3, column=1, pady=5)
        
        ttk.Button(messages_frame, text="Send Message", command=self.send_message).grid(row=4, column=0, columnspan=2, pady=10)
        
        # View Messages Section
        ttk.Label(messages_frame, text="View Messages", font=('Helvetica', 12, 'bold')).grid(row=5, column=0, columnspan=2, pady=10)
        
        ttk.Label(messages_frame, text="Username:").grid(row=6, column=0, sticky=tk.W)
        self.view_messages_username_entry = ttk.Entry(messages_frame, width=30)
        self.view_messages_username_entry.grid(row=6, column=1, pady=5)
        
        ttk.Button(messages_frame, text="View Messages", command=self.view_messages).grid(row=7, column=0, columnspan=2, pady=10)
        
        # Messages Display
        self.messages_text = tk.Text(messages_frame, height=10, width=50)
        self.messages_text.grid(row=8, column=0, columnspan=2, pady=5)
        
        # Add scrollbar for messages
        messages_scrollbar = ttk.Scrollbar(messages_frame, orient="vertical", command=self.messages_text.yview)
        messages_scrollbar.grid(row=8, column=2, sticky=(tk.N, tk.S))
        self.messages_text.configure(yscrollcommand=messages_scrollbar.set)

    def create_account(self):
        username = self.username_entry.get()
        if not username:
            messagebox.showerror("Error", "Please enter a username")
            return
            
        if username in self.app.users:
            messagebox.showerror("Error", "Username already exists")
            return
            
        self.app.users[username] = {'balance': 0.0}
        self.app.messages[username] = []
        messagebox.showinfo("Success", f"Account created for {username}")
        self.username_entry.delete(0, tk.END)

    def view_balance(self):
        username = self.balance_username_entry.get()
        if not username:
            messagebox.showerror("Error", "Please enter a username")
            return
            
        if username not in self.app.users:
            messagebox.showerror("Error", "User not found")
            return
            
        balance = self.app.users[username]['balance']
        self.balance_label.config(text=f"Current Balance: ${balance:.2f}")

    def transfer_money(self):
        sender = self.sender_entry.get()
        recipient = self.recipient_entry.get()
        try:
            amount = float(self.amount_entry.get())
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid amount")
            return
            
        if not sender or not recipient:
            messagebox.showerror("Error", "Please enter both usernames")
            return
            
        if sender not in self.app.users or recipient not in self.app.users:
            messagebox.showerror("Error", "One or both users not found")
            return
            
        if self.app.users[sender]['balance'] < amount:
            messagebox.showerror("Error", "Insufficient funds")
            return
            
        self.app.users[sender]['balance'] -= amount
        self.app.users[recipient]['balance'] += amount
        self.app.transactions.append(f"{sender} transferred ${amount:.2f} to {recipient}")
        
        messagebox.showinfo("Success", f"Successfully transferred ${amount:.2f} to {recipient}")
        self.refresh_transactions()
        
        # Clear entries
        self.sender_entry.delete(0, tk.END)
        self.recipient_entry.delete(0, tk.END)
        self.amount_entry.delete(0, tk.END)

    def refresh_transactions(self):
        self.transaction_text.delete(1.0, tk.END)
        for transaction in self.app.transactions:
            self.transaction_text.insert(tk.END, transaction + "\n")

    def send_message(self):
        sender = self.message_sender_entry.get()
        recipient = self.message_recipient_entry.get()
        message = self.message_text.get("1.0", tk.END).strip()
        
        if not sender or not recipient or not message:
            messagebox.showerror("Error", "Please fill in all fields")
            return
            
        if sender not in self.app.users or recipient not in self.app.users:
            messagebox.showerror("Error", "One or both users not found")
            return
            
        self.app.messages[recipient].append(f"From {sender}: {message}")
        messagebox.showinfo("Success", f"Message sent to {recipient}")
        
        # Clear entries
        self.message_sender_entry.delete(0, tk.END)
        self.message_recipient_entry.delete(0, tk.END)
        self.message_text.delete("1.0", tk.END)

    def view_messages(self):
        username = self.view_messages_username_entry.get()
        if not username:
            messagebox.showerror("Error", "Please enter a username")
            return
            
        if username not in self.app.users:
            messagebox.showerror("Error", "User not found")
            return
            
        self.messages_text.delete(1.0, tk.END)
        if not self.app.messages[username]:
            self.messages_text.insert(tk.END, "No messages found")
        else:
            for message in self.app.messages[username]:
                self.messages_text.insert(tk.END, message + "\n")

if __name__ == "__main__":
    root = tk.Tk()
    app = PayChatGUI(root)
    root.mainloop()