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


doc = HCW(role='doctor')
print('doc', doc.id)
patient1 = Patient(firstName='Bob', lastName='The Builder', sex='Male')
patient2 = Patient(firstName='Alice', lastName='Wonderland', sex='Female')
patient3 = Patient(firstName='Charlie', lastName='Chaplin', sex='Male')
patient4 = Patient(firstName='Dorothy', lastName='Gale', sex='Female')
patient5 = Patient(firstName='Eddie', lastName='Murphy', sex='Male')
patient6 = Patient(firstName='Fiona', lastName='Apple', sex='Female')
# vitals1 = Vital(takenById=doc.id, takenForId=patient.id)
# vitals2 = Vital(takenById=doc.id, takenForId=patient.id)

# info = MedInfo(patientId=patient.id)

# proc = Procedure(patientId=patient.id, prescribedById=doc.id)

# drug1 = Drug()
# drug2 = Drug()
# drug3 = Drug()

# vaccine1 = Vaccine(administeredById=doc.id, administeredForId=patient.id, drugId=drug1.id)
# vaccine2 = Vaccine(administeredById=doc.id, administeredForId=patient.id, drugId=drug1.id)

# prsc = Prescription(prescribedById=doc.id, prescribedForId=patient.id)
# med1 = DrugPrescribed(drugId=drug1.id, prescriptionId = prsc.id)
# med2 = DrugPrescribed(drugId=drug2.id, prescriptionId = prsc.id)
# med3 = DrugPrescribed(drugId=drug3.id, prescriptionId = prsc.id)
# med4 = DrugPrescribed(drugId=drug3.id)
# med4.prescriptionId = prsc.id

# prsc = Prescription(prescribedById=doc.id, prescribedForId=patient.id)
# med1 = DrugPrescribed(drugId=drug1.id, prescriptionId = prsc.id)
# med2 = DrugPrescribed(drugId=drug2.id, prescriptionId = prsc.id)
# med3 = DrugPrescribed(drugId=drug3.id, prescriptionId = prsc.id)
# med4 = DrugPrescribed(drugId=drug3.id)
# med4.prescriptionId = prsc.id

# record1 = Record(patientId=patient.id, vaccineId=vaccine1.id,
#                  vitalsId=vitals1.id, procedureId=proc.id,
#                  prescriptionId=prsc.id, assessedById=doc.id)

# print(doc == record1.assessedBy)