# VitaSync Backend Project

This project is the backend part of the VitaSync application, designed to manage patient healthcare services efficiently. It provides a robust API for handling various aspects of patient healthcare, including appointments, prescriptions, procedures, records, vaccines, and vital information.

## Prerequisites

- Python 3.6 or higher
- Pip (Python package installer)
- Virtualenv (optional, for isolated Python environments)

## Installation

1. Clone the repository to your local machine:

```bash
git clone https://github.com/Hasbi-sabah/VitaSync.git
```

2. Navigate to the backend directory:

```bash
cd backend
```

3. Create a virtual environment (optional):

```bash
python -m venv env
```

4. Activate the virtual environment:

- On Windows:

```bash
env\Scripts\activate
```

- On Unix or MacOS:

```bash
source env/bin/activate
```

5. Install the required Python packages:

```bash
pip install -r requirements.txt
```

## Running the Backend

To run the backend server, use the following command:

```bash
python app.py
```

This will start the server, and you should be able to access the API endpoints at `http://localhost:5000` (or the port you have configured).


## API Routes

This section provides an overview of all available API endpoints in the VitaSync backend.

### Healthcare Workers (HCW)

- `GET /hcw_extended`: Retrieve extended information about all healthcare workers.
- `GET /hcw`: Retrieve detailed information about all healthcare workers.
- `GET /hcw_extended/<uuid:hcwId>`: Retrieve extended information about a specific healthcare worker.
- `GET /hcw/<uuid:hcwId>`: Retrieve detailed information about a specific healthcare worker.
- `POST /hcw`: Add a new healthcare worker to the system.
- `PUT /hcw/<uuid:hcwId>`: Update the information of a specific healthcare worker.
- `DELETE /hcw/<uuid:hcwId>`: Delete (archive) a healthcare worker from the system.

### Patients

- `GET /patient_extended`: Retrieve extended details of all patients.
- `GET /patient`: Retrieve details of all patients.
- `GET /patient/<uuid:patientId>`: Retrieve details of a specific patient.
- `GET /patient_extended/<uuid:patientId>`: Retrieve extended details of a specific patient.
- `POST /patient`: Add a new patient to the system.
- `PUT /patient/<uuid:patientId>`: Update patient details in the system.
- `DELETE /patient/<uuid:patientId>`: Delete a patient and associated user from the system.

### Authentication

- `POST /login`: Authenticate a user and return a JWT token.
- `POST /logout`: Logs User out.

### Patient's Medical Information

- `GET /patient/<uuid:patientId>/info`: Retrieve all medical information associated with a specific patient.
- `POST /patient/<uuid:patientId>/info`: Add new medical information for a specific patient.
- `GET /med_info/<uuid:infoId>`: Retrieve details of a specific medical information record.
- `PUT /med_info/<uuid:infoId>`: Update a specific medical information record's information.
- `DELETE /med_info/<uuid:infoId>`: Delete a specific medical information record.

### Drugs

- `GET /drug`: Retrieve a list of all drugs or filter drugs based on provided criteria.
- `GET /drug_lookup`: Lookup drugs based on name.
- `GET /drug/<uuid:drugId>`: Retrieve details of a specific drug identified by drugId.
- `POST /drug`: Add a new drug to the database.
- `PUT /drug/<uuid:drugId>`: Update details of a specific drug.
- `DELETE /drug/<uuid:drugId>`: Delete a drug from the database.

### Prescriptions

- `GET /prescription/<uuid:prescriptionId>/drug`: Retrieve all drugs associated with a specific prescription.
- `POST /prescription/<uuid:prescriptionId>/drug`: Add a new drug to a specific prescription.
- `GET /prescription/<uuid:prescriptionId>`: Retrieve details of a specific prescription.
- `POST /prescription/<uuid:prescriptionId>/fill`: Mark a specific prescription as filled.
- `PUT /prescription/<uuid:prescriptionId>`: Update a specific prescription's information.
- `DELETE /prescription/<uuid:prescriptionId>`: Delete a specific prescription.
- `GET /prescription_drug/<uuid:drugId>`: Retrieve details of a specific prescription drug.
- `PUT /prescription_drug/<uuid:drugId>`: Update a specific prescription drug's information.
- `DELETE /prescription_drug/<uuid:drugId>`: Delete a specific prescription drug.
- `GET /patient/<uuid:patientId>/prescription`: Retrieve all prescriptions associated with a specific patient.
- `POST /patient/<uuid:patientId>/prescription`: Add a new prescription for a specific patient.

