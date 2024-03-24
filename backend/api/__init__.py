from flask import Blueprint

api = Blueprint('api', __name__, url_prefix='/api')

from api.base import *
from api.access.accessHandle import *
from api.smtp.emailsHandler import *

from api.drug.drug import *

from api.hcw.hcw import *

from api.patient.patient import *
from api.patient.patient_appointment import *
from api.patient.patient_prescription import *
from api.patient.patient_procedure import *
from api.patient.patient_record import *
from api.patient.patient_vaccine import *
from api.patient.patient_vital import *

from api.prescription.prescription_drug import *
from api.prescription.prescription import *
from api.prescription_drug.drug import *

from api.procedure.procedure import *

from api.record.record import *

from api.vaccine.vaccine import *

from api.vital.vital import *
