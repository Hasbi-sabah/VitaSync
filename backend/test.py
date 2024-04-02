#!/usr/bin/env python3
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
import random


# patient1 = Patient(firstName='Bob', lastName='The Builder', sex='Male', email='bob.builder@example.com', role='patient', username='pat', password='pat')
# # patient2 = Patient(firstName='Alice', lastName='Wonderland', sex='Female', email='alice.wonderland@example.com', role='patient')
# # doc1 = HCW(firstName='John', lastName='Doe', email='john.doe@example.com', username='doc', password='doc', role='doctor')
# # doc2 = HCW(firstName='Jane', lastName='Smith', email='jane.smith@example.com', role='doctor')
# # nurse1 = HCW(firstName='Alice', lastName='Johnson', email='alice.johnson@example.com', role='nurse')
# # nurse2 = HCW(firstName='Bob', lastName='Williams', email='bob.williams@example.com', role='nurse')
pharmacist1 = HCW(firstName='Eva', lastName='Davis', email='eva.davis@example.com', role='pharmacist', username='pharm', password='pharm')
# # pharmacist2 = HCW(firstName='Tom', lastName='Jones', email='tom.jones@example.com', role='pharmacist')
# # admin = HCW(firstName='admin', username='admin', password='admin', role='admin')
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

# drug_entries = [
#     {'commercialName': 'Aspirin', 'activeIngredient': 'Acetylsalicylic Acid', 'distributor': 'Pharma Inc.',
#      'description': 'Pain reliever and anti-inflammatory drug', 'dose': '75mg', 'form': 'Tablet', 'status': True, 'price': round(random.uniform(20, 100), 2)},
#     {'commercialName': 'Paracetamol', 'activeIngredient': 'Paracetamol', 'distributor': 'MediCorp',
#      'description': 'Commonly used for pain relief and reducing fever', 'dose': '500mg', 'form': 'Capsule', 'status': True, 'price': round(random.uniform(20, 100), 2)},
#     {'commercialName': 'Amoxicillin', 'activeIngredient': 'Amoxicillin', 'distributor': 'MediCo',
#      'description': 'Antibiotic used to treat bacterial infections', 'dose': '250mg', 'form': 'Capsule', 'status': True, 'price': round(random.uniform(20, 100), 2)},
#     {'commercialName': 'Ibuprofen', 'activeIngredient': 'Ibuprofen', 'distributor': 'MediPharm',
#      'description': 'Nonsteroidal anti-inflammatory drug (NSAID)', 'dose': '200mg', 'form': 'Tablet', 'status': True, 'price': round(random.uniform(20, 100), 2)},
#     {'commercialName': 'Omeprazole', 'activeIngredient': 'Omeprazole', 'distributor': 'PharmaCorp',
#      'description': 'Proton pump inhibitor used to reduce stomach acid', 'dose': '20mg', 'form': 'Capsule', 'status': True, 'price': round(random.uniform(20, 100), 2)},
#     {'commercialName': 'Simvastatin', 'activeIngredient': 'Simvastatin', 'distributor': 'PharmaCo',
#      'description': 'Lipid-lowering medication', 'dose': '40mg', 'form': 'Tablet', 'status': True, 'price': round(random.uniform(20, 100), 2)},
#     {'commercialName': 'Metformin', 'activeIngredient': 'Metformin', 'distributor': 'MediHealth',
#      'description': 'Used to treat type 2 diabetes mellitus', 'dose': '500mg', 'form': 'Tablet', 'status': True, 'price': round(random.uniform(20, 100), 2)},
#     {'commercialName': 'Prednisone', 'activeIngredient': 'Prednisone', 'distributor': 'PharmaHealth',
#      'description': 'Corticosteroid medication', 'dose': '5mg', 'form': 'Tablet', 'status': True, 'price': round(random.uniform(20, 100), 2)},
#     {'commercialName': 'Lisinopril', 'activeIngredient': 'Lisinopril', 'distributor': 'PharmaMed',
#      'description': 'Used to treat high blood pressure and heart failure', 'dose': '10mg', 'form': 'Tablet', 'status': True, 'price': round(random.uniform(20, 100), 2)},
#     {'commercialName': 'Albuterol', 'activeIngredient': 'Albuterol', 'distributor': 'MediPharma',
#      'description': 'Bronchodilator used to treat asthma and COPD', 'dose': '2mg', 'form': 'Tablet', 'status': True, 'price': round(random.uniform(20, 100), 2)},
#     {'commercialName': 'Inactive Drug', 'activeIngredient': 'Inactive Ingredient', 'distributor': 'Inactive Distributor',
#      'description': 'This is an inactive drug for testing purposes', 'dose': '10mg', 'form': 'Tablet', 'status': False, 'price': round(random.uniform(20, 100), 2)},
#     {'commercialName': 'Inactive Drug 2', 'activeIngredient': 'Inactive Ingredient', 'distributor': 'Inactive Distributor',
#      'description': 'This is another inactive drug for testing purposes', 'dose': '20mg', 'form': 'Capsule', 'status': False, 'price': round(random.uniform(20, 100), 2)},
# ]

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
