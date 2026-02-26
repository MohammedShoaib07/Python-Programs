class Hospital:
    
    def __init__(self, total_beds):
        self.total_beds = total_beds
        self.available_beds = total_beds
        self.patients = {}   # Dictionary to store patient name and bed number

    def allocate_bed(self):
        if self.available_beds > 0:
            name = input("Enter patient name: ")
            if name in self.patients:
                print("Patient already admitted!")
            else:
                bed_number = self.total_beds - self.available_beds + 1
                self.patients[name] = bed_number
                self.available_beds -= 1
                print(f"Bed {bed_number} allocated to {name}")
        else:
            print("No beds available!")

    def discharge_patient(self):
        name = input("Enter patient name to discharge: ")
        if name in self.patients:
            bed_number = self.patients.pop(name)
            self.available_beds += 1
            print(f"Patient {name} discharged from Bed {bed_number}")
        else:
            print("Patient not found!")

    def show_status(self):
        print("\nTotal Beds:", self.total_beds)
        print("Available Beds:", self.available_beds)
        print("Allocated Patients:")
        for name, bed in self.patients.items():
            print(f"{name} -> Bed {bed}")

    def divider(self):
        print("-" * 49)


# Creating object
hospital = Hospital(10)

while True:
    hospital.divider()
    print("\nHospital Bed Allocation System ---")
    print("1. Allocate Bed")
    print("2. Discharge Patient")
    print("3. Show Status")
    print("4. Exit")
    hospital.divider()


    choice = input("Enter your choice: ")
    hospital.divider()


    if choice == '1':
        hospital.allocate_bed()
    elif choice == '2':
        hospital.discharge_patient()
    elif choice == '3':
        hospital.show_status()
    elif choice == '4':
        print("byeeeee")
        break
    else:
        print("Invalid choice!")