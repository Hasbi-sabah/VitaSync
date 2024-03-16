from flask import Blueprint

api = Blueprint('api', __name__, url_prefix='/api')

from api.drug.drug import *
from api.hcw.hcw import *
from api.patient.patient import *
from api.patient.patient_record import *
from api.patient.patient_prescription import *
from api.prescription.prescription import *
from api.base import *
from api.access.accessHandle import *
from api.record.record import *