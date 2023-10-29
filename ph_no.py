import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier

# print("Enter yr pone no (starting with '+country_code' : )")
no = input(("Enter yr pone no (starting with '+country_code'): "))

# to get country name
country = phonenumbers.parse(no, "CH")
count = geocoder.description_for_number(country, "en")
print(f"Country : {count}")
# print()

# to get service provider name
service = phonenumbers.parse(no, "RO")
serv = carrier.name_for_number(service, "en")
print(f"Service Provider : {serv}")
# print()
