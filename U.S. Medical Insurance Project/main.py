import csv

ages = []
sexes = []
bmis = []
children = []
smokers = []
regions = []
charges = []

with open("insurance.csv") as insurance_file:
    insurance_data = csv.DictReader(insurance_file)
    for row in insurance_data:
        ages.append(int(row['age']))
        sexes.append(row['sex'])
        bmis.append(float(row['bmi']))
        children.append(int(row['children']))
        smokers.append(row['smoker'])
        regions.append(row['region'])
        charges.append(float(row['charges']))

def calculate_average(data):
    return sum(data) / len(data)

def show_average_age():
    average_age = calculate_average(ages)
    print("Average age:", average_age)

def show_average_bmi():
    average_bmi = calculate_average(bmis)
    print("Average BMI:", average_bmi)

def show_smoker_statistics():
    num_smokers = smokers.count('yes')
    num_non_smokers = smokers.count('no')
    print("Number of smokers:", num_smokers)
    print("Number of non-smokers:", num_non_smokers)

def show_average_charges_by_smoking_status():
    smoker_charges = [charges[i] for i in range(len(charges)) if smokers[i] == 'yes']
    non_smoker_charges = [charges[i] for i in range(len(charges)) if smokers[i] == 'no']
    average_smoker_charges = calculate_average(smoker_charges)
    average_non_smoker_charges = calculate_average(non_smoker_charges)
    print("Average charges for smokers:", average_smoker_charges)
    print("Average charges for non-smokers:", average_non_smoker_charges)

def show_highest_average_region():
    region_charges = {}
    for i in range(len(regions)):
        if regions[i] not in region_charges:
            region_charges[regions[i]] = []
        region_charges[regions[i]].append(charges[i])

    average_region_charges = {region: calculate_average(charges) for region, charges in region_charges.items()}
    highest_average_region = max(average_region_charges, key=average_region_charges.get)
    print("Region with highest average charges:", highest_average_region)
    print("Average charges in that region:", average_region_charges[highest_average_region])

def main():
    while True:
        print("\nChoose an option:")
        print("1. Show average age")
        print("2. Show average BMI")
        print("3. Show smoker statistics")
        print("4. Show average charges by smoking status")
        print("5. Show region with highest average charges")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            show_average_age()
        elif choice == '2':
            show_average_bmi()
        elif choice == '3':
            show_smoker_statistics()
        elif choice == '4':
            show_average_charges_by_smoking_status()
        elif choice == '5':
            show_highest_average_region()
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
