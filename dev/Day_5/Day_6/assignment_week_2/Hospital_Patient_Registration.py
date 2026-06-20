patients = {}

n = int(input("Enter number of patients: "))

for i in range(n):
    patient_id = int(input("Enter Patient ID: "))
    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    disease = input("Enter Disease: ")

    patients[patient_id] = {
        "Name": name,
        "Age": age,
        "Disease": disease
    }

search_id = int(input("\nEnter Patient ID to search: "))

if search_id in patients:
    print("Patient Details:")
    print("Name:", patients[search_id]["Name"])
    print("Age:", patients[search_id]["Age"])
    print("Disease:", patients[search_id]["Disease"])
else:
    print("Patient not found.")