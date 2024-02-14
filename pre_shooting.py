import csv

# Initialize a dictionary to store the counts for each shooting type
shooting_num_list = [
    "HIT_SHOOTING",'NON_HIT_SHOOTING','ANIMAL_SHOOTING','OTHER_SHOOTING','UNINTENTIONAL_DISCHARGE','WARNING_SHOT'
]

# Open the CSV file and iterate over each row
with open("Sheriff_All_Shootings_-_Incident_Summary_Count_-_2010_to_Present_(Deputy_Shootings).csv", newline='') as csvfile:
    reader = csv.reader(csvfile)
    # Add the shooting type field name to the first row of the CSV
    header_row = next(reader)
    header_row.append("shooting_num")
    rows = []

    # Add the header row to the list of rows
    rows.append(header_row)
    for row in reader:
        shooting_num = 0
        # Check if the city is "LOS ANGELES"
        # if row[9] == "LOS ANGELES":
        if True:
           
            shooting_num += 1
            # Append the shooting type to the row and add the modified row to a list of rows
            row.append(shooting_num)
            rows.append(row)

output_file_name = "los_angeles_shootings.csv"


# Write the list of rows to a new CSV file with the specified name
with open(output_file_name, "w", newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(rows)
            