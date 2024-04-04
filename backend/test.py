#!/usr/bin/env python3
import time
from models.hcw import HCW
from models.drug import Drug
from models.drug_prescribed import DrugPrescribed
from models.prescription import Prescription
from models.patient import Patient
from models.vital import Vital
from models.med_info import MedInfo
from models.vaccine import Vaccine
from models.procedure import Procedure
from models.record import Record
from models.user import User
from models.appointment import Appointment
import random


from datetime import datetime

admin = HCW(firstName='Admin', lastName='Admin', username='admin', password='admin', role='admin')
""" patient1 = Patient(firstName='James', lastName='Smith', sex='Male', phoneNumber='123-456-7890', birthDate=datetime(2000, 1, 15).timestamp(), address='1234 Elm Street', role='patient', username='pat1', password='pat1')
patient2 = Patient(firstName='Emily', lastName='Johnson', sex='Female', phoneNumber='234-567-8901', birthDate=datetime(1995, 6, 22).timestamp(), address='5678 Oak Avenue', role='patient', username='pat2', password='pat2')
patient3 = Patient(firstName='Michael', lastName='Williams', sex='Male', phoneNumber='345-678-9012', birthDate=datetime(1988, 12, 10).timestamp(), address='9101 Pine Lane', role='patient', username='pat3', password='pat3')
patient4 = Patient(firstName='Emma', lastName='Brown', sex='Female', phoneNumber='456-789-0123', birthDate=datetime(1992, 9, 5).timestamp(), address='1212 Maple Drive', role='patient', username='pat4', password='pat4')
patient5 = Patient(firstName='David', lastName='Jones', sex='Male', phoneNumber='567-890-1234', birthDate=datetime(1977, 3, 28).timestamp(), address='1414 Cedar Road', role='patient', username='pat5', password='pat5')
patient6 = Patient(firstName='Olivia', lastName='Miller', sex='Female', phoneNumber='678-901-2345', birthDate=datetime(1985, 11, 17).timestamp(), address='1616 Birch Court', role='patient', username='pat6', password='pat6')
patient7 = Patient(firstName='William', lastName='Davis', sex='Male', phoneNumber='789-012-3456', birthDate=datetime(1998, 4, 30).timestamp(), address='1818 Walnut Avenue', role='patient', username='pat7', password='pat7')
patient8 = Patient(firstName='Ava', lastName='Garcia', sex='Female', phoneNumber='890-123-4567', birthDate=datetime(1990, 7, 12).timestamp(), address='2020 Pineapple Street', role='patient', username='pat8', password='pat8')
patient9 = Patient(firstName='John', lastName='Rodriguez', sex='Male', phoneNumber='901-234-5678', birthDate=datetime(1982, 8, 25).timestamp(), address='2222 Cherry Lane', role='patient', username='pat9', password='pat9')
patient10 = Patient(firstName='Sophia', lastName='Martinez', sex='Female', phoneNumber='012-345-6789', birthDate=datetime(1979, 2, 9).timestamp(), address='2424 Grapevine Road', role='patient', username='pat10', password='pat10')



doc1 = HCW(firstName='John', lastName='Doe', username='doc1', password='doc1', role='doctor', speciality='Cardiology', workNumber='123-456-7890', workAddress='123 Main St, City, Country')
doc2 = HCW(firstName='Jane', lastName='Smith', role='doctor', username='doc2', password='doc2', speciality='Pediatrics', workNumber='987-654-3210', workAddress='456 Elm St, City, Country')
nurse1 = HCW(firstName='Alice', lastName='Johnson', role='nurse', username='nurse1', password='nurse1', speciality='Emergency Care', workNumber='111-222-3333', workAddress='789 Oak St, City, Country')
nurse2 = HCW(firstName='Bob', lastName='Williams', role='nurse', username='nurse2', password='nurse2', speciality='Surgery', workNumber='444-555-6666', workAddress='101 Pine St, City, Country')
pharmacist1 = HCW(firstName='Eva', lastName='Davis', role='pharmacist', username='pharm1', password='pharm1', speciality='Clinical Pharmacy', workNumber='777-888-9999', workAddress='321 Cedar St, City, Country')
pharmacist2 = HCW(firstName='Tom', lastName='Jones', role='pharmacist', username='pharm2', password='pharm2', speciality='Hospital Pharmacy', workNumber='222-333-4444', workAddress='555 Maple St, City, Country')

doc3 = HCW(firstName='Michael', lastName='Brown', role='doctor', username='doc3', password='doc3', speciality='Dermatology', workNumber='111-222-3333', workAddress='789 Oak St, City, Country')
doc4 = HCW(firstName='Jessica', lastName='Taylor', role='doctor', username='doc4', password='doc4', speciality='Internal Medicine', workNumber='444-555-6666', workAddress='101 Pine St, City, Country')
nurse3 = HCW(firstName='William', lastName='Martinez', role='nurse', username='nurse3', password='nurse3', speciality='Psychiatric Nursing', workNumber='777-888-9999', workAddress='321 Cedar St, City, Country')
nurse4 = HCW(firstName='Olivia', lastName='Garcia', role='nurse', username='nurse4', password='nurse4', speciality='Emergency Care', workNumber='222-333-4444', workAddress='555 Maple St, City, Country')
pharmacist3 = HCW(firstName='Daniel', lastName='Rodriguez', role='pharmacist', username='pharm3', password='pharm3', speciality='Retail Pharmacy', workNumber='123-456-7890', workAddress='123 Main St, City, Country')
pharmacist4 = HCW(firstName='Sophia', lastName='Hernandez', role='pharmacist', username='pharm4', password='pharm4', speciality='Clinical Pharmacy', workNumber='987-654-3210', workAddress='456 Elm St, City, Country')

doc5 = HCW(firstName='David', lastName='Wilson', role='doctor', username='doc5', password='doc5', speciality='Neurology', workNumber='555-666-7777', workAddress='888 Pine St, City, Country')
doc6 = HCW(firstName='Sarah', lastName='Anderson', role='doctor', username='doc6', password='doc6', speciality='Oncology', workNumber='666-777-8888', workAddress='999 Oak St, City, Country')
nurse5 = HCW(firstName='Matthew', lastName='Thomas', role='nurse', username='nurse5', password='nurse5', speciality='Pediatric Nursing', workNumber='333-444-5555', workAddress='111 Cedar St, City, Country')
nurse6 = HCW(firstName='Emily', lastName='White', role='nurse', username='nurse6', password='nurse6', speciality='ICU Nursing', workNumber='777-888-9999', workAddress='555 Elm St, City, Country')
pharmacist5 = HCW(firstName='Andrew', lastName='Lopez', role='pharmacist', username='pharm5', password='pharm5', speciality='Community Pharmacy', workNumber='888-999-0000', workAddress='777 Maple St, City, Country')
pharmacist6 = HCW(firstName='Madison', lastName='King', role='pharmacist', username='pharm6', password='pharm6', speciality='Geriatric Pharmacy', workNumber='000-111-2222', workAddress='444 Cedar St, City, Country')

current_timestamp = int(time.time()) """

