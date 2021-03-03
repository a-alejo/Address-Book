class person:
    def __init__(self, first, last, phone, email):
        self.first = first
        self.last = last
        self.phone = phone
        self.email = email

    def full_name(self):
        print(f'{self.first} {self.last}')

    def full_contact(self):
        print(f'{self.first} {self.last} - {self.phone} - {self.email}')


print('Welcome to the address book program\nEnter your contact\'s information')

first_name = input('First name = ')
last_name = input('Last name = ')
phone_number = input('Phone number = ')
email_address = input('Email address = ')

print('Your contact information has been stored')

our_contact = person(first_name, last_name, phone_number, email_address)
our_contact.full_contact()
