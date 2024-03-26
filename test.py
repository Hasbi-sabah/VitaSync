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
from models.test import Test
from models.test_request import TestRequest
import random

tests = [
    Test(name='Blood Glucose Test', type='Blood Test', sampleType='Blood', instructions='Fasting required for accurate results', price=round(random.uniform(20, 100), 2), description='Measures the level of glucose (sugar) in the blood to diagnose diabetes or monitor blood sugar control.'),
    Test(name='Complete Blood Count (CBC)', type='Blood Test', sampleType='Blood', price=round(random.uniform(20, 100), 2), description='Provides information about the cells in the blood, including red blood cells, white blood cells, and platelets.'),
    Test(name='Urinalysis', type='Urine Test', sampleType='Urine', instructions='Collect a midstream urine sample', price=round(random.uniform(20, 100), 2), description='Analyzes the physical, chemical, and microscopic properties of urine to detect urinary tract infections, kidney problems, and other conditions.'),
    Test(name='X-ray Imaging (Chest X-ray)', type='Imaging Study', price=round(random.uniform(20, 100), 2), description='Produces images of the chest area to evaluate the lungs, heart, ribs, and other structures.'),
    Test(name='Electrocardiogram (ECG or EKG)', type='Cardiac Test', price=round(random.uniform(20, 100), 2), description='Records the electrical activity of the heart to detect irregularities and heart rhythm disorders.'),
    Test(name='Thyroid Function Tests', type='Blood Test', sampleType='Blood', price=round(random.uniform(20, 100), 2), description='Measures thyroid hormone levels in the blood to evaluate thyroid function and diagnose thyroid disorders.'),
    Test(name='Magnetic Resonance Imaging (MRI)', type='Imaging Study', price=round(random.uniform(20, 100), 2), description='Uses magnetic fields and radio waves to produce detailed images of internal organs, soft tissues, and musculoskeletal structures.'),
    Test(name='Stool Culture', type='Microbiological Test', sampleType='Stool', instructions='Collect a fresh stool sample', price=round(random.uniform(20, 100), 2), description='Identifies bacteria, parasites, or other pathogens present in the stool to diagnose gastrointestinal infections.'),
    Test(name='Pap Smear (Cervical Screening)', type='Gynecological Test', sampleType='Cervical Cells', instructions='No sexual intercourse or douching 24 hours prior', price=round(random.uniform(20, 100), 2), description='Screens for cervical cancer by examining cervical cells for abnormalities or signs of infection.'),
    Test(name='Serum Cholesterol Test', type='Blood Test', sampleType='Blood', price=round(random.uniform(20, 100), 2), description='Measures cholesterol levels in the blood to assess cardiovascular risk and monitor cholesterol-lowering treatments.'),
    Test(name='Liver Function Tests', type='Blood Test', sampleType='Blood', price=round(random.uniform(20, 100), 2), description='Evaluates liver health by measuring liver enzymes, proteins, and other substances in the blood.'),
    Test(name='CT Scan (Computed Tomography)', type='Imaging Study', price=round(random.uniform(20, 100), 2), description='Uses X-rays to create detailed cross-sectional images of the body for diagnostic purposes.'),
    Test(name='Throat Swab', type='Microbiological Test', sampleType='Throat Swab', instructions='Collect a throat swab sample', price=round(random.uniform(20, 100), 2), description='Identifies bacteria or viruses causing throat infections or respiratory illnesses.'),
    Test(name='Bone Density Test (DEXA Scan)', type='Imaging Study', price=round(random.uniform(20, 100), 2), description='Measures bone mineral density to assess bone health and diagnose osteoporosis or bone-related conditions.'),
    Test(name='Hemoglobin A1c Test', type='Blood Test', sampleType='Blood', price=round(random.uniform(20, 100), 2), description='Measures average blood glucose levels over the past 2-3 months to assess long-term diabetes control.'),
    Test(name='Pregnancy Test (HCG)', type='Laboratory Test', sampleType='Urine or Blood', instructions='Collect a urine or blood sample', price=round(random.uniform(20, 100), 2), description='Detects the presence of human chorionic gonadotropin (HCG) hormone to confirm pregnancy.'),
    Test(name='Thyroid Ultrasound', type='Imaging Study', price=round(random.uniform(20, 100), 2), description='Uses sound waves to create images of the thyroid gland to evaluate its size, structure, and abnormalities.'),
    Test(name='C-reactive Protein Test (CRP)', type='Blood Test', sampleType='Blood', price=round(random.uniform(20, 100), 2), description='Measures CRP levels in the blood as a marker of inflammation and infection.'),
    Test(name='Spirometry (Lung Function Test)', type='Respiratory Test', price=round(random.uniform(20, 100), 2), description='Assesses lung function by measuring airflow and lung capacity to diagnose respiratory conditions.'),
    Test(name='Gastrointestinal Endoscopy', type='Endoscopic Procedure', price=round(random.uniform(20, 100), 2), description='Involves inserting a flexible tube with a camera into the digestive tract to visualize and diagnose gastrointestinal issues.'),
    Test(name='Allergy Testing (Skin Prick Test)', type='Allergy Test', sampleType='Skin Prick', instructions='Administered by applying allergens to the skin surface', price=round(random.uniform(20, 100), 2), description='Determines allergic reactions by observing skin responses to common allergens.'),
    Test(name='HIV Antibody Test', type='Blood Test', sampleType='Blood', instructions='Pre-test counseling may be required', price=round(random.uniform(20, 100), 2), description='Detects antibodies to HIV virus in the blood to diagnose HIV infection.'),
    Test(name='Colonoscopy', type='Endoscopic Procedure', price=round(random.uniform(20, 100), 2), description='Involves examining the colon and rectum using a flexible tube with a camera to screen for colorectal cancer and other conditions.'),
    Test(name='Thrombophilia Panel', type='Blood Test', sampleType='Blood', price=round(random.uniform(20, 100), 2), description='Analyzes blood clotting factors to assess the risk of thrombosis or blood clotting disorders.'),
    Test(name='Ultrasound Imaging (Abdominal Ultrasound)', type='Imaging Study', price=round(random.uniform(20, 100), 2), description='Uses sound waves to create images of abdominal organs like liver, gallbladder, kidneys, and pancreas.'),
    Test(name='Hepatitis Panel (Hepatitis A, B, C Tests)', type='Blood Test', sampleType='Blood', price=round(random.uniform(20, 100), 2), description='Tests for hepatitis A, B, and C viruses to diagnose hepatitis infections and assess liver health.'),
    Test(name='Prostate-Specific Antigen (PSA) Test', type='Blood Test', sampleType='Blood', price=round(random.uniform(20, 100), 2), description='Measures PSA levels in the blood to screen for prostate cancer and monitor prostate health.'),
    Test(name='Thyroid Biopsy (Fine Needle Aspiration)', type='Biopsy Procedure', sampleType='Tissue Sample', instructions='Performed under local anesthesia', price=round(random.uniform(20, 100), 2), description='Involves extracting a tissue sample from the thyroid gland for pathological analysis.'),
    Test(name='Glucose Tolerance Test (GTT)', type='Blood Test', sampleType='Blood', instructions='Requires fasting and glucose consumption', price=round(random.uniform(20, 100), 2), description='Measures blood glucose levels before and after consuming a glucose solution to diagnose diabetes or insulin resistance.'),
    Test(name='Lipid Profile (Cholesterol Panel)', type='Blood Test', sampleType='Blood', price=round(random.uniform(20, 100), 2), description='Measures cholesterol and triglyceride levels in the blood to assess cardiovascular risk and lipid metabolism.'),
    Test(name='Sleep Study (Polysomnography)', type='Sleep Study', price=round(random.uniform(20, 100), 2), description='Monitors sleep patterns, brain waves, breathing, and other parameters to diagnose sleep disorders like sleep apnea.'),
    Test(name='Hemoglobin Electrophoresis', type='Blood Test', sampleType='Blood', price=round(random.uniform(20, 100), 2), description='Separates and analyzes different types of hemoglobin in the blood to diagnose hemoglobinopathies like sickle cell disease.'),
    Test(name='Liver Biopsy', type='Biopsy Procedure', sampleType='Liver Tissue', instructions='Performed under local anesthesia', price=round(random.uniform(20, 100), 2), description='Involves extracting a tissue sample from the liver for pathological examination to diagnose liver diseases.'),
    Test(name='Lung Function Tests (Pulmonary Function Tests)', type='Respiratory Test', price=round(random.uniform(20, 100), 2), description='Assesses lung function by measuring airflow, lung volume, and gas exchange to diagnose respiratory conditions and monitor lung health.'),
    Test(name='Rapid Strep Test (Strep Throat Test)', type='Microbiological Test', sampleType='Throat Swab', instructions='Collect a throat swab sample', price=round(random.uniform(20, 100), 2), description='Rapidly detects streptococcal bacteria causing strep throat to guide antibiotic treatment.'),
    Test(name='Echocardiogram (Echo)', type='Cardiac Test', price=round(random.uniform(20, 100), 2), description='Uses ultrasound waves to create images of the heart to assess heart structure, function, and blood flow.'),
    Test(name='Prothrombin Time (PT) Test', type='Blood Test', sampleType='Blood', price=round(random.uniform(20, 100), 2), description='Measures the time it takes for blood to clot to assess bleeding disorders and monitor anticoagulant therapy.'),
    Test(name='Bone Marrow Biopsy', type='Biopsy Procedure', sampleType='Bone Marrow', instructions='Performed under local anesthesia', price=round(random.uniform(20, 100), 2), description='Involves extracting a sample of bone marrow from the hip bone for diagnostic evaluation of blood disorders or cancers.'),
    Test(name='Fecal Occult Blood Test (FOBT)', type='Stool Test', sampleType='Stool Sample', instructions='Collect a stool sample at home', price=round(random.uniform(20, 100), 2), description='Detects hidden blood in stool as a screening test for colorectal cancer and gastrointestinal bleeding.'),
    Test(name='Hemoglobinopathy Screening', type='Blood Test', sampleType='Blood', price=round(random.uniform(20, 100), 2), description='Screens for inherited hemoglobin disorders like thalassemia and sickle cell disease by analyzing hemoglobin variants in the blood.')
]
# for test in tests:
#     print(test.id)
# patient1 = Patient(firstName='Bob', lastName='The Builder', sex='Male', email='bob.builder@example.com', role='patient')
doc1 = HCW(firstName='John', lastName='Doe', email='john.doe@example.com', password='1', username='1', role='doctor')
# request = TestRequest(notes='this is a test request', requestedForId=patient1.id, requestedById=doc1.id)
# request.tests.append(tests[3])


