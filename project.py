BEDS = 20


allocated_beds = {}  
# { bed_no : {"name": patient_name, "disease": disease} }

def available_beds():
    print("\nAvailable Beds:", end=" ")
    count = 0

    for i in range(1, BEDS + 1):
        if i not in allocated_beds:
            print(i, end=" ")
            count += 1

    if count == 0:
        print("0 Available")

    print("\n")

def allocate_bed():
    bed_no = int(input(f"Enter Bed Number (1-{BEDS}): "))

    if bed_no < 1 or bed_no > BEDS:
        print("Invalid bed number.")
        return

    if bed_no in allocated_beds:
        print("Bed already occupied.")
        return

    name = input("Enter Patient Name: ")
    disease = input("Enter Disease: ")

    allocated_beds[bed_no] = {
        "name": name,
        "disease": disease
    }

    print("Bed allocated successfully!")

def deallocate_bed():
    bed_no = int(input("Enter Bed Number to Deallocate: "))

    if bed_no in allocated_beds:
        print("Bed Deallocated Successfully!")
        print("Patient:", allocated_beds[bed_no]["name"])
        print("Disease:", allocated_beds[bed_no]["disease"])

        del allocated_beds[bed_no]
    else:
        print("Bed not found or already free.")

def display():
    if not allocated_beds:
        print("No beds are currently allocated.")
        return
    print("\nAllocated Beds\n")

    for bed_no, details in allocated_beds.items():
        print("Bed No :", bed_no)
        print("Patient:", details["name"])
        print("Disease:", details["disease"])

while True:

    available_beds()

    print("1.ALLOCATE BED")
    print("2.DEALLOCATE BED")
    print("3.VIEW ALLOCATED BEDS")
    print("4.EXIT")

    choice = int(input("ENTER THE CHOICE : "))

    if choice == 1:
        allocate_bed()

    elif choice == 2:
        deallocate_bed()

    elif choice == 3:
        display()

    elif choice == 4:
        print("Exited System!!!")
        break

    else:
        print("Invalid choice.")