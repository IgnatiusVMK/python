import phonenumbers
from phonenumbers import geocoder

phone_number1 = phonenumbers.parse("+25479088484")

print("\n Phone numbers location \n")
print(geocoder.description_for_number(phone_number1,"en"));