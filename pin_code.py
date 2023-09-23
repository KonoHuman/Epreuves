def validate_pin(pin):
    # Check if the pin contains only digits and has a length of 4 or 6
    if pin.isdigit() and (len(pin) == 4 or len(pin) == 6):
        return True
    else:
        return False

pin = "1234"
print(validate_pin(pin))