# Appointments for today at different times (assuming each appointment is one hour apart)
""" appointment1 = Appointment(patientId=patient1.id, hcwId=doc1.id, time=current_timestamp + 0)
appointment2 = Appointment(patientId=patient2.id, hcwId=doc1.id, time=current_timestamp + 3600)  # 1 hour later
appointment3 = Appointment(patientId=patient3.id, hcwId=doc1.id, time=current_timestamp + 7200)  # 2 hours later
appointment4 = Appointment(patientId=patient4.id, hcwId=doc1.id, time=current_timestamp + 10800)  # 3 hours later
appointment5 = Appointment(patientId=patient5.id, hcwId=doc1.id, time=current_timestamp + 14400)  # 4 hours later
appointment6 = Appointment(patientId=patient6.id, hcwId=doc1.id, time=current_timestamp + 18000)  # 5 hours later
appointment7 = Appointment(patientId=patient7.id, hcwId=doc1.id, time=current_timestamp + 21600)  # 6 hours later
appointment8 = Appointment(patientId=patient8.id, hcwId=doc1.id, time=current_timestamp + 25200)  # 7 hours later
appointment9 = Appointment(patientId=patient9.id, hcwId=doc1.id, time=current_timestamp + 28800)  # 8 hours later
appointment10 = Appointment(patientId=patient10.id, hcwId=doc1.id, time=current_timestamp + 32400)  """
# admin = HCW(username='admin', password='admin', role='admin')
# patient3 = Patient(firstName='Charlie', lastName='Chaplin', sex='Male')
# patient4 = Patient(firstName='Dorothy', lastName='Gale', sex='Female')
# patient5 = Patient(firstName='Eddie', lastName='Murphy', sex='Male')
# patient6 = Patient(firstName='Fiona', lastName='Apple', sex='Female')

