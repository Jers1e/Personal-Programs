import os
import datetime
import openpyxl
from openpyxl.utils import get_column_letter, column_index_from_string
#* This script helps automate the pulling of data from Excel into a SQL statement
#! This is the gitversion of this script, all sensitive information has been redacted

#* This function calculates the date needed for the output SQL file in metrics_extractor
def weird_date():
   
    # Get last month's date
    today = datetime.date.today() 
    first = today.replace(day=1)
    last_month = first - datetime.timedelta(days=1)

    # Save month and year values as integer variables
    y = int(last_month.strftime("%Y"))
    lm = int(last_month.strftime("%m"))
    full_date = datetime.datetime(y, lm, 1)

    # Store into callable date string
    format_time = (full_date.strftime("'%d-%b-%y'").upper())
    file.write("Where month = " + format_time)

# Load the workbook
wb = openpyxl.load_workbook(#! Redacted - Insert workbook title here #)
inf_storage_sheet = wb['#! Redacted - Insert Sheet name here']

# Set Parameters for columns/rows we are searching 
max_row = "56"
column_let_list = [#! Redacted - Put column letters you are searching through here]
column_header_list = [#! Redacted - Put header cells you are searching for here]

# Empty lists for data to populate
cells_list = []
values_list = []
header_list = []

# Extracts list of cells with desired data
for column in column_let_list:
    c = column + max_row
    cells_list.append(c)

# print(column_let_list) #*For Troubleshooting 
# print(cells_list) #*For Troubleshooting

# Extracts values from the desired cells
for i in cells_list:
    values_list.append(inf_storage_sheet[i].value)

# Extracts column header names
for i in column_header_list:
    header_list.append(inf_storage_sheet[i].value)

# Keeps writing loop from adding extra blank line at end
end_val = len(column_header_list) - 1
add_val = 0

# Write extracted values into a file
with open(#! Redacted - put output file name here', 'w') as file:
    file.write(#! Redacted - put SQL header statement here' + '\n')
    for h, v in zip(header_list, values_list):
        if add_val != end_val:
            file.write(str(h) + ' = ' + str(v) + "," + '\n')
            add_val+=1
        else:
            file.write(str(h) + ' = ' + str(v) + '\n')
    weird_date()    

# Print additional sheet information to terminal
print(f"The current sheet is {#! Redacted}")
print(f"The maximum row is {max_row}")

