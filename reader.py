import csv
import os.path


def read(filename):
    data_list = []
    with open(filename, 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',')
        for row in reader:
            if row["product"] == "pink morsel":
                data_list.append(row)
        return data_list

def edit_csv(data):
    data_list = []
    for row in data:
        dict_csv = {"Sales": float(row["quantity"]) * float(row["price"][1:]), "Date": row["date"], "Region": row["region"]}
        data_list.append(dict_csv)
    return data_list


def write(filename, data):
    with open(filename, 'a', newline='') as csvfile:
        fieldnames = ['Sales', 'Date', 'Region']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        if os.path.getsize(filename) == 0:
            writer.writeheader()
        for row in data:
            writer.writerow(row)
        print("Written successfully")

soul_food = read(os.path.expanduser('~/Dev/misc-projects/quantium-starter-repo/data/daily_sales_data_2.csv'))
soul_food_formatted = edit_csv(soul_food)
write(os.path.expanduser('~/Dev/misc-projects/quantium-starter-repo/data/pink_morsel_total.csv'), soul_food_formatted)


