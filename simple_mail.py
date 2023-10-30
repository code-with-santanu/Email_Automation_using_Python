import smtplib
import getpass


def emailSender(sender, receiver, password, subject, msg):

    # header = 'Subject : {}'.format(subject)
    header = 'To : {}'.format(
        receiver) + "\n" + 'From : {}'.format(sender) + "\n" + 'Subject : {}'.format(subject)
    msg = header + "\n\n" + text

    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.ehlo()  # make the communication between SMTP server and gmail
        server.starttls()  # start the service
        server.login(sender, password)
        print("Successfully login")

        server.sendmail(sender, receiver, msg)
        print('Messege send successfully')


if __name__ == "__main__":

    receiver = input("Enter the receiver email: ")
    sender = input("Enter the sender email: ")

    password = getpass.getpass('Enter your password: ')

    subject = input('Enter the Subject: ')
    text = input('Enter the messege: ')
    emailSender(sender, receiver, password, subject, text)
