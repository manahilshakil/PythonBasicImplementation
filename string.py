email = "manahil@gmail.com"
old_domain = "gmail.com"
new_domain="hotmail.com"

def email_replacement(email,old_domain,new_domain):
    if email.endswith(old_domain):
     c = len(email)
     new = email[:-c]+email[-c:].replace(old_domain,new_domain)
     return new
    return email

print(email_replacement(email,old_domain,new_domain))

def username_replacement(username,old_year,new_year):
    if "," + old_year in username:
        index = username.index("," + old_year)
        new_username = username[:index] + "," + new_year
        return new_username
    return username

print(username_replacement("Manahil,2004","2004","2023"))


def username(last_name, birth_year):
    return ("{}{}".format(last_name[0:3], birth_year))

print(username("Ivanov", "1985"))
print(username("Rodríguez", "2000"))


def convert_weight(ounces):
    # Conversion formula: 1 pound = 16 ounces
    pounds = ounces / 16
    result = "{} ounces equals {:.2f} pounds".format(ounces, pounds)
    return result

print(convert_weight(12))  # Should be: 12 ounces equals 0.75 pounds