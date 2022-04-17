""" Staff Module"""
class StaffClass:
    """Staff Class"""

    def staff_menu(self):
        """Staff Menu"""
        print("\t\t\tWelcome to Staff Module")
        print("   1. Add new Staff Details\n")
        print("   2. View Staff Details\n")
        print("   3. Edit Staff Details\n")
        print("   4. Delete Staff Details\n\n")
        value = int(input("Enter your choice"))
        return value


    def get_staff(self):
        """Adding Staff Details"""
        print("\n\t\tADD STAFF DETAILS\n\n")
        file = open("StaffDetails.txt", "at", encoding="utf-8")
        staff_id = input("Enter staff_id:- ")
        file.write("Staff ID:- " + staff_id + "\n")
        name = input("Enter Name:- ")
        file.write("Name:- " + name + "\n")
        designation = input("Enter Designation:- ")
        file.write("Designation:- " + designation + "\n")
        sex = input("Enter Sex:- ")
        file.write("Sex:- " + sex + "\n")
        salary = input("Enter Salary:- ")
        file.write("Salary:- " + salary + "\n")
        file.close()

    def view_staff(self):
        """Viewing Staff Details"""
        print("\n\t\tVIEW STAFF DETAILS\n\n")
        print("1. View Specific Staff Details\n")
        print("2. View Entire Staff Details\n")
        choice = int(input("Enter your choice"))
        file = open("StaffDetails.txt", "rt", encoding="utf-8")
        if choice == 1:
            lookup = input("Enter Staff's Name")
            file = open('StaffDetails.txt', encoding="utf-8")
            content = file.readlines()
            with open("StaffDetails.txt", encoding="utf-8") as myFile:
                for num, line in enumerate(myFile, 1):
                    if lookup in line:
                        print(content[num - 2])
                        print(content[num - 1])
                        print(content[num])
                        print(content[num + 1])
                        print(content[num + 2])

        else:

            print(file.read())
        file.close()

    def edit_staff(self):
        """Editing Staff Details"""
        print("\n\t\tEDIT STAFF DETAILS\n\n")
        search_text = input("Enter the data you want to edit:- ")
        replace_text = input("Enter the data you want to replace:- ")
        with open("StaffDetails.txt", "r", encoding="utf-8") as file:
            data = file.read()
            data = data.replace(search_text, replace_text)

        with open(r"StaffDetails.txt", "w", encoding="utf-8") as file:
            file.write(data)

        print("\nEdited File\n\n")
        file = open("StaffDetails.txt", "rt", encoding="utf-8")

        print(file.read())
        file.close()

    def delete_staff(self):
        """Deleting Staff Details"""
        print("\n\t\tDELETE STAFF DETAILS\n\n")
        print("1. Delete one line")
        print("2. Delete entire content in file")
        choice = int(input("Enter your choice\n"))

        if choice == 1:
            delete_line = int(input("Enter the line which you want to delete"))

            try:
                with open('StaffDetails.txt', 'r', encoding="utf-8") as file_r:

                    lines = file_r.readlines()

                    ptr = 1

                    with open('StaffDetails.txt', 'w', encoding="utf-8") as file_w:
                        for line in lines:

                            if ptr != delete_line:
                                file_w.write(line)
                            ptr += 1
                print("Deleted")

            except Exception as exep:
                print("Oops! something error", exep)

        else:

            file = open('StaffDetails.txt', 'r+', encoding="utf-8")
            file.truncate(0)




