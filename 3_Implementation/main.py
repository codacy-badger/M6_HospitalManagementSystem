from Doctor import DoctorClass
from Facility import *
from Lab import *
from Medical import *
from Patients import *
from Staff import *


print("\n\n\t\t\t\t\tHospital  Management System\n\n")
print("\n   1: Doctor\n   2: Patients\n   3: Medicines\n   4: Laboratories\n   5: Facilities\n   6: Staff\n   7: "
      "Exit\n\n")

answer = int(input("\n\nEnter your choice\n\n"))

if answer == 1:
    doc = DoctorClass()
    doc_menu_value = doc.doctor_menu()

    if doc_menu_value == 1:
        doc.get_doctor()

    elif doc_menu_value == 2:
        doc.view_doctor()

    elif doc_menu_value == 3:
        doc.edit_doctor()

    elif doc_menu_value == 4:
        doc.delete_doctor()

    else:
        exit(0)

elif answer == 2:
    patient = PatientClass()
    patient_menu_value = patient.patient_menu()

    if patient_menu_value == 1:
        patient.get_patient()

    elif patient_menu_value == 2:
        patient.view_patient()

    elif patient_menu_value == 3:
        patient.edit_patient()

    elif patient_menu_value == 4:
        patient.delete_patient()

    else:
        exit(0)

elif answer == 3:
    medicine = MedicineClass()
    medicine_menu_value = medicine.medicine_menu()
    if medicine_menu_value == 1:
        medicine.get_medicine()

    elif medicine_menu_value == 2:
        medicine.view_medicine()

    elif medicine_menu_value == 3:
        medicine.edit_medicine()

    elif medicine_menu_value == 4:
        medicine.delete_medicine()

    else:
        exit(0)

elif answer == 4:
    lab = LaboratoryClass()
    lab_menu_value = lab.laboratory_menu()
    if lab_menu_value == 1:
        lab.get_laboratory()

    elif lab_menu_value == 2:
        lab.view_laboratory()

    elif lab_menu_value == 3:
        lab.edit_laboratory()

    elif lab_menu_value == 4:
        lab.delete_laboratory()

    else:
        exit(0)

elif answer == 5:
    facility = FacilityClass()
    facility_menu_value = facility.facility_menu()
    if facility_menu_value == 1:
        facility.get_facility()

    elif facility_menu_value == 2:
        facility.view_facility()

    elif facility_menu_value == 3:
        facility.edit_facility()

    elif facility_menu_value == 4:
        facility.delete_facility()

    else:
        exit(0)

elif answer == 6:
    staff = StaffClass()
    staff_menu_value = staff.staff_menu()
    if staff_menu_value == 1:
        staff.get_staff()

    elif staff_menu_value == 2:
        staff.view_staff()

    elif staff_menu_value == 3:
        staff.edit_staff()

    elif staff_menu_value == 4:
        staff.delete_staff()

    else:
        exit(0)

else:
    exit(0)
