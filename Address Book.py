import os


# A class to create a person and store data to that specific person
class person:
    def __init__(self, first, last, phone):
        self.first = first
        self.last = last
        self.phone = phone

    # function to display/print full name
    def full_name(self):
        return f'{self.first} {self.last}'

    # converts object to strings
    def __str__(self):
        return f'{self.first} {self.last} - {self.phone}'


contacts = list()

# checks to see if file already exists or needs to be created
if os.path.isfile('contacts.csv'):
    with open('contacts.csv') as file:
        csv_file = file.readlines()
        for contact_line in csv_file:
            contact_data = contact_line.rstrip().split(',')
            contact = person(contact_data[0], contact_data[1], contact_data[2])
            contacts.append(contact)

user_input = ''
print('Welcome to the address book application')

# while loop to give user a list of options
while user_input != '4':
    print('\nPlease select an option: '
          '\n Enter 1 - Create a contact'
          '\n Enter 2 - Display contacts'
          '\n Enter 3 - Search contacts'
          '\n Enter 4 - Exit')
    user_input = input('Enter selection: ')

    # created a conditional check to direct person to desired option
    if user_input == '1':
        print('\nEnter your contact\'s information')

        first_name = input('First name = ')
        last_name = input('Last name = ')
        phone_number = input('Phone number = ')

        print('Your contact information has been stored')

        our_contact = person(first_name, last_name, phone_number)
        contacts.append(our_contact)

    elif user_input == '4':
        print('\nGoodbye!')
        break

    elif user_input == '2':
        for contact in contacts:
            print(contact)

    elif user_input == '3':
        contact_search = input('\n Enter contact\'s name to search: ').capitalize()
        for contact in contacts:
            if contact_search in contact.full_name():
                print(contact)

# creates and adds users contacts into a csv format file
with open('contacts.csv', 'w') as file:
    for contact in contacts:
        file.write(f'{contact.first}, {contact.last}, {contact.phone}\n')
