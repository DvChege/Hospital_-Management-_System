#conditional statements
def check_number(num):
    if num > 0:
        return "Positive"
    elif num < 0:
        return "Negative"
    else:
        return "Zero"
    
    #output: "poistive", "negative", "zero"
print(check_number(10))  # Positive
print(check_number(-5))  # Negative
print(check_number(0))   # Zero    