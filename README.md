# RFID-Based Attendance System (Software Version)

## Overview

This project implements an RFID-based attendance system using Python. It automates the process of marking attendance by identifying students through their unique RFID IDs and storing the data in an Excel file.

---

## Features

* Automatic attendance marking
* Records date and time of each entry
* Validates student IDs
* Displays output in terminal
* Stores data in Excel format

---

## Technologies Used

* Python
* Pandas
* OpenPyXL
* Excel

---

## Working Principle

1. The user scans an RFID card or enters a UID manually.
2. The system checks whether the UID exists in the predefined student database.
3. If the UID is valid, attendance is recorded with date and time.
4. The data is stored in an Excel file.
5. If the UID is invalid, an error message is displayed.

---

## Output

### Terminal

* Displays attendance status messages
* Indicates whether the ID is valid or invalid

### Excel File

The following details are stored:

* Student Name
* UID
* Date
* Time

---

## How to Run

1. Install required libraries:

   ```
   pip install pandas openpyxl
   ```

2. Run the program:

   ```
   python attendance.py
   ```

---

## Project Structure

* attendance.py : Main program file
* attendance.xlsx : Attendance data file

---

## Conclusion

The system provides an efficient method for recording attendance and reduces manual errors. It can be extended with graphical user interfaces, database integration, or real-time RFID hardware.

---

## Authors

* Anwesha
* Atharvi