# record1 = Record(diagnosis="Bronchitis", notes="Medication given", patientId=patient1.id, assessedById=doc1.id)
# record2 = Record(diagnosis="Hypertension", notes="Patient advised to monitor blood pressure regularly", patientId=patient1.id, assessedById=doc2.id)
# record3 = Record(notes="Insulin prescribed, dietary recommendations provided", patientId=patient1.id, assessedById=doc1.id)
# record4 = Record(diagnosis="Fractured leg", notes="Leg cast applied, follow-up appointment scheduled", patientId=patient2.id, assessedById=doc1.id)
# record5 = Record(diagnosis="Migraine", notes="Prescribed pain medication, advised to rest in a quiet environment", patientId=patient2.id, assessedById=doc2.id)
# record6 = Record(diagnosis="Common cold")
""" 
drugs = [
    Drug(commercialName='Aspirin', activeIngredient='Acetylsalicylic Acid', distributor='ABC Pharmaceuticals', description='Pain reliever and anti-inflammatory drug', dose='325 mg', form='Tablet', status=True, price=round(random.uniform(20, 100), 2)),
    Drug(commercialName='Aspirin', activeIngredient='Acetylsalicylic Acid', distributor='ABC Pharmaceuticals', description='Pain reliever and anti-inflammatory drug', dose='81 mg', form='Chewable tablet', status=True, price=round(random.uniform(20, 100), 2)),
    Drug(commercialName='Aspirin', activeIngredient='Acetylsalicylic Acid', distributor='ABC Pharmaceuticals', description='Pain reliever and anti-inflammatory drug', dose='500 mg', form='Effervescent tablet', status=True, price=round(random.uniform(20, 100), 2)),
    Drug(commercialName='Aspirin', activeIngredient='Acetylsalicylic Acid', distributor='ABC Pharmaceuticals', description='Pain reliever and anti-inflammatory drug', dose='1000 mg', form='Powder for solution', status=True, price=round(random.uniform(20, 100), 2)),
    Drug(commercialName='Tylenol', activeIngredient='Paracetamol', distributor='XYZ Pharmaceuticals', description='Fever reducer and mild pain reliever', dose='500 mg', form='Capsule', status=True, price=round(random.uniform(20, 100), 2)),
    Drug(commercialName='Tylenol', activeIngredient='Paracetamol', distributor='XYZ Pharmaceuticals', description='Fever reducer and mild pain reliever', dose='325 mg', form='Tablet', status=True, price=round(random.uniform(20, 100), 2)),
    Drug(commercialName='Tylenol', activeIngredient='Paracetamol', distributor='XYZ Pharmaceuticals', description='Fever reducer and mild pain reliever', dose='650 mg', form='Liquid suspension', status=True, price=round(random.uniform(20, 100), 2)),
    Drug(commercialName='Tylenol', activeIngredient='Paracetamol', distributor='XYZ Pharmaceuticals', description='Fever reducer and mild pain reliever', dose='1000 mg', form='Suppository', status=True, price=round(random.uniform(20, 100), 2)),
    Drug(commercialName='Lisinopril', activeIngredient='Lisinopril', distributor='Pharma Solutions', description='ACE inhibitor for hypertension and heart failure', dose='10 mg', form='Tablet', status=True, price=round(random.uniform(20, 100), 2)),
    Drug(commercialName='Lisinopril', activeIngredient='Lisinopril', distributor='Pharma Solutions', description='ACE inhibitor for hypertension and heart failure', dose='20 mg', form='Capsule', status=True, price=round(random.uniform(20, 100), 2)),
    Drug(commercialName='Lisinopril', activeIngredient='Lisinopril', distributor='Pharma Solutions', description='ACE inhibitor for hypertension and heart failure', dose='40 mg', form='Oral solution', status=True, price=round(random.uniform(20, 100), 2)),
    Drug(commercialName='Lisinopril', activeIngredient='Lisinopril', distributor='Pharma Solutions', description='ACE inhibitor for hypertension and heart failure', dose='5 mg', form='Oral solution', status=True, price=round(random.uniform(20, 100), 2)),
    Drug(commercialName='Metformin', activeIngredient='Metformin Hydrochloride', distributor='MediCorp', description='Antidiabetic medication for type 2 diabetes', dose='500 mg', form='Extended-release tablet', status=True, price=round(random.uniform(20, 100), 2)),
    Drug(commercialName='Metformin', activeIngredient='Metformin Hydrochloride', distributor='MediCorp', description='Antidiabetic medication for type 2 diabetes', dose='250 mg', form='Immediate-release tablet', status=True, price=round(random.uniform(20, 100), 2)),
    Drug(commercialName='Metformin', activeIngredient='Metformin Hydrochloride', distributor='MediCorp', description='Antidiabetic medication for type 2 diabetes', dose='850 mg', form='Extended-release tablet', status=True, price=round(random.uniform(20, 100), 2)),
    Drug(commercialName='Metformin', activeIngredient='Metformin Hydrochloride', distributor='MediCorp', description='Antidiabetic medication for type 2 diabetes', dose='1000 mg', form='Oral solution', status=True, price=round(random.uniform(20, 100), 2)),
    Drug(commercialName='Prilosec', activeIngredient='Omeprazole', distributor='Global Pharma', description='Proton pump inhibitor for acid reflux and ulcers', dose='20 mg', form='Capsule', status=True, price=round(random.uniform(20, 100), 2)),
    Drug(commercialName='Prilosec', activeIngredient='Omeprazole', distributor='Global Pharma', description='Proton pump inhibitor for acid reflux and ulcers', dose='10 mg', form='Tablet', status=True, price=round(random.uniform(20, 100), 2)),
    Drug(commercialName='Prilosec', activeIngredient='Omeprazole', distributor='Global Pharma', description='Proton pump inhibitor for acid reflux and ulcers', dose='40 mg', form='Tablet', status=True, price=round(random.uniform(20, 100), 2)),
    Drug(commercialName='Prilosec', activeIngredient='Omeprazole', distributor='Global Pharma', description='Proton pump inhibitor for acid reflux and ulcers', dose='20 mg', form='Liquid suspension', status=True, price=round(random.uniform(20, 100), 2)),
    Drug(commercialName='Amoxicillin', activeIngredient='Amoxicillin', distributor='Healthcare Distributors', description='Antibiotic for bacterial infections', dose='1000 mg', form='Powder for suspension', status=True, price=round(random.uniform(20, 100), 2)),
    Drug(commercialName='Amoxicillin', activeIngredient='Amoxicillin', distributor='Healthcare Distributors', description='Antibiotic for bacterial infections', dose='500 mg', form='Capsule', status=True, price=round(random.uniform(20, 100), 2)),
    Drug(commercialName='Amoxicillin', activeIngredient='Amoxicillin', distributor='Healthcare Distributors', description='Antibiotic for bacterial infections', dose='250 mg', form='Chewable tablet', status=True, price=round(random.uniform(20, 100), 2)),
    Drug(commercialName='Amoxicillin', activeIngredient='Amoxicillin', distributor='Healthcare Distributors', description='Antibiotic for bacterial infections', dose='1000 mg', form='Powder for suspension', status=True, price=round(random.uniform(20, 100), 2)),    
    Drug(commercialName='Lipitor', activeIngredient='Atorvastatin Calcium', distributor='PharmaCare', description='Statins for lowering cholesterol levels', dose='10 mg', form='Tablet', status=True, price=round(random.uniform(20, 100), 2)),
    Drug(commercialName='Lipitor', activeIngredient='Atorvastatin Calcium', distributor='PharmaCare', description='Statins for lowering cholesterol levels', dose='20 mg', form='Capsule', status=True, price=round(random.uniform(20, 100), 2)),
    Drug(commercialName='Lipitor', activeIngredient='Atorvastatin Calcium', distributor='PharmaCare', description='Statins for lowering cholesterol levels', dose='40 mg', form='Extended-release tablet', status=True, price=round(random.uniform(20, 100), 2)),
    Drug(commercialName='Lipitor', activeIngredient='Atorvastatin Calcium', distributor='PharmaCare', description='Statins for lowering cholesterol levels', dose='10 mg', form='Tablet', status=True, price=round(random.uniform(20, 100), 2)),
    Drug(commercialName='Ventolin', activeIngredient='Albuterol Sulfate', distributor='PharmaXpress', description='Bronchodilator for asthma and COPD', dose='2 mg', form='Inhaler', status=True, price=round(random.uniform(20, 100), 2)),
    Drug(commercialName='Ventolin', activeIngredient='Albuterol Sulfate', distributor='PharmaXpress', description='Bronchodilator for asthma and COPD', dose='4 mg', form='Inhaler', status=True, price=round(random.uniform(20, 100), 2)),
    Drug(commercialName='Ventolin', activeIngredient='Albuterol Sulfate', distributor='PharmaXpress', description='Bronchodilator for asthma and COPD', dose='8 mg', form='Inhaler', status=True, price=round(random.uniform(20, 100), 2)),
    Drug(commercialName='Ventolin', activeIngredient='Albuterol Sulfate', distributor='PharmaXpress', description='Bronchodilator for asthma and COPD', dose='1 mg', form='Nebulizer solution', status=True, price=round(random.uniform(20, 100), 2)),
    Drug(commercialName='Valium', activeIngredient='Diazepam', distributor='MediSafe', description='Benzodiazepine for anxiety and seizures', dose='5 mg', form='Tablet', status=True, price=round(random.uniform(20, 100), 2)),
    Drug(commercialName='Claritin', activeIngredient='Loratadine', distributor='MegaPharma', description='Antihistamine for allergies and hay fever', dose='10 mg', form='Tablet', status=True, price=round(random.uniform(20, 100), 2)),
    Drug(commercialName='Cozaar', activeIngredient='Losartan Potassium', distributor='PharmaLink', description='ARB for hypertension and heart failure', dose='50 mg', form='Tablet', status=True, price=round(random.uniform(20, 100), 2)),
    Drug(commercialName='Coumadin', activeIngredient='Warfarin Sodium', distributor='MediLife', description='Anticoagulant for blood clot prevention', dose='2 mg', form='Tablet', status=True, price=round(random.uniform(20, 100), 2)),
    Drug(commercialName='Synthroid', activeIngredient='Levothyroxine Sodium', distributor='Global Med', description='Thyroid hormone replacement therapy', dose='100 mcg', form='Tablet', status=True, price=round(random.uniform(20, 100), 2)),
    Drug(commercialName='Hydrochlorothiazide', activeIngredient='Hydrochlorothiazide', distributor='HealthCo', description='Diuretic for hypertension and edema', dose='25 mg', form='Tablet', status=True, price=round(random.uniform(20, 100), 2)),
    Drug(commercialName='Zantac', activeIngredient='Ranitidine Hydrochloride', distributor='PharmaGen', description='H2 blocker for acid reflux and ulcers', dose='150 mg', form='Tablet', status=True, price=round(random.uniform(20, 100), 2)),
    Drug(commercialName='Cipro', activeIngredient='Ciprofloxacin', distributor='MediNet', description='Fluoroquinolone antibiotic for infections', dose='500 mg', form='Tablet', status=True, price=round(random.uniform(20, 100), 2)),
    Drug(commercialName='Cymbalta', activeIngredient='Duloxetine Hydrochloride', distributor='PharmaHub', description='SNRI antidepressant for depression and anxiety', dose='60 mg', form='Capsule', status=True, price=round(random.uniform(20, 100), 2)),
    Drug(commercialName='Singulair', activeIngredient='Montelukast Sodium', distributor='HealthMed', description='Leukotriene receptor antagonist for asthma and allergies', dose='10 mg', form='Tablet', status=True, price=round(random.uniform(20, 100), 2)),
    Drug(commercialName='Lyrica', activeIngredient='Pregabalin', distributor='PharmaDirect', description='Anticonvulsant for neuropathic pain and seizures', dose='75 mg', form='Capsule', status=True, price=round(random.uniform(20, 100), 2)),
    Drug(commercialName='Zocor', activeIngredient='Simvastatin', distributor='MediGroup', description='Statins for lowering cholesterol levels', dose='20 mg', form='Tablet', status=True, price=round(random.uniform(20, 100), 2)),
    Drug(commercialName='Advil', activeIngredient='Ibuprofen', distributor='PharmaCo', description='Nonsteroidal anti-inflammatory drug (NSAID)', dose='200 mg', form='Tablet', status=True, price=round(random.uniform(20, 100), 2)),
    Drug(commercialName='Zyrtec', activeIngredient='Cetirizine', distributor='MediPharm', description='Antihistamine for allergies and hives', dose='10 mg', form='Tablet', status=True, price=round(random.uniform(20, 100), 2)),
    Drug(commercialName='Norvasc', activeIngredient='Amlodipine', distributor='CardioMed', description='Calcium channel blocker for hypertension', dose='5 mg', form='Tablet', status=True, price=round(random.uniform(20, 100), 2)),
    Drug(commercialName='Prozac', activeIngredient='Fluoxetine', distributor='MentalHealth', description='SSRI antidepressant for depression and anxiety', dose='20 mg', form='Capsule', status=True, price=round(random.uniform(20, 100), 2)),
    Drug(commercialName='Xanax', activeIngredient='Alprazolam', distributor='AnxietyRelief', description='Benzodiazepine for anxiety disorders', dose='0.5 mg', form='Tablet', status=True, price=round(random.uniform(20, 100), 2)),
    Drug(commercialName='Prednisone', activeIngredient='Prednisone', distributor='AntiInflammatory', description='Corticosteroid for inflammation and autoimmune conditions', dose='5 mg', form='Tablet', status=True, price=round(random.uniform(20, 100), 2)),
    Drug(commercialName='Metoprolol', activeIngredient='Metoprolol Tartrate', distributor='HeartCare', description='Beta-blocker for hypertension and heart conditions', dose='25 mg', form='Tablet', status=True, price=round(random.uniform(20, 100), 2)),
    Drug(commercialName='Flonase', activeIngredient='Fluticasone', distributor='NasalHealth', description='Nasal corticosteroid for allergies and nasal congestion', dose='50 mcg', form='Nasal Spray', status=True, price=round(random.uniform(20, 100), 2)),
    Drug(commercialName='Ativan', activeIngredient='Lorazepam', distributor='SleepWell', description='Benzodiazepine for anxiety and insomnia', dose='1 mg', form='Tablet', status=True, price=round(random.uniform(20, 100), 2)),
    Drug(commercialName='Cephalexin', activeIngredient='Cephalexin', distributor='InfectoCare', description='Antibiotic for bacterial infections', dose='500 mg', form='Capsule', status=True, price=round(random.uniform(20, 100), 2)),
    Drug(commercialName='Zoloft', activeIngredient='Sertraline', distributor='MentalHealth', description='SSRI antidepressant for depression and anxiety', dose='50 mg', form='Tablet', status=True, price=round(random.uniform(20, 100), 2)),
    Drug(commercialName='Gabapentin', activeIngredient='Gabapentin', distributor='NeuroPharma', description='Anticonvulsant for neuropathic pain and seizures', dose='300 mg', form='Capsule', status=True, price=round(random.uniform(20, 100), 2)),
    Drug(commercialName='Benadryl', activeIngredient='Diphenhydramine', distributor='AllergyRelief', description='Antihistamine for allergies and sleep aid', dose='25 mg', form='Capsule', status=True, price=round(random.uniform(20, 100), 2)),
    Drug(commercialName='Crestor', activeIngredient='Rosuvastatin', distributor='CholesterolCare', description='Statins for lowering cholesterol levels', dose='10 mg', form='Tablet', status=True, price=round(random.uniform(20, 100), 2)),
    Drug(commercialName='Bactrim', activeIngredient='Sulfamethoxazole/Trimethoprim', distributor='InfectoCare', description='Antibiotic for bacterial infections', dose='800/160 mg', form='Tablet', status=True, price=round(random.uniform(20, 100), 2)),
    Drug(commercialName='Seroquel', activeIngredient='Quetiapine', distributor='MentalHealth', description='Atypical antipsychotic for schizophrenia and bipolar disorder', dose='100 mg', form='Tablet', status=True, price=round(random.uniform(20, 100), 2)),
    Drug(commercialName='Lexapro', activeIngredient='Escitalopram', distributor='MentalHealth', description='SSRI antidepressant for depression and anxiety', dose='10 mg', form='Tablet', status=True, price=round(random.uniform(20, 100), 2)),
    Drug(commercialName='Nexium', activeIngredient='Esomeprazole', distributor='GastroCare', description='Proton pump inhibitor for acid reflux and ulcers', dose='20 mg', form='Capsule', status=True, price=round(random.uniform(20, 100), 2)),
    Drug(commercialName='Hydrocodone', activeIngredient='Hydrocodone/Acetaminophen', distributor='PainRelief', description='Opioid pain medication', dose='5/325 mg', form='Tablet', status=True, price=round(random.uniform(20, 100), 2)),
    Drug(commercialName='Lantus', activeIngredient='Insulin Glargine', distributor='DiabetesCare', description='Long-acting insulin for diabetes', dose='100 units/mL', form='Injection', status=True, price=round(random.uniform(20, 100), 2)),
    Drug(commercialName='Viagra', activeIngredient='Sildenafil', distributor='ErectileHealth', description='Phosphodiesterase inhibitor for erectile dysfunction', dose='50 mg', form='Tablet', status=True, price=round(random.uniform(20, 100), 2)),
    Drug(commercialName='Celebrex', activeIngredient='Celecoxib', distributor='PainRelief', description='COX-2 inhibitor for pain and inflammation', dose='200 mg', form='Capsule', status=True, price=round(random.uniform(20, 100), 2)),
    Drug(commercialName='Alprazolam', activeIngredient='Alprazolam', distributor='AnxietyRelief', description='Benzodiazepine for anxiety disorders', dose='0.25 mg', form='Tablet', status=True, price=round(random.uniform(20, 100), 2)),
    Drug(commercialName='Pravastatin', activeIngredient='Pravastatin', distributor='CholesterolCare', description='Statins for lowering cholesterol levels', dose='40 mg', form='Tablet', status=True, price=round(random.uniform(20, 100), 2)),
    Drug(commercialName='Metronidazole', activeIngredient='Metronidazole', distributor='InfectoCare', description='Antibiotic and antiprotozoal agent', dose='500 mg', form='Tablet', status=True, price=round(random.uniform(20, 100), 2)),
    Drug(commercialName='Metronidazole', activeIngredient='Metronidazole', distributor='InfectoCare', description='Antibiotic and antiprotozoal agent', dose='250 mg', form='Capsule', status=True, price=round(random.uniform(20, 100), 2)),
    Drug(commercialName='Metronidazole', activeIngredient='Metronidazole', distributor='InfectoCare', description='Antibiotic and antiprotozoal agent', dose='0.75% cream', form='Topical Cream', status=True, price=round(random.uniform(20, 100), 2)),
    Drug(commercialName='Metronidazole', activeIngredient='Metronidazole', distributor='InfectoCare', description='Antibiotic and antiprotozoal agent', dose='500 mg', form='Vaginal Gel', status=True, price=round(random.uniform(20, 100), 2)),
    Drug(commercialName='Amoxicillin', activeIngredient='Amoxicillin', distributor='Healthcare Distributors', description='Antibiotic for bacterial infections', dose='250 mg', form='Chewable Tablet', status=True, price=round(random.uniform(20, 100), 2)),
    Drug(commercialName='Amoxicillin', activeIngredient='Amoxicillin', distributor='Healthcare Distributors', description='Antibiotic for bacterial infections', dose='125 mg/5 mL', form='Oral Suspension', status=True, price=round(random.uniform(20, 100), 2)),
    Drug(commercialName='Loratadine', activeIngredient='Loratadine', distributor='MegaPharma', description='Antihistamine for allergies and hay fever', dose='10 mg', form='Tablet', status=True, price=round(random.uniform(20, 100), 2)),
    Drug(commercialName='Loratadine', activeIngredient='Loratadine', distributor='MegaPharma', description='Antihistamine for allergies and hay fever', dose='5 mg', form='Chewable Tablet', status=True, price=round(random.uniform(20, 100), 2)),
    Drug(commercialName='Loratadine', activeIngredient='Loratadine', distributor='MegaPharma', description='Antihistamine for allergies and hay fever', dose='5 mg/5 mL', form='Oral Solution', status=True, price=round(random.uniform(20, 100), 2)),
    Drug(commercialName='Lisinopril', activeIngredient='Lisinopril', distributor='Pharma Solutions', description='ACE inhibitor for hypertension and heart failure', dose='10 mg', form='Tablet', status=True, price=round(random.uniform(20, 100), 2)),
    Drug(commercialName='Lisinopril', activeIngredient='Lisinopril', distributor='Pharma Solutions', description='ACE inhibitor for hypertension and heart failure', dose='5 mg', form='Capsule', status=True, price=round(random.uniform(20, 100), 2)),
    Drug(commercialName='Lisinopril', activeIngredient='Lisinopril', distributor='Pharma Solutions', description='ACE inhibitor for hypertension and heart failure', dose='2.5 mg', form='Oral Solution', status=True, price=round(random.uniform(20, 100), 2)),
    Drug(commercialName='Atorvastatin', activeIngredient='Atorvastatin Calcium', distributor='PharmaCare', description='Statins for lowering cholesterol levels', dose='40 mg', form='Tablet', status=True, price=round(random.uniform(20, 100), 2)),
    Drug(commercialName='Atorvastatin', activeIngredient='Atorvastatin Calcium', distributor='PharmaCare', description='Statins for lowering cholesterol levels', dose='20 mg', form='Capsule', status=True, price=round(random.uniform(20, 100), 2)),
    Drug(commercialName='Atorvastatin', activeIngredient='Atorvastatin Calcium', distributor='PharmaCare', description='Statins for lowering cholesterol levels', dose='80 mg', form='Extended-release Tablet', status=True, price=round(random.uniform(20, 100), 2)),
    Drug(commercialName='Omeprazole', activeIngredient='Omeprazole', distributor='Global Pharma', description='Proton pump inhibitor for acid reflux and ulcers', dose='20 mg', form='Capsule', status=True, price=round(random.uniform(20, 100), 2)),
    Drug(commercialName='Omeprazole', activeIngredient='Omeprazole', distributor='Global Pharma', description='Proton pump inhibitor for acid reflux and ulcers', dose='40 mg', form='Delayed-release Capsule', status=True, price=round(random.uniform(20, 100), 2)),
    Drug(commercialName='Omeprazole', activeIngredient='Omeprazole', distributor='Global Pharma', description='Proton pump inhibitor for acid reflux and ulcers', dose='10 mg', form='Oral Suspension', status=True, price=round(random.uniform(20, 100), 2)),
    Drug(commercialName='Ciprofloxacin', activeIngredient='Ciprofloxacin', distributor='MediNet', description='Fluoroquinolone antibiotic for infections', dose='500 mg', form='Tablet', status=True, price=round(random.uniform(20, 100), 2)),
    Drug(commercialName='Ciprofloxacin', activeIngredient='Ciprofloxacin', distributor='MediNet', description='Fluoroquinolone antibiotic for infections', dose='250 mg', form='Capsule', status=True, price=round(random.uniform(20, 100), 2)),
    Drug(commercialName='Ciprofloxacin', activeIngredient='Ciprofloxacin', distributor='MediNet', description='Fluoroquinolone antibiotic for infections', dose='0.3% Eye Drops', form='Eye Drops', status=True, price=round(random.uniform(20, 100), 2)),
    Drug(commercialName='Diazepam', activeIngredient='Diazepam', distributor='MediSafe', description='Benzodiazepine for anxiety and seizures', dose='5 mg', form='Tablet', status=True, price=round(random.uniform(20, 100), 2)),
    Drug(commercialName='Diazepam', activeIngredient='Diazepam', distributor='MediSafe', description='Benzodiazepine for anxiety and seizures', dose='10 mg', form='Injection', status=True, price=round(random.uniform(20, 100), 2)),
    Drug(commercialName='Diazepam', activeIngredient='Diazepam', distributor='MediSafe', description='Benzodiazepine for anxiety and seizures', dose='2 mg/mL', form='Oral Solution', status=True, price=round(random.uniform(20, 100), 2)),
    Drug(commercialName='Warfarin', activeIngredient='Warfarin Sodium', distributor='MediLife', description='Anticoagulant for blood clot prevention', dose='2 mg', form='Tablet', status=True, price=round(random.uniform(20, 100), 2)),
    Drug(commercialName='Warfarin', activeIngredient='Warfarin Sodium', distributor='MediLife', description='Anticoagulant for blood clot prevention', dose='1 mg', form='Capsule', status=True, price=round(random.uniform(20, 100), 2)),
    Drug(commercialName='Warfarin', activeIngredient='Warfarin Sodium', distributor='MediLife', description='Anticoagulant for blood clot prevention', dose='5 mg', form='Injection', status=True, price=round(random.uniform(20, 100), 2))
]
 """
