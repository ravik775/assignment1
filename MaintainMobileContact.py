import gspread


gc = gspread.service_account(filename="credentials.json")
sh = gc.open_by_key('1YfQEcgK2L-wPP5mgQOSdoPNUBqYIvF0ieDC7KQ7ORos')
worksheet = sh.sheet1

allRecords = worksheet.get_all_records() # get_all_values

print ("\nFile Contents")
print("Row : Name  - Country - Mobile Number\n")
for index, rec in enumerate(allRecords):
    print("%s : %s - %s - %s "% (index+1, rec['Name'], rec['Country'], rec['Mobile Number']))

choise = input("Do you want to Edit exising row (Y/N) :")
if choise in ['Y', 'y']:
    row = input("Enter Row number : ")
    if row.isdigit() and int(row) and int(row) < len(allRecords):
        row = int(row)
        mobile = input("Enter Mobile Number : ")
        if mobile.isdigit() and int(mobile):
            mobile = int(mobile)
            worksheet.update_cell(row, 3, mobile)
        else:
            print("Please enter a valid Mobile number")
    else:
        print("Entered row is not valid")

choise = input("Do you want to Add Data (Y/N) :")
if choise in ['Y', 'y']:
    name = input("Enter Name: ")
    country = input("Enter Country: ")
    mobile = input("Enter Mobile Number : ")
    if name and country and int(mobile):
        worksheet.append_row((name, country, mobile))
    else:
        print("Entered valid data for row to be added")