# patient2 = Patient(firstName='Alice', lastName='Wonderland', sex='Female', email='alice.wonderland@example.com', role='patient')
# doc2 = HCW(firstName='Jane', lastName='Smith', email='jane.smith@example.com', role='doctor')
# nurse1 = HCW(firstName='Alice', lastName='Johnson', email='alice.johnson@example.com', role='nurse')
# nurse2 = HCW(firstName='Bob', lastName='Williams', email='bob.williams@example.com', role='nurse')
# pharmacist1 = HCW(firstName='Eva', lastName='Davis', email='eva.davis@example.com', role='pharmacist')
# pharmacist2 = HCW(firstName='Tom', lastName='Jones', email='tom.jones@example.com', role='pharmacist')
# admin = HCW(firstName='admin', username='admin', password='admin', role='admin')
# # patient3 = Patient(firstName='Charlie', lastName='Chaplin', sex='Male')
# # patient4 = Patient(firstName='Dorothy', lastName='Gale', sex='Female')
# # patient5 = Patient(firstName='Eddie', lastName='Murphy', sex='Male')
# # patient6 = Patient(firstName='Fiona', lastName='Apple', sex='Female')

# record1 = Record(diagnosis="Bronchitis", notes="Medication given", patientId=patient1.id, assessedById=doc1.id)
# record2 = Record(diagnosis="Hypertension", notes="Patient advised to monitor blood pressure regularly", patientId=patient1.id, assessedById=doc2.id)
# record3 = Record(notes="Insulin prescribed, dietary recommendations provided", patientId=patient1.id, assessedById=doc1.id)
# record4 = Record(diagnosis="Fractured leg", notes="Leg cast applied, follow-up appointment scheduled", patientId=patient2.id, assessedById=doc1.id)
# record5 = Record(diagnosis="Migraine", notes="Prescribed pain medication, advised to rest in a quiet environment", patientId=patient2.id, assessedById=doc2.id)
# record6 = Record(diagnosis="Common cold")

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
