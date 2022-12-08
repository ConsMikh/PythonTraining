class MailSender:
    def send_mail(self, message):
        # print(f"Sending mail to {self.email}:\n {message}") # There is no error
        print(f"Sending mail message:\n{message}")


class Contact:
    all_contacts = []
    def __init__(self, name, email):
        self.name = name
        self.email = email
        Contact.all_contacts.append(self)


# Mixin multiple inheritance
class EmailableContact(Contact, MailSender):
    pass


e = EmailableContact("John Smith", "jsmith@example.net")
e.send_mail("Hello, test e-mail here")