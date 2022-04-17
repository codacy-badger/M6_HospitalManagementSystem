"""Facility Module"""
class FacilityClass:
    """Facility Class"""

    def facility_menu(self):
        """Facility Menu"""
        print("\t\t\tWelcome to Facility Module")
        print("   1. Add new Facility Details\n")
        print("   2. View Facility Details\n")
        print("   3. Edit Facility Details\n")
        print("   4. Delete Facility Details\n\n")
        value = int(input("Enter your choice"))
        return value


    def get_facility(self):
        """Adding Facility Details"""
        print("\n\t\tADD FACILITY DETAILS\n\n")
        file = open("FacilityDetails.txt", "at", encoding="utf-8")
        facility_name = input("Enter Facility Name:- ")
        file.write("Facility Name:- " + facility_name + "\n")
        file.close()

    def view_facility(self):
        """Viewing Facility Details"""
        print("\n\t\tVIEW FACILITY DETAILS\n\n")
        print("1. View Specific Facility Details\n")
        print("2. View Entire Facility Details\n")
        choice = int(input("Enter your choice"))
        file = open("FacilityDetails.txt", "rt", encoding="utf-8")
        if choice == 1:
            lookup = input("Enter Facility to view")
            file = open('FacilityDetails.txt', encoding="utf-8")
            content = file.readlines()
            with open("FacilityDetails.txt", encoding="utf-8") as my_File:
                for num, line in enumerate(my_File, 1):
                    if lookup in line:
                        print(content[num - 1])

        else:

            print(file.read())
        file.close()

    def edit_facility(self):
        """Editing Facility Details"""
        print("\n\t\tEDIT FACILITY DETAILS\n\n")
        search_text = input("Enter the data you want to edit:- ")
        replace_text = input("Enter the data you want to replace:- ")
        with open("FacilityDetails.txt", "r", encoding="utf-8") as file:
            data = file.read()
            data = data.replace(search_text, replace_text)

        with open(r"FacilityDetails.txt", "w", encoding="utf-8") as file:
            file.write(data)

        print("\nEdited File\n\n")
        file = open("FacilityDetails.txt", "rt", encoding="utf-8")

        print(file.read())
        file.close()

    def delete_facility(self):
        """Deleting Facility Details"""
        print("\n\t\tDELETE FACILITY DETAILS\n\n")
        print("1. Delete one line")
        print("2. Delete entire content in file")
        choice = int(input("Enter your choice\n"))

        if choice == 1:
            delete_line = int(input("Enter the line which you want to delete"))

            try:
                with open('FacilityDetails.txt', 'r', encoding="utf-8") as file_r:

                    lines = file_r.readlines()

                    ptr = 1

                    with open('FacilityDetails.txt', 'w', encoding="utf-8") as file_w:
                        for line in lines:

                            if ptr != delete_line:
                                file_w.write(line)
                            ptr += 1
                    print("Deleted")

            except Exception as exep:
                print("Oops! something error", exep)

        else:

            file = open('FacilityDetails.txt', 'r+', encoding="utf-8")
            file.truncate(0)


