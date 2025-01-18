class PayChatApp:
    def __init__(self):  # Constructor to initialize the class
        # Dictionary for storing user data (e.g., username and balance)
        self.users = {}

        # List for storing transaction history
        self.transactions = []

        # Dictionary for storing user messages
        self.messages = {}

    def create_account(self):
        # Prompt the user to input a username
        username = input("Enter a username for this application: ")

        # Check if the username already exists
        if username in self.users:
            print("Invalid. Username already exists. Please choose a different username.")
        else:
            # Add the new user with an initial balance of 0.0
            self.users[username] = {'balance': 0.0}
            
            # Initialize an empty list for the user's messages
            self.messages[username] = []

            print(f"Account created for {username}.")

    def view_balance(self, username):
        # Check if the username exists
        if username not in self.users:
            print("User not found. Please create an account.")
        else:
            # Retrieve and display the user's balance
            balance = self.users[username]['balance']
            print(f"{username}, your current balance is: ${balance:.2f}")

    def transfer_money(self, username):
        # Check if the username exists
        if username not in self.users:
            print("User not found. Please create an account.")
        else:
            # Prompt for the recipient's username
            recipient = input("Enter the recipient's username:")

            # Check if the recipient exists
            if recipient not in self.users:
                print("Invalid recipient. Please enter a valid username.")
            else:
                # Prompt for the transfer amount
                try:
                    amount = float(input("Enter the amount to transfer: $"))
                except ValueError:
                    print("Invalid amount. Please enter a numeric value.")
                    return

                # Check if the user has sufficient balance
                if self.users[username]['balance'] < amount:
                    print("Insufficient funds.")
                else:
                    # Deduct the amount from the sender and add it to the recipient
                    self.users[username]['balance'] -= amount
                    self.users[recipient]['balance'] += amount

                    # Record the transaction
                    self.transactions.append(
                        f"{username} transferred ${amount:.2f} to {recipient}."
                    )

                    print(f"Successfully transferred ${amount:.2f} to {recipient}.")

    def view_transactions(self):
        # Check if there are any transactions
        if not self.transactions:
            print("No transactions found.")
        else:
            # Display all transactions
            for transaction in self.transactions:
                print(transaction)

    def send_message(self, username):
        # Check if the username exists
        if username not in self.users:
            print("User not found. Please create an account.")
        else:
            # Prompt for the recipient's username
            recipient = input("Enter the recipient's username:")

            # Check if the recipient exists
            if recipient not in self.users:
                print("Invalid recipient. Please enter a valid username.")
            else:
                # Prompt for the message content
                message = input("Enter your message:")

                # Add the message to the recipient's message list
                self.messages[recipient].append(f"From {username}: {message}")
                print(f"Message sent to {recipient}.")

    def view_messages(self, username):
        # Check if the username exists
        if username not in self.users:
            print("User not found. Please create an account.")
        else:
            # Check if there are any messages for the user
            if not self.messages[username]:
                print("No messages found.")
            else:
                # Display all messages for the user
                for message in self.messages[username]:
                    print(message)

    def menu(self):
        # Main menu loop
        while True:
            print("Welcome to PayChat!")
            print("\nPayChat App Menu:")
            print("1. Create Account")
            print("2. View Balance")
            print("3. Transfer Money")
            print("4. View Transactions")
            print("5. Send Message")
            print("6. View Messages")
            print("7. Exit")

            # Prompt for menu choice
            choice = input("Enter your choice (1-7): ")

            if choice == '1':
                # Call create_account method
                self.create_account()
            elif choice == '2':
                # Call view_balance method
                username = input("Enter your username: ")
                self.view_balance(username)
            elif choice == '3':
                # Call transfer_money method
                username = input("Enter your username: ")
                self.transfer_money(username)
            elif choice == '4':
                # Call view_transactions method
                self.view_transactions()
            elif choice == '5':
                # Call send_message method
                username = input("Enter your username: ")
                self.send_message(username)
            elif choice == '6':
                # Call view_messages method
                username = input("Enter your username: ")
                self.view_messages(username)
            elif choice == '7':
                # Exit the application
                print("Exiting PayChat. Goodbye!")
                break
            else:
                # Handle invalid menu choice
                print("Invalid choice. Please try again.")

# Entry point for the application
if __name__ == "__main__":
    app = PayChatApp()
    app.menu()
