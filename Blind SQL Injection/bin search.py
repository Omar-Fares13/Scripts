def cond(c, i):
    s = "kaztrfaker2372"
    # Compare characters using their ASCII values
    return s[i] <= c

for i in range(0, 14):
    l = ord('0')  # Convert '0' to its ASCII value (48)
    r = ord('z')  # Convert 'z' to its ASCII value (122)
    
    while l < r:
        mid = (l + r) // 2  # Calculate the midpoint
        mid_char = chr(mid)  # Convert midpoint back to character
        
        if cond(mid_char, i):  # Use the character in the condition
            r = mid  # Adjust the upper bound to avoid skipping 'z'
        else:
            l = mid + 1  # Adjust the lower bound
    
    print(chr(r))  # Print the character corresponding to the final value of r