# drugs = [Drug(**entry) for entry in drug_entries]

# vitals1 = Vital(takenById=doc1.id, takenForId=patient1.id)
# vitals2 = Vital(takenById=doc1.id, takenForId=patient1.id)

# info = MedInfo(patientId=patient1.id)

# proc = Procedure(patientId=patient1.id, prescribedById=doc1.id)

# drug1 = Drug(name='doliprane')
# drug2 = Drug(name='paracetamol')
# drug3 = Drug(name='ibuprofen')

# vaccine1 = Vaccine(administeredById=doc1.id, administeredForId=patient1.id, drugId=drug1.id)
# vaccine2 = Vaccine(administeredById=doc1.id, administeredForId=patient1.id, drugId=drug1.id)

# prsc1 = Prescription(prescribedById=doc2.id, rescribedForId=patient1.id)
# med1 = DrugPrescribed(drugId=drugs[0].id, prescriptionId = prsc1.id, instructions='twice a day for 15 days')
# med2 = DrugPrescribed(drugId=drugs[3].id, prescriptionId = prsc1.id, instructions='before meals, adjust as needed')
# med3 = DrugPrescribed(drugId=drugs[5].id, prescriptionId = prsc1.id, instructions='as per allergist advice')


# prsc2 = Prescription(prescribedById=doc2.id, prescribedForId=patient2.id)
# med1 = DrugPrescribed(drugId=drugs[1].id, prescriptionId = prsc2.id, instructions='daily in the morning')
# med2 = DrugPrescribed(drugId=drugs[2].id, prescriptionId = prsc2.id, instructions='as needed, maximum 3 times a day')
# med3 = DrugPrescribed(drugId=drugs[4].id, prescriptionId = prsc2.id, instructions='once a day for a week')


# record1 = Record(patientId=patient1.id, vaccineId=vaccine1.id,
#                   vitalsId=vitals1.id, procedureId=proc.id,
#                   prescriptionId=prsc1.id, assessedById=doc1.id)

# print(doc1 == record1.assessedBy)
