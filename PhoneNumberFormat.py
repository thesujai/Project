import phonenumbers

# Get the phone number with country code as input from the user

phone_number_input = input("Enter the phone number with country code: ")

# Parse the phone number using the phonenumbers library
parsed_number = phonenumbers.parse(phone_number_input, None)

# Check if the phone number is valid
if phonenumbers.is_valid_number(parsed_number):
    # Format the phone number according to the national convention of the country
    formatted_number = phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.NATIONAL)
    print("Formatted phone number:", formatted_number)
else:
    print("Invalid phone number")
