class PatientClass:

    def patient_menu(self):
        """Patient Menu"""
        print("\t\t\tWelcome to Patient Module")
        print("   1. Add new Patient Details\n")
        print("   2. View Patient Details\n")
        print("   3. Edit Patient Details\n")
        print("   4. Delete Patient Details\n\n")
        value = int(input("Enter your choice"))
        return value



    def get_patient(self):
        """Adding Patient Details"""
        print("\n\t\tADD PATIENT DETAILS\n\n")
        file = open("PatientDetails.txt", "at", encoding="utf-8")
        patient_id = input("Enter patient_id:- ")
        file.write("Patient ID:- " + patient_id + "\n")
        name = input("Enter Name:- ")
        file.write("Name:- " + name + "\n")
        disease = input("Enter Disease:- ")
        file.write("Disease:- " + disease + "\n")
        sex = input("Enter Sex:- ")
        file.write("Sex:- " + sex + "\n")
        admit_status = input("Enter Admit Status:- ")
        file.write("Admit Status:- " + admit_status + "\n")
        age = input("Enter Age:- ")
        file.write("Age:- " + age + "\n")
        file.close()

    def view_patient(self):
        """Viewing Patient Details"""
        print("\n\t\tVIEW PATIENT DETAILS\n\n")
        print("1. View Specific Patient Details\n")
        print("2. View Entire Patient Details\n")
        choice = int(input("Enter your choice"))
        file = open("PatientDetails.txt", "rt", encoding="utf-8")
        if choice == 1:
            lookup = input("Enter Patient's Name")
            file = open('PatientDetails.txt', encoding="utf-8")
            content = file.readlines()
            with open("PatientDetails.txt", encoding="utf-8") as myFile:
                for num, line in enumerate(myFile, 1):
                    if lookup in line:
                        print(content[num - 2])
                        print(content[num - 1])
                        print(content[num])
                        print(content[num + 1])
                        print(content[num + 2])
                        print(content[num + 3])

        else:

            print(file.read())
        file.close()

    def edit_patient(self):
        """Editing Patient Details"""
        print("\n\t\tEDIT PATIENT DETAILS\n\n")
        search_text = input("Enter the data you want to edit:- ")
        replace_text = input("Enter the data you want to replace:- ")
        with open("PatientDetails.txt", "r", encoding="utf-8") as file:
            data = file.read()
            data = data.replace(search_text, replace_text)

        with open(r"PatientDetails.txt", "w", encoding="utf-8") as file:
            file.write(data)

        print("\nEdited File\n\n")
        file = open("PatientDetails.txt", "rt", encoding="utf-8")

        print(file.read())
        file.close()

    def delete_patient(self):
        """Deleting Patient Details"""
        print("\n\t\tDELETE PATIENT DETAILS\n\n")
        print("1. Delete one line")
        print("2. Delete entire content in file")
        choice = int(input("Enter your choice\n"))

        if choice == 1:
            delete_line = int(input("Enter the line which you want to delete"))

            try:
                with open('PatientDetails.txt', 'r', encoding="utf-8") as file_r:

                    lines = file_r.readlines()

                    ptr = 1

                    with open('PatientDetails.txt', 'w', encoding="utf-8") as file_w:
                        for line in lines:

                            if ptr != delete_line:
                                file_w.write(line)
                            ptr += 1
                print("Deleted")

            except Exception as exep:
                print("Oops! something error", exep)

        else:

            file = open('PatientDetails.txt', 'r+', encoding="utf-8")
            file.truncate(0)

