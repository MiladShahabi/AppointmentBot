import openpyxl

# Load the Excel workbook and the specific sheet
workbook = openpyxl.load_workbook('myexcel.xlsx')
sheet = workbook['MainSheet']  # Replace 'Sheet1' with the name of your sheet, if different

# Loop through rows in the sheet and extract data
for row in sheet.iter_rows(max_row=51, values_only=True):  # Assuming 1st row contains headers
    a, telegram_id, b, x, firstname, lastname, dob, email, c, preferred_date, d, e, time_range, country_1, number_of_applicant, with_family, country_2, category, is_idcard, id_card_number, r_type, r_title, *other_fields = row


time_offer_1, time_offer_2 = time_range.split("/")
time_offer_1, time_offer_2 = time_range.split("/")

    # Now you can use these variables in your script
    # For example, if you want to print them:
print(f'''
          
booking_time_offer_1 = '{time_offer_1}'
booking_time_offer_2 = '{time_offer_2}'

booking_month_1st = 'September'
booking_month_2nd = 'October'
booking_month_3rd = 'November'

prefered_start_day = 1 # September
prefered_end_day = 30 # September
prefered_day = '{preferred_date}' # off/on

allow_channel_notifications = True # True
USER_CHAT_ID: Final = {telegram_id}  # User's Chat ID
firstname = '{firstname}' 
lastname = '{lastname}' 
dob = '{dob}' # DD.MM.YYYY 
email = '{email}' 
citizenship = "{country_1}" 
nr_applicants = '{number_of_applicant}' 
with_family_live = '{with_family}' 
family_citizenship = '{country_2}' 
residence_title = "{category}" 
currently_have_a_residence = '{is_idcard}' # If selected Extend this item should be set 'no' 
id_card_number = '{id_card_number}' 
category = "{r_type}" 
request_type = "{r_title}"

''')

    # If you have more fields, access them using the other_fields list
    # e.g., other_fields[0] will give you the third column's value for the current row

# Close the workbook
workbook.close()
