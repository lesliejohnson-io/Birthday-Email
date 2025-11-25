import smtplib
from datetime import datetime
import random
import pandas as pd

today = datetime.now()
today_tuple = (today.month, today.day)

MY_EMAIL = "youremail.gmail.com"
PASSWORD = "yourpasswordhere"

data = pd.read_csv("birthdays.csv")


birthdays_dict = {(data_row.month, data_row.day): data_row for (index, data_row) in data.iterrows()}

#print(birthdays_dict)

if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    letter = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(letter) as letter_file:
        message = email_contents = letter_file.read()
        email = message.replace("[NAME]", birthday_person["name"])
        print(email)

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=birthday_person["email"],
                            msg=f"Subject: Happy Birthday!\n\n{email}")


