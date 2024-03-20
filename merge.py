import pandas as pd
import os
import re

def clean_phone_number(phone):
    phone = str(phone)
    if phone.endswith(".0"):
        phone = phone[:-2]
    if len(phone) == 12:
        phone = phone[2:]
    return phone

def replace_6_digit_numbers(city):
    if re.match(r'^\d{6}$', str(city)):
        return 'Other'
    if re.match(r'^\d{10}$', str(city)):
        return 'Other'
    return city

def replace_parganas(city):
    if "24 Parganas" in city:
        return "Parganas"
    return city

def merge_csv_files(folder_path, output_file):
    merged_data = pd.DataFrame()

    for filename in os.listdir(folder_path):
        if filename.endswith(".csv"):
            file_path = os.path.join(folder_path, filename)
            data = pd.read_csv(file_path)
            
            data = data.apply(lambda x: x.str.strip() if x.dtype == "object" else x)
            
            data['phone'] = data['phone'].apply(clean_phone_number)
            data['email'] = data['email'].str.lower()
            data['name'] = data['name'].str.title()
            data['city'] = data['city'].str.title()
            data['city'] = data['city'].replace('0', 'Other')
            data['city'] = data['city'].replace('-', 'Other')
            data['city'] = data['city'].replace('#Name?', 'Other')
            data['city'] = data['city'].apply(replace_parganas)
            data['city'] = data['city'].apply(replace_6_digit_numbers)
            merged_data = merged_data._append(data, ignore_index=True)

    merged_data.drop_duplicates(subset='email', inplace=True)
    merged_data = merged_data.sort_values(by='city')
    merged_data.to_csv(output_file, index=False)
    print("Merged data saved to", output_file)

folder_path = "new"
output_file = "new_data.csv"

merge_csv_files(folder_path, output_file)
