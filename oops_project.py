class chatbook:
    def __init__(self):
        self.user_name= ''
        self.password = ''
        self.loggedin = False
        self.menu()

    def menu(self):
        user_input = input(''' Welcome to chatbook! how would you like to proceed?
                           1. Press 1 to Sign Up
                           2. Press 2 to Sign in
                           3. Press 3 to write a post
                           4. Press 4 to message a friend 
                           5. Press any other key to exit the app''')
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

obj= chatbook()