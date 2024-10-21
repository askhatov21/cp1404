
def main():
    """Function ask the email from user"""
    email_to_name = {}

    while True:
        email = input("Email: ")
        if email == "":
            break

    name = get_name_from_email(email)
    confirmation = input(f"Is your name {name}? (Y/n)").lower()

    if confirmation != "y" and confirmation != "":
        name = input("Name: ")
    # Store email and name
    email_to_name[email] = name

    for email, name in email_to_name.items():
        print(f'{name} ({email})')


def get_name_from_email(email):
    """Extracts name from email address"""
    name = email.split('@')[0]
    name_parts = name.split('.')
    name = ''.join(name_parts).title()
    return name



main()