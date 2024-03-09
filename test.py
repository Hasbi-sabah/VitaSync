from models.hcw import HCW
from models.drug import Drug
from models.drug_version import DrugVersion
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
patient = Patient()
print('patient', patient.id)

vitals1 = Vital(takenById=doc.id, takenForId=patient.id)
vitals2 = Vital(takenById=doc.id, takenForId=patient.id)

info = MedInfo(patientId=patient.id)

proc = Procedure(patientId=patient.id, prescribedById=doc.id)

drug1 = Drug()
drug2 = Drug()
drug3 = Drug()
version1 = DrugVersion(drugId=drug1.id)
version2 = DrugVersion(drugId=drug2.id)
version3 = DrugVersion(drugId=drug3.id)
version4 = DrugVersion(drugId=drug3.id)

vaccine1 = Vaccine(administeredById=doc.id, administeredForId=patient.id, drugId=drug1.id, drugVersionId=version1.id)
vaccine2 = Vaccine(administeredById=doc.id, administeredForId=patient.id, drugId=drug1.id, drugVersionId=version1.id)

prsc = Prescription(prescribedById=doc.id, prescribedForId=patient.id)
med1 = DrugPrescribed(drugId=drug1.id, drugVersionId=version1.id, prescriptionId = prsc.id)
med2 = DrugPrescribed(drugId=drug2.id, drugVersionId=version2.id, prescriptionId = prsc.id)
med3 = DrugPrescribed(drugId=drug3.id, drugVersionId=version3.id, prescriptionId = prsc.id)
med4 = DrugPrescribed(drugId=drug3.id, drugVersionId=version4.id)
med4.prescriptionId = prsc.id

prsc = Prescription(prescribedById=doc.id, prescribedForId=patient.id)
med1 = DrugPrescribed(drugId=drug1.id, drugVersionId=version1.id, prescriptionId = prsc.id)
med2 = DrugPrescribed(drugId=drug2.id, drugVersionId=version2.id, prescriptionId = prsc.id)
med3 = DrugPrescribed(drugId=drug3.id, drugVersionId=version3.id, prescriptionId = prsc.id)
med4 = DrugPrescribed(drugId=drug3.id, drugVersionId=version4.id)
med4.prescriptionId = prsc.id

record1 = Record(patientId=patient.id, vaccineId=vaccine1.id,
                 vitalsId=vitals1.id, procedureId=proc.id,
                 prescriptionId=prsc.id, assessedById=doc.id)

print(doc == record1.assessedBy)