### Records

- `GET /patient/<uuid:patientId>/record`: Retrieve all records associated with a specific patient.
- `POST /patient/<uuid:patientId>/record`: Add a new record for a specific patient.
- `GET /record/<uuid:recordId>`: Retrieve details of a specific record.
- `PUT /record/<uuid:recordId>`: Update a specific record's information.
- `DELETE /record/<uuid:recordId>`: Delete a specific record.

### Vitals

- `GET /patient/<uuid:patientId>/vital`: Retrieve all vital signs associated with a specific patient.
- `POST /patient/<uuid:patientId>/vital`: Add a new vital sign for a specific patient.
- `GET /vital/<uuid:vitalId>`: Retrieve details of a specific vital sign.
- `PUT /vital/<uuid:vitalId>`: Update a specific vital sign's information.
- `DELETE /vital/<uuid:vitalId>`: Delete a specific vital sign.

### Procedures

- `GET /patient/<uuid:patientId>/procedure`: Retrieve all procedures associated with a specific patient.
- `POST /patient/<uuid:patientId>/procedure`: Add a new procedure for a specific patient.
- `GET /procedure/<uuid:procedureId>`: Retrieve details of a specific procedure.
- `POST /procedure/<uuid:procedureId>/perform`: Mark a specific procedure as performed.
- `PUT /procedure/<uuid:procedureId>`: Update a specific procedure's information.
- `DELETE /procedure/<uuid:procedureId>`: Delete a specific procedure.

### Vaccines

- `GET /patient/<uuid:patientId>/vaccine`: Retrieve all vaccines associated with a specific patient.
- `POST /patient/<uuid:patientId>/vaccine`: Add a new vaccine for a specific patient.
- `GET /vaccine/<uuid:vaccineId>`: Retrieve details of a specific vaccine.
- `PUT /vaccine/<uuid:vaccineId>`: Update a specific vaccine's information.
- `DELETE /vaccine/<uuid:vaccineId>`: Delete a specific vaccine.

### Appointments

- `GET /hcw/<uuid:hcwId>/appointment`: Retrieve all appointments associated with a specific healthcare worker.
- `GET /patient/<uuid:patientId>/appointment`: Retrieve all appointments associated with a specific patient.
- `POST /patient/<uuid:patientId>/appointment`: Add a new appointment for a specific patient.
- `GET /appointment/<uuid:appointmentId>`: Retrieve details of a specific appointment.
- `PUT /appointment/<uuid:appointmentId>`: Update a specific appointment's information.
- `DELETE /appointment/<uuid:appointmentId>`: Delete a specific appointment.

## Email Notifications

The VitaSync API is designed to enhance the user experience by sending automated emails to users at various stages of their interaction with the system. These emails are sent to notify users about important events such as registration, appointment creation, rescheduling, and cancellation. This feature ensures that users are kept informed and can take necessary actions promptly.

### Registration Confirmation

Upon successful registration, users receive an email confirming their account creation. This email includes a welcome message, instructions on how to log in, and a link to verify their email address. Verification is a crucial step to ensure the security and authenticity of the user's account.

### Appointment Creation

When a user schedules an appointment, they receive a confirmation email. This email contains details about the appointment, including the date, time, and the doctor's contact information. It also includes a reminder to bring any necessary documents or information related to the patient's health.

### Appointment Rescheduling

In case an appointment needs to be rescheduled, users are notified via email. The email includes the new date and time of the appointment, along with any changes in the doctor's availability. It also provides a link to cancel the rescheduled appointment if needed.

### Appointment Cancellation

If a user decides to cancel an appointment, they can do so through the system. Upon cancellation, an email is sent to confirm the cancellation. This email includes the cancellation details and any potential refund information, if applicable.

### Appointment Reminders

The system sends appointment reminder emails to users to ensure they are aware of their upcoming appointments. These reminders are sent a day before the appointment and include all the necessary details to help users prepare for their visit.

### Email Configuration

The system uses SMTP (Simple Mail Transfer Protocol) for sending emails. The SMTP settings, including the server address, port, and authentication details, are configured in the `.env` file. This allows for easy customization and ensures that emails are sent securely and reliably.

