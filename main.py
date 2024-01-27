import phonenumbers
number="+917702269640"

from phonenumbers import geocoder
ch_nmber=phonenumbers.parse(number, "CH")
print(geocoder.description_for_number(ch_nmber,"en"))
# Getting carrier of a phone number
from phonenumbers import carrier
# Getting region information 
service_nmber= phonenumbers.parse(number,"RO")
print(carrier.name_for_number(service_nmber, "en"))
from phonenumbers import timezone

# Parsing String to Phone number
phoneNumber = phonenumbers.parse(number)

# Pass the parsed phone number in below function
timeZone = timezone.time_zones_for_number(phoneNumber)

# It print the timezone of a phonenumber
print(timeZone)