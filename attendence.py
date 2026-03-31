import pandas as pd
from datetime import datetime

# Student database with PES format IDs
students = {
    "PES2UG24AM001": "Atharvi",
    "PES2UG24AM002": "Chandana",
    "PES2UG24AM003": "Anwesha",
    
    "PES2UG24CS001": "Rahul",
    "PES2UG24CS002": "Priya",
    "PES2UG24CS003": "Amit",
    
    "PES2UG24EC001": "Sneha",
    "PES2UG24EC002": "Karan",
    "PES2UG24EC003": "Neha"
}

file = "attendance.xlsx"

try:
    df = pd.read_excel(file)
except:
    df = pd.DataFrame(columns=["ID", "Name", "Date", "Time"])

while True:
    uid = input("Scan RFID (Enter ID or 'exit'): ")

    if uid.lower() == 'exit':
        break

    if uid in students:
        name = students[uid]
        now = datetime.now()

        new_entry = {
            "ID": uid,
            "Name": name,
            "Date": now.strftime("%Y-%m-%d"),
            "Time": now.strftime("%H:%M:%S")
        }

        df = pd.concat([df, pd.DataFrame([new_entry])], ignore_index=True)
        df.to_excel(file, index=False)

        print(f"{name} attendance marked ")
    else:
        print("Invalid ID ")
        