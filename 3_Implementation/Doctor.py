"""Doctor Module"""
class DoctorClass:
    """Doctor Class"""

    def doctor_menu(self):
        """Doctor Menu"""
        print("\t\t\tWelcome to Doctor Module")
        print("   1. Add new Doctor Details\n")
        print("   2. View Doctor Details\n")
        print("   3. Edit Doctor Details\n")
        print("   4. Delete doctor details\n\n")
        value = int(input("Enter your choice\n"))
        return value

    def get_doctor(self):
        """Adding Doctor Details"""
        print("\n\t\tAdd Doctor Details\n\n")
        file = open("DoctorDetails.txt", "at", encoding="utf-8")
        doctor_id = input("Enter doctor_id:- ")
        file.write("Doctor ID:- " + doctor_id + "\n")
        name = input("Enter Name:- ")
        file.write("Name:- " + name + "\n")
        spec = input("Enter Specialisation:- ")
        file.write("Specialisation:- " + spec + "\n")
        working_time = input("Enter Working Time:- ")
        file.write("Working Time:- " + working_time + "\n")
        qualification = input("Enter Qualification:- ")
        file.write("Qualification:- " + qualification + "\n")
        file.close()

    def view_doctor(self):
        """Viewing Doctor Details"""
        print("\n\t\tVIEW DOCTOR DETAILS\n\n")
        print("1. View Specific Doctor Details\n")
        print("2. View Entire Doctor Details\n")
        choice = int(input("Enter your choice"))
        file = open("DoctorDetails.txt", "rt", encoding="utf-8")
        if choice == 1:
            lookup = input("Enter Doctor's Name")
            file = open('DoctorDetails.txt', encoding="utf-8")
            content = file.readlines()
            with open("DoctorDetails.txt", encoding="utf-8") as myFile:
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

    def edit_doctor(self):
        """Editing Doctor Details"""
        print("\n\t\tEdit Doctor Details\n\n")
        search_text = input("Enter the data you want to edit:- ")
        replace_text = input("Enter the data you want to replace:- ")
        with open("DoctorDetails.txt", "r", encoding="utf-8") as file:
            data = file.read()
            data = data.replace(search_text, replace_text)

        with open(r"DoctorDetails.txt", "w", encoding="utf-8") as file:
            file.write(data)

        print("\nEdited File\n\n")
        file = open("DoctorDetails.txt", "rt", encoding="utf-8")

        print(file.read())
        file.close()

    def delete_doctor(self):
        """Deleting Doctor Details"""
        print("\n\t\tDelete Doctor Details\n\n")
        print("1. Delete one line")
        print("2. Delete entire content in file")
        choice = int(input("Enter your choice\n"))

        if choice == 1:
            delete_line = int(input("Enter the line which you want to delete"))

            try:
                with open('DoctorDetails.txt', 'r', encoding="utf-8") as file_r:

                    lines = file_r.readlines()

                    ptr = 1

                    with open('DoctorDetails.txt', 'w', encoding="utf-8") as file_w:
                        for line in lines:

                            if ptr != delete_line:
                                file_w.write(line)
                            ptr += 1
                print("Deleted")

            except Exception as exep:
                print("Oops! something error", exep)

        else:

            file = open('DoctorDetails.txt', 'r+', encoding="utf-8")
            file.truncate(0)