### Security and Privacy

All emails sent by the system are encrypted using TLS (Transport Layer Security) to protect the privacy and security of the user's information. Additionally, the system complies with GDPR (General Data Protection Regulation) and other relevant data protection laws, ensuring that user data is handled responsibly and securely.

## Prescription Printing

The VitaSync API supports the functionality to print prescriptions directly. This feature is designed to streamline the process for healthcare professionals, allowing them to easily generate and print prescriptions for their patients.

### Features

- **Automated Prescription Generation**: Doctors can create prescriptions directly within the system, including details such as medication name, dosage, frequency, and duration.
- **Customizable Prescription Templates**: The system allows for the customization of prescription templates, enabling healthcare professionals to match the prescription format with their clinic's branding or specific requirements.
- **Direct PDF Generation**: Once a prescription is created, it can be generated as a PDF directly from the API. This eliminates the need for manual data entry or formatting, saving time and reducing errors.
- **Watermark for Filled Prescriptions**: If a prescription is marked as filled, a watermark is added to the printed prescription to indicate its status. This feature helps prevent the reuse of prescriptions that have already been dispensed.

### Usage

To generate a prescription PDF, a healthcare professional would make a GET request to the `/print_prescription/<uuid:id>` endpoint, providing the prescription ID as a parameter. The system will then generate a formatted prescription PDF based on a template and return it as an attachement.

This feature is particularly useful for healthcare professionals who frequently need to print prescriptions for their patients, as it saves time and reduces the risk of errors compared to manual printing.

## QR Code Generation

The VitaSync API includes a feature to generate QR codes for various purposes, such as tracking prescriptions or appointments. This functionality is particularly useful for enhancing the traceability and security of healthcare records.

### API Endpoint

- `GET /get_qr/<uuid:id>`: Generates a QR code for the given ID and returns the URL to the QR code image. This endpoint requires authentication and role-based permissions to ensure that only authorized users can access and generate QR codes.

### Features

- **Unique Identifiers**: QR codes can be generated for any object within the system that requires a unique identifier, such as prescriptions, appointments, or patient records.
- **Easy Integration**: The generated QR codes can be easily integrated into printed documents or digital interfaces, providing a convenient way to access and verify information.
- **Security**: The QR code generation process is secure, ensuring that the data encoded within the QR codes is protected and can only be accessed by authorized users.

### Usage

To generate a QR code, a healthcare professional would make a GET request to the `/get_qr/<uuid:id>` endpoint, providing the ID of the object for which the QR code is generated. The system will then create a QR code image and return it as an attachment.

This feature is particularly useful for healthcare professionals who need to quickly and securely access and verify information, such as prescription details or appointment records.

## Authentication and Authorization

The VitaSync backend employs a token-based authentication system to secure its API endpoints. This system uses JSON Web Tokens (JWT) to authenticate users and manage their sessions. Upon successful login, users receive a token that must be included in the header of subsequent requests to access protected endpoints.

The backend also implements role-based access control (RBAC) to manage permissions. There are several roles defined within the system, each with specific permissions:

- **Admin**: Has full access to all API endpoints, including creating, reading, updating, and deleting records for all entities.
- **Doctor**: Can access and manage patient records, prescriptions, and procedures.
- **Nurse**: Can access and manage patient records and procedures.
- **Patient**: Can view their own records, prescriptions, and appointments. They cannot create or delete records but can update their own profile.
- **Pharmacist**: Can access and manage prescriptions. They can view prescription details, update prescription status (e.g., filled, not filled), and cannot access patient records or other sensitive information.

Each role has specific permissions that determine which API endpoints they can access. For example, a Doctor can access all endpoints related to prescriptions and procedures but cannot access endpoints for managing other users or system settings.

Paths are protected by token-based authentication, and role-based permissions are enforced on each request to ensure that users can only access the resources and perform actions that their role permits.

### Archiving vs. Deleting

In the VitaSync system, when an element is deleted, it is not permanently removed from the database. Instead, it is archived. Archiving is a process where records are marked as inactive or hidden from regular operations but are still retained in the database for historical purposes and potential future use. This approach ensures that no data is lost and that the integrity of the system is maintained.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For any questions or concerns, please open an issue on the GitHub repository.