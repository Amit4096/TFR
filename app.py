from flask import Flask, render_template, request
import os
import re
from datetime import datetime
app = Flask(__name__)

def count_rows(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    return len(lines)



def is_valid_date_format(date_string):
    try:
        # Attempt to parse the date string using the specified format
        datetime.strptime(date_string, "%d %b %Y %H:%M:%S")
        return True  # If successful, the format is correct
    except ValueError:
        return False  # If an exception is raised, the format is incorrect
def is_valid_date_format1(date_string):
    pattern = re.compile(r'^\d{2}[A-Z]{3}\d{4}$')
    return bool(pattern.match(date_string))
    
def read_rows_from_file(file_path):
    correct_rows = []
    incorrect_rows = []
    with open(file_path, 'r') as file:
        for line in file:
            row = line.strip().split(',')

            # Validation: Check if all values in the first column are numeric
            if not all(value.strip().isdigit() and int(value.strip()) > 100 for value in row[:1]):
                incorrect_rows.append(row)
                continue
            
            # Validation: Check if all values in the second column are two-digit integers
            if not all(value.strip().isdigit() and len(value.strip()) == 2 for value in row[1:2]):
                # If the second column values are not two-digit integers, add the row to incorrect_rows
                incorrect_rows.append(row)
                continue

            if not all(value.strip() in ["OPTIDX", "OPTSTK","FUTSTK","FUTIDX"] for value in row[2:3]):
                incorrect_rows.append(row)
                continue

            # # Validation: Check if all values in the fourth column are characters only
            # if not all(value.strip().isalpha() for value in row[3:4]):
            #     incorrect_rows.append(row)
            #     continue
            if all(value.strip().isnumeric() for value in row[3:4]):
                # If the fourteenth column values are not single-digit numeric, add the row to incorrect_rows
                incorrect_rows.append(row)
                continue
            #-> contain special character
# Validation: Check if all values in the specified column have the correct date format
            if not all(is_valid_date_format1(value.strip()) for value in row[4:5]):
    # If the date format is incorrect, add the row to incorrect_rows
                incorrect_rows.append(row)
                continue

# Validation: Check if all values in the sixth column are either float or blank
            if not all(value.strip() == "" or validate_float(value.strip()) for value in row[5:6]):
    # If the sixth column values are not float or blank, add the row to incorrect_rows
                incorrect_rows.append(row)
                continue

            #-> some rows are empty

            # # Validation: Check if all values in the seventh column are either "CE" or "PE"
# # Validation: Check if all values in the seventh column are either "CE", "PE", or blank
            if not all(value.strip() in ["CE", "PE", ""] for value in row[6:7]):
    # If the seventh column values are not "CE", "PE", or blank, add the row to incorrect_rows
                incorrect_rows.append(row)
                continue

#-> some rows are empty


            # Validation: Check if all values in the ninth column are either 0 or 1
            if not all(value.strip() in ["0", "1"] for value in row[8:9]):
                # If the ninth column values are not "0" or "1", add the row to incorrect_rows
                incorrect_rows.append(row)
                continue
            if not all(value.strip() in ["0", "1"] for value in row[10:11]):
                # If the ninth column values are not "0" or "1", add the row to incorrect_rows
                incorrect_rows.append(row)
                continue
    #         # Validation: Check if all values in the eleventh column are either 0 or 1
    #         if not all(value.strip().isalnum() for value in row[7:8]):
    #             incorrect_rows.append(row)
    #             continue
            if all(value.strip().isnumeric() for value in row[7:8]):
                # If the fourteenth column values are not single-digit numeric, add the row to incorrect_rows
                incorrect_rows.append(row)
                continue
    #  #-> contain special character

            # Validation: Check if all values in the twelfth column are alphanumeric
            if not all(value.strip().isalnum() for value in row[11:12]):
                # If the twelfth column values are not alphanumeric, add the row to incorrect_rows
                incorrect_rows.append(row)
                continue

            if not all(value.strip().isnumeric() for value in row[12:13]):
                # If the fourteenth column values are not single-digit numeric, add the row to incorrect_rows
                incorrect_rows.append(row)
                continue
            # Validation: Check if all values in the fourteenth column are single-digit numeric
            if not all(value.strip().isdigit() and len(value.strip()) == 1 for value in row[13:14]):
                # If the fourteenth column values are not single-digit numeric, add the row to incorrect_rows
                incorrect_rows.append(row)
                continue

            # Validation: Check if all values in the fifteenth column are numeric
            if not all(value.strip().isnumeric() for value in row[14:15]):
                # If the fifteenth column values are not numeric, add the row to incorrect_rows
                incorrect_rows.append(row)
                continue

            # Validation: Check if all values in the sixteenth column are float
            if not all(validate_float(value.strip()) for value in row[15:16]):
                # If the sixteenth column values are not float, add the row to incorrect_rows
                incorrect_rows.append(row)
                continue

            # Validation: Check if all values in the seventeenth column are either 0 or 1
            if not all(value.strip() in ["0", "1"] for value in row[16:17]):
                # If the seventeenth column values are not "0" or "1", add the row to incorrect_rows
                incorrect_rows.append(row)
                continue

            # Validation: Check if all values in the eighteenth column are alphanumeric
            if not all(value.strip().isalnum() for value in row[17:18]):
                # If the eighteenth column values are not alphanumeric, add the row to incorrect_rows
                incorrect_rows.append(row)
                continue

            # Validation: Check if all values in the nineteenth column are alphanumeric
            if not all(value.strip().isalnum() for value in row[18:19]):
                # If the nineteenth column values are not alphanumeric, add the row to incorrect_rows
                incorrect_rows.append(row)
                continue

            # Validation: Check if all values in the twentieth column are either "OPEN" or "CLOSE"
            if not all(value.strip() in ["OPEN", "CLOSE"] for value in row[19:20]):
                # If the twentieth column values are not "OPEN" or "CLOSE", add the row to incorrect_rows
                incorrect_rows.append(row)
                continue
            if not all(value.strip() in ["UNCOVER"] for value in row[20:21]):
                # If the twentieth column values are not "OPEN" or "CLOSE", add the row to incorrect_rows
                incorrect_rows.append(row)
                continue
            if not all(value.strip() in ["Nil"] for value in row[24:25]):
                # If the twentieth column values are not "OPEN" or "CLOSE", add the row to incorrect_rows
                incorrect_rows.append(row)
                continue
            # Validation: Check if all values in the twenty-fourth column are numeric
            if not all(value.strip().replace(".", "").isdigit() and len(value.strip()) > 5 for value in row[23:24]):
                incorrect_rows.append(row)
                continue
            # Validation: Check if all values in the twenty-seventh column are alphanumeric
            if not all(value.strip().isalnum() for value in row[26:27]):
                # If the twenty-seventh column values are not alphanumeric, add the row to incorrect_rows
                incorrect_rows.append(row)
                continue
            # Validation: Check if all values in the specified column have the correct date format



            if  all(value.strip().isalnum() for value in row[21:22]):
                if all(value.strip().isnumeric() for value in row[21:22]):
                    incorrect_rows.append(row)
                    continue
            # if  all(is_valid_date_format(value.strip()) for value in row[21:23]):
            #     # If the date format is incorrect: add the row to incorrect_rows
            #     incorrect_rows.append(row)
            #     continue
            if  all(value.strip().isalnum() for value in row[22:23]):
                if all(value.strip().isnumeric() for value in row[22:23]):
                    incorrect_rows.append(row)
                    continue
            # if  all(is_valid_date_format(value.strip()) for value in row[22:24]):
            #     # If the date format is incorrect: add the row to incorrect_rows
            #     incorrect_rows.append(row)
            #     continue
            if  all(value.strip().isalnum() for value in row[25:26]):
                if all(value.strip().isnumeric() for value in row[25:26]):
                    incorrect_rows.append(row)
                    continue
            # if not all(is_valid_date_format(value.strip()) for value in row[25:27]):
            #     # If the date format is incorrect, add the row to incorrect_rows
            #     incorrect_rows.append(row)
            #     continue


            if row[27].strip() != "":
                incorrect_rows.append(row)
            if row[9].strip() != "":
                incorrect_rows.append(row)
            # Remove the 10th and 28th columns (assuming 0-based indexing)
            # if len(row) > 27 and row[27].strip() == "":
            #     del row[27]
            # if len(row) > 9 and row[9].strip() == "":
            #     del row[9]
            correct_rows.append(row)

    return correct_rows, incorrect_rows

def validate_float(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'file' not in request.files:
            return render_template('index.html', error='No file part')

        file = request.files['file']

        if file.filename == '':
            return render_template('index.html', error='No selected file')

        upload_folder = 'uploads'
        os.makedirs(upload_folder, exist_ok=True)
        file_path = os.path.join(upload_folder, file.filename)
        file.save(file_path)
        action = request.form.get('action')
        correct_rows, incorrect_rows = read_rows_from_file(file_path)
        row_count = len(correct_rows) + len(incorrect_rows)

        # Render the result on the web page
      
        if action == 'upload':
            return render_template('index.html', row_count=row_count, correct_rows=correct_rows, incorrect_rows=incorrect_rows)
        elif action == 'view':
            # Render a new page for viewing data
            return render_template('view_data.html',row_count=row_count, correct_rows=correct_rows, incorrect_rows=incorrect_rows)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(use_evalex=False, use_reloader=False, debug=True)






