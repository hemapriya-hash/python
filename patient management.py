class PatientManagement:
def init (self):
self.patients = {}
def add_patient(self):
pid = input("Enter Patient ID: ")
name = input("Enter Name: ")
age = input("Enter Age: ")
disease = input("Enter Disease: ")
self.patients[pid] = {
"Name": name,
"Age": age,
"Disease": disease
}
print("Patient Added Successfully")
def view_patients(self):
if not self.patients:
print("No Patient Records Found")
else:
print("\nPatient Records")
print(" ")
for pid, details in self.patients.items():
print("ID:", pid,
"Name:", details["Name"],
"Age:", details["Age"],
"Disease:", details["Disease"])
def search_patient(self):
pid = input("Enter Patient ID: ")
if pid in self.patients:
print("\nRecord Found")
print("ID:", pid)
print("Name:", self.patients[pid]["Name"])
print("Age:", self.patients[pid]["Age"])
print("Disease:", self.patients[pid]["Disease"])
else:
print("Patient Not Found")
def save_data(self):
file = open("patients.txt", "w")
for pid, details in self.patients.items():
file.write(pid + "," +
details["Name"] + "," +
details["Age"] + "," +
details["Disease"] + "\n")
file.close()
def load_data(self):
try:
file = open("patients.txt", "r")
for line in file:
pid, name, age, disease = line.strip().split(",")
self.patients[pid] = {
"Name": name,
"Age": age,
"Disease": disease
}
file.close()
except FileNotFoundError:
print("No Previous Records Found")
system = PatientManagement()
system.load_data()
while True:
print("\n===== PATIENT MANAGEMENT SYSTEM =====")
print("1. Add Patient")
print("2. View Patients")
print("3. Search Patient")
print("4. Exit")
choice = input("Enter Choice: ")
if choice == "1":
system.add_patient()
elif choice == "2":
system.view_patients()
elif choice == "3":
system.search_patient()
elif choice == "4":
system.save_data()
print("Data Saved Successfully")
print("Thank You")
break
else:
print("Invalid Choice")
