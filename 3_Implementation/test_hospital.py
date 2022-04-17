import pytest
from main import *


def test_doctor():
    doc = DoctorClass()
    assert doc.doctor_menu() == [1, 2, 3, 4]


def test_doctor1():
    doc = DoctorClass()
    assert doc.doctor_menu() == [1, 2, 3, 4, 5]


def test_patient():
    patient = PatientClass()
    assert patient.patient_menu() == [1, 2, 3, 4]


def test_patient1():
    patient = PatientClass()
    assert patient.patient_menu() == [1, 2, 3, 4, 5]


def test_staff():
    staff = StaffClass()
    assert staff.staff_menu() == [1, 2, 3, 4]


def test_staff1():
    staff = StaffClass()
    assert staff.staff_menu() == [1, 2, 3, 4, 5]


def test_medical():
    medical = MedicineClass
    assert medical.medicine_menu() == [1, 2, 3, 4]


def test_medical1():
    medical = MedicineClass
    assert medical.medicine_menu() == [1, 2, 3, 4, 5]


def test_lab():
    lab = LaboratoryClass
    assert lab.laboratory_menu() == [1, 2, 3, 4]


def test_lab1():
    lab = LaboratoryClass
    assert lab.laboratory_menu() == [1, 2, 3, 4, 5]


def test_facility():
    facility = FacilityClass
    assert facility.facility_menu() == [1, 2, 3, 4]


def test_facility1():
    facility = FacilityClass
    assert facility.facility_menu() == [1, 2, 3, 4, 5]
