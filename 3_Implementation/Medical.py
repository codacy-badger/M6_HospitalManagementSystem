"""Medicine Module"""
class MedicineClass:
    """Medicine Class"""

    def medicine_menu(self):
        """Medicine Menu"""
        print("\t\t\tWelcome to Medical Module")
        print("   1. Add new Medical Details\n")
        print("   2. View Medical Details\n")
        print("   3. Edit Medical Details\n")
        print("   4. Delete Medical Details\n\n")
        value = int(input("Enter your choice"))
        return value


    def get_medicine(self):
        """Adding Medicine Details"""
        print("\n\t\tADD MEDICINE DETAILS\n\n")
        file = open("MedicineDetails.txt", "at", encoding="utf-8")
        name = input("Enter Name:- ")
        file.write("Name:- " + name + "\n")
        company = input("Enter Company:- ")
        file.write("Company:- " + company + "\n")
        exp_date = input("Enter Exp-Date:- ")
        file.write("Exp-Date:- " + exp_date + "\n")
        cost = input("Enter Cost:- ")
        file.write("Cost:- " + cost + "\n")
        count = input("Enter No. of Units:- ")
        file.write("No. of Units:- " + count + "\n")
        file.close()

    def view_medicine(self):
        """Viewing Medicine Details"""
        print("\n\t\tVIEW MEDICINE DETAILS\n\n")
        print("1. View Specific Medicine Details\n")
        print("2. View Entire Medicine Details\n")
        choice = int(input("Enter your choice"))
        file = open("MedicineDetails.txt", "rt", encoding="utf-8")
        if choice == 1:
            lookup = input("Enter Medicine's Name")
            file = open('MedicineDetails.txt', encoding="utf-8")
            content = file.readlines()
            with open("MedicineDetails.txt", encoding="utf-8") as myFile:
                for num, line in enumerate(myFile, 1):
                    if lookup in line:
                        print(content[num - 1])
                        print(content[num])
                        print(content[num + 1])
                        print(content[num + 2])
                        print(content[num + 3])

        else:

            print(file.read())
        file.close()

    def edit_medicine(self):
        """Editing Medicine Details"""
        print("\n\t\tEDIT MEDICINE DETAILS\n\n")
        search_text = input("Enter the data you want to edit:- ")
        replace_text = input("Enter the data you want to replace:- ")
        with open("MedicineDetails.txt", "r", encoding="utf-8") as file:
            data = file.read()
            data = data.replace(search_text, replace_text)

        with open(r"MedicineDetails.txt", "w", encoding="utf-8") as file:
            file.write(data)

        print("\nEdited File\n\n")
        file = open("MedicineDetails.txt", "rt", encoding="utf-8")

        print(file.read())
        file.close()

    def delete_medicine(self):
        """Deleting Medicine Details"""
        print("\n\t\tDELETE MEDICINE DETAILS\n\n")
        print("1. Delete one line")
        print("2. Delete entire content in file")
        choice = int(input("Enter your choice\n"))

        if choice == 1:
            delete_line = int(input("Enter the line which you want to delete"))

            try:
                with open('MedicineDetails.txt', 'r', encoding="utf-8") as file_r:

                    lines = file_r.readlines()

                    ptr = 1

                    with open('MedicineDetails.txt', 'w', encoding="utf-8") as file_w:
                        for line in lines:

                            if ptr != delete_line:
                                file_w.write(line)
                            ptr += 1
                print("Deleted")

            except Exception as exep:
                print("Oops! something error", exep)

        else:

            file = open('MedicineDetails.txt', 'r+', encoding="utf-8")
            file.truncate(0)
