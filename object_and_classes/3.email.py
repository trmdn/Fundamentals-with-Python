class Email:
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"


emails_object = []
command = input()

while command != "Stop":
    sender, receiver, content = command.split()
    email_info = Email(sender, receiver, content)
    emails_object.append(email_info)

indexes = [int(index) for index in input().split()]

for index in indexes:
    emails_object.append(index)

for current_mail in emails_object:
    print(current_mail.get_info())
