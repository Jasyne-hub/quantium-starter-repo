import csv
import os.path

DATA_PATH = "./data"
PROCESSED_DATA_PATH = "./data/pink_morsel_total.csv"

def read(filename):
    #Reads from a csv file and appends each row in the file
    #to data_list
    #Returns a list of dictionaries
    #data_list is a list of dictionaries
    data_list = []
    with open(filename, 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',')
        #Iterate through every row in the file
        for row in reader:
            #Filter by pink morsel
            if row["product"] == "pink morsel":
                #Append to data_list
                data_list.append(row)
        return data_list

def edit_csv(data_to_be_used):
    #data is a list of dictionaries
    #Edits the given data to calculate sales and filter
    #for date and region in each dictionary
    #Returns a list of dictionaries
    #data_list is a list of dictionaries
    data_list = []
    #Iterate through dictionaries in data
    for row in data_to_be_used:
        #Calculates sales and filters only date and region
        dict_csv = {"Sales": float(row["quantity"]) * float(row["price"][1:]), "Date": row["date"], "Region": row["region"]}
        #Append to data_list
        data_list.append(dict_csv)
    return data_list


def write(filename, data_to_be_used):
    #Appends data to the file, filename
    #data is a list of dictionaries
    with open(filename, 'a', newline='') as csvfile:
        fieldnames = ['Sales', 'Date', 'Region']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        #Ensure header is created only if file is empty
        if os.path.getsize(filename) == 0:
            writer.writeheader()
        for row in data_to_be_used:
            writer.writerow(row)
        #Confirm data has been written
        print("Written successfully")


files = [f'{DATA_PATH}/daily_sales_data_0.csv',
         f'{DATA_PATH}/daily_sales_data_1.csv',
         f'{DATA_PATH}/daily_sales_data_2.csv']

for file in files:
    data = read(file)
    formatted = edit_csv(data)
    write(PROCESSED_DATA_PATH, formatted)


