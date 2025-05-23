import pandas as pd
import datetime
from datetime import datetime

class chatbook:
    __user_id = 0
    def __init__(self):
        self.__name = "Default user"
        self.id = chatbook.__user_id
        chatbook.__user_id += 1
        self.user_name= ''
        self.password = ''
        self.loggedin = False
        # self.menu()

    @staticmethod
    def get_id():
        return chatbook.__user_id
    
    @staticmethod
    def set_id(value):
        chatbook.__user_id = value
        return chatbook.__user_id


    def get_name(self):
        return self.__name
    
    def set_name(self, name):
        if isinstance(name, str):
            self.__name = name
        else:
            raise ValueError("Name must be a string.")
            self.__name = name  

    def menu(self):
        user_input = input(''' Welcome to chatbook! how would you like to proceed?
                           1. Press 1 to Sign Up
                           2. Press 2 to Sign in
                           3. Press 3 to write a post
                           4. Press 4 to message a friend 
                           5. Press any other key to exit the app --> ''')
        if user_input == '1':
            self.sign_up()
        elif user_input == '2':
            self.sign_in()
        elif user_input == '3':
            self.write_post()
        elif user_input == '4': 
            self.message_friend()
        else:
            print('Exiting the app...')
            exit()

    def sign_up(self):
        email = input('Enter your email: ')
        password = input('Set up your password here: ')
        full_name = input('Enter your full name: ')
        dob = input('Enter your date of birth (YYYY-MM-DD): ')
        bio = input('Write a short bio about yourself: ')

        self.user_name = email.split('@')[0]
        self.password = password

         # Create new user data
        new_user = pd.DataFrame({
            'email': [email],
            'password': [password],
            'full_name': [full_name],
            'dob': [dob],
            'bio': [bio]
        })
        
        try:
            users = pd.read_csv('users.csv')
            users = pd.concat([users, new_user], ignore_index=True)
        except FileNotFoundError:
            users = new_user

        users.to_csv('users.csv', index=False)
        
        print(f'\nAccount created successfully! Your username is {self.user_name}')
        print("Welcome to Chatbook, {0}!\n".format(full_name))
        self.menu()

    def sign_in(self):
        email = input('Enter your email: ')
        password = input('Enter your password: ')
    
        try:
            users = pd.read_csv('users.csv')
            # Check if credentials match
            match = users[(users['email'] == email) & (users['password'] == password)]
            if not match.empty:
                self.user_name = email.split('@')[0]
                self.loggedin = True
                print(f'Welcome back {self.user_name}!')
            else:
                print('Invalid credentials, please try again.')
        except FileNotFoundError:
            print('User database not found. Please sign up first.')
        
        print("\n")
        self.menu()

    def write_post(self):
        if self.loggedin:
            post = input('Write your post here: ')
            print(f'Post created successfully! Your post: {post}')
            print ("\n")
            self.menu()
        else:
            print('You need to sign in first.')
            print ("\n")
            self.menu()
    
    # Check if friend exists
    def message_friend(self):
        if self.loggedin:
            friend = input('Enter your friend\'s username: ')
            message = input('Enter your message: ')
            try:
                users = pd.read_csv('users.csv')
                usernames = users['email'].apply(lambda x: x.split('@')[0])
                if friend in usernames.values:
                    # Save the message to messages.csv
                    new_message = pd.DataFrame({
                        'sender': [self.user_name],
                        'receiver': [friend],
                        'message': [message],
                        'timestamp': [datetime.now().strftime("%Y-%m-%d %H:%M:%S")]
                    })

                    try:
                        messages = pd.read_csv('messages.csv')
                        messages = pd.concat([messages, new_message], ignore_index=True)
                    except FileNotFoundError:
                        messages = new_message

                    messages.to_csv('messages.csv', index=False)
                    
                    print(f'Message sent to {friend}: {message}')
                else:
                    print(f"User {friend} not found. Please check the username.")
            except FileNotFoundError:
                print('User database not found. Please sign up first.')
        else:
            print('You need to sign in first.')
        print("\n")
        self.menu()
    def view_message_feed(self):
        if self.loggedin:
            try:
                messages = pd.read_csv('messages.csv')
                user_messages = messages[messages['sender'] == self.user_name]
                if not user_messages.empty:
                    print(f"\n--- Your Sent Messages ---\n")
                    for idx, row in user_messages.iterrows():
                        print(f"To {row['receiver']} at {row['timestamp']}: {row['message']}")
                else:
                    print("\nYou have not sent any messages yet.\n")
            except FileNotFoundError:
                print("\nNo messages found.\n")
        else:
            print('You need to sign in first.')
        print("\n")
        self.menu()

object = chatbook() 