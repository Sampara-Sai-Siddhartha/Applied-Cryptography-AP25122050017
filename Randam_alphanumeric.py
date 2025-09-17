import random
import string

def generate_random_string(length, use_digits=True, use_upper=True, use_lower=True):
    # Choose subsets
    chars = ""
    if use_digits:
        chars += string.digits              # 0-9
    if use_upper:
        chars += string.ascii_uppercase     # A-Z
    if use_lower:
        chars += string.ascii_lowercase     # a-z
    
    if not chars:
        raise ValueError("No character sets selected!")
    
    # Randomly choose characters
    return ''.join(random.choice(chars) for _ in range(length))

print("Enter a length of Random aplhanumeric string to generater:")
length = int(input())
print("Random Digits Only: ", generate_random_string(length, use_upper=False, use_lower=False))
print("Random Uppercase + Digits: ", generate_random_string(length, use_lower=False))
print("Random Lowercase + Digits: ", generate_random_string(length, use_upper=False))
print("Random Mixed (All): ", generate_random_string(length))
