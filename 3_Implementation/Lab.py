"""Laboratory Module"""
class LaboratoryClass:
    """Laboratory Class"""

    def laboratory_menu(self):
        """Laboratory Menu"""
        print("\t\t\tWelcome to Laboratory Module")
        print("   1. Add new Laboratory Details\n")
        print("   2. View Laboratory Details\n")
        print("   3. Edit Laboratory Details\n")
        print("   4. Delete Laboratory Details\n\n")
        value = int(input("Enter your choice"))
        return value

    def get_laboratory(self):
        """Adding Laboratory Details"""
        print("\n\t\tADD LABORATORY DETAILS\n\n")
        file = open("LabDetails.txt", "at", encoding="utf-8")
        facility = input("Enter Lab Facility:- ")
        file.write("Lab Facility:- " + facility + "\n")
        cost = input("Enter Cost:- ")
        file.write("Cost:- " + cost + "\n")
        file.close()

    def view_laboratory(self):
        """Viewing Laboratory Details"""
        print("\n\t\tVIEW LABORATORY DETAILS\n\n")
        print("1. View Specific Laboratory Details\n")
        print("2. View Entire Laboratory Details\n")
        choice = int(input("Enter your choice"))
        file = open("LabDetails.txt", "rt", encoding="utf-8")
        if choice == 1:
            lookup = input("Enter Facility to view")
            file = open('LabDetails.txt', encoding="utf-8")
            content = file.readlines()
            with open("LabDetails.txt", encoding="utf-8") as myFile:
                for num, line in enumerate(myFile, 1):
                    if lookup in line:
                        print(content[num - 1])
                        print(content[num])
        else:

            print(file.read())
        file.close()

    def edit_laboratory(self):
        """Editing Laboratory Details"""
        print("\n\t\tEDIT LABORATORY DETAILS\n\n")
        search_text = input("Enter the data you want to edit:- ")
        replace_text = input("Enter the data you want to replace:- ")
        with open("LabDetails.txt", "r", encoding="utf-8") as file:
            data = file.read()
            data = data.replace(search_text, replace_text)

        with open(r"LabDetails.txt", "w", encoding="utf-8") as file:
            file.write(data)

        print("\nEdited File\n\n")
        file = open("LabDetails.txt", "rt", encoding="utf-8")

        print(file.read())
        file.close()

    def delete_laboratory(self):
        """Deleting Laboratory Details"""
        print("\n\t\tDELETE LABORATORY DETAILS\n\n")
        print("1. Delete one line")
        print("2. Delete entire content in file")
        choice = int(input("Enter your choice\n"))

        if choice == 1:
            delete_line = int(input("Enter the line which you want to delete"))

            try:
                with open('LabDetails.txt', 'r', encoding="utf-8") as file_r:

                    lines = file_r.readlines()

                    ptr = 1

                    with open('LabDetails.txt', 'w', encoding="utf-8") as file_w:
                        for line in lines:

                            if ptr != delete_line:
                                file_w.write(line)
                            ptr += 1
                print("Deleted")

            except Exception as exep:
                print("Oops! something error", exep)

        else:

            file = open('LabDetails.txt', 'r+', encoding="utf-8")
            file.truncate(0)



