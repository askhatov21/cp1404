def get_name_from_email(email):
    name = email.split('@')[0]  # Extract the part before '@'
    name_parts = name.split('.')  # Split based on dots (if any)
    name = ' '.join(name_parts).title()  # Join with spaces and capitalize
    return name

def main():
    email_to_name = {}

    while True:
        email = input("Email: ")
        if email == "":
            break

        # Extract name from email
        name = get_name_from_email(email)
        confirmation = input(f"Is your name {name}? (Y/n) ").lower()

        if confirmation != 'y' and confirmation != '':
            name = input("Name: ")

        # Store email and name
        email_to_name[email] = name

    # Print the emails and names
    for email, name in email_to_name.items():
        print(f"{name} ({email})")

# Run the main function
main()
