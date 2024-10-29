class Information:
    def __init__(self):
        print("hi")
        self.first_name = input('Enter their first name: ')
        self.last_name = input('Enter their last name: ')
        self.personal_phone = input('Enter their personal phone number: ')
        self.personal_email = input('Enter their personal email address: ')
        self.work_phone = input('Enter their work phone number: ')
        self.work_email = input('Enter their work email address: ')
        self.title = input('Enter their work title: ')
    
class Contacts:
    def __init__(self):
        self.view = 'list'
        self.contact_list = []
        self.choice = None
        self.index = None

    def __add__(self, new_contact):
        self.contact_list.append(new_contact)
        
    def add_contact(self):
        self + Information()
        self.view = 'list'

    def handle_choice(self):
        if self.choice == 'q':
            self.view = 'quit'
        elif self.choice == 'a' and self.view == 'list':
            self.view = 'add'

    def show_list(self):
        print()
        if len(self.contact_list) == 0:
            self.choice = input('(A)dd a new contact \n(Q)uit \n> ').lower()
        else:
            self.view = 'quit'
        self.handle_choice()

    def show_info(self):
        pass
    
    def add_contact(self):
        pass

    def display(self):
        while True:
            if self.view == 'list':
                self.show_list()
            elif self.view == 'info':
                self.show_info()
            elif self.view == 'add':
                #print()
                self.add_contact()
            elif self.view == 'quit':
                print('\nClosing the contact list...\n')
                break
    


contacts = Contacts()
contacts.display()