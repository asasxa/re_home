from pprint import pprint

import re
import csv

def format_name(row):
    name_items = row[0].split()
    row[0], row[1], row[2] = name_items[0], name_items[1], name_items[2] if len(name_items) > 2 else ''
    return row

def format_phone(row)
    number_phone = (row[-2])
    number_phone = re.sub(r"^8", '+7', number_phone)
    number_phone = re.sub(r"[ ()-]", "", number_phone)
    number_phone = re.sub(r"доб.", " доб. ", number_phone)
    number_phone = f"{number_phone[:2]} ({number_phone[2:5]}){number_phone[5:8]}-{number_phone[8:10]}-{number_phone[10:]}"
    row[-2] = number_phone
    return row

unique_contacts = dict()

with open("phonebook_raw.csv", encoding="utf-8") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)

for row in contacts_list[1:]:
    format_name(row)
    format_phone(row)

for row in contacts_list[1:]:
    lastname, firstname, surname = row[0], row[1], row[2]
    key = (lastname, firstname, surname)  

    if key not in unique_contacts:
        unique_contacts[key] = row[:]  
    else:
        existing_contact = unique_contacts[key]
        for i in range(len(existing_contact)):
            if existing_contact[i] == "" and row[i] != "":
                existing_contact[i] = row[i]

with open("phonebook.csv", "w", encoding="utf-8") as f:
    datawriter = csv.writer(f, delimiter=',')
    datawriter.writerows([contacts_list[0]] + list(unique_contacts.values()))
