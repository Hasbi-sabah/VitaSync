# VitaSync Project

VitaSync is a comprehensive healthcare management system designed to streamline and digitize healthcare processes. This document provides an overview of the VitaSync project, including its backend and frontend components, key features, and how to get started with both.

## Overview

VitaSync aims to provide a centralized system for managing healthcare-related information and appointments. It includes functionalities for handling patients, healthcare workers (HCW), prescriptions, medical information, appointments, procedures, records, vaccines, and more. The system is divided into two main components:

- **Backend**: Handles data processing, storage, and retrieval. It's built with Python and Flask, providing a robust and scalable backend infrastructure.
- **Frontend**: Comprises several applications tailored for different user roles within the healthcare system, including authentication, documentation, nurses, pharmacists, and patients. It's developed using React, ensuring a responsive and user-friendly interface.

## Key Features

- **Centralized Healthcare Management**: Streamlines the management of patient information, appointments, prescriptions, and medical records.
- **Role-Based Access Control**: Ensures that users have access only to the functionalities relevant to their role, enhancing security and user experience.
- **Comprehensive Patient Management**: Supports the creation, modification, and management of patient profiles, medical records, and prescriptions.
- **Efficient Appointment Scheduling**: Facilitates the scheduling and management of appointments, ensuring timely and efficient healthcare services.
- **Advanced Search and Filtering**: Provides powerful search and filtering capabilities for accessing patient information and medical records.

## Getting Started

### Prerequisites

Ensure you have the following installed on your system:

- Node.js (v14.0.0 or later)
- npm (v6.14.0 or later)
- Python (v3.8 or later)
- Flask (v1.1.2 or later)

Ensure your system has more than 2GB available in RAM

### Backend Setup

1. Navigate to the `backend` directory in your project root.
2. Install the dependencies by running `pip install -r requirements.txt`.
3. Start the Flask server by running `python run.py`.

### Frontend Setup

1. Navigate to the `frontend` directory in your project root.
2. Install the dependencies for each application by running `npm install` in each application's directory.
3. Start each frontend application by navigating to its directory and running `npm start`.
(optional)
3. make build.


## API Routes

This section provides an overview of all available API endpoints in the VitaSync backend.

### home
- `GET /`: json response about status and version of api

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

The VitaSync API is designed to enhance the user experience by sending automated emails to users at various stages of their interaction with the system. These emails are sent to notify users about important events such as registration, appointment creation, rescheduling, and cancellation. This feature ensures that users are kept informed and can take necessary actions promptly, backed by a checker that runs both when triggered and in a loop.

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

### Application Details

#### Auth

- **Purpose**: Serves as the gateway to the VitaSync system, handling user authentication and session management. It plays a crucial role in ensuring secure access to the various healthcare management applications.
- **Features**:
 - **User Registration and Login**: Allows new users to sign up and existing users to log in, providing a seamless entry point into the VitaSync ecosystem.
 - **Role-Based Access Control**: Directs users to the appropriate application based on their role (e.g., Nurse, Patient, Pharmacist) after successful authentication. This ensures that users have access only to the functionalities relevant to their role, enhancing security and user experience.
 - **Redirection to Appropriate App**: After successful authentication, the Auth platform intelligently redirects users to the specific application tailored to their role within the healthcare system. This feature streamlines the user experience by providing direct access to the relevant functionalities without unnecessary navigation.

The Auth platform is designed to be the first point of contact for users, setting the stage for a secure and efficient healthcare management experience.

#### Doc

- **Purpose**: Provides access to healthcare documentation and resources, serving as a comprehensive tool for healthcare professionals to manage patient information, records, and prescriptions.
- **Features**:
 - **Patient Profile Management**: Allows healthcare professionals to create and manage patient profiles, including personal information, medical history, and contact details.
 - **QR Code Scanning**: Enables the scanning of QR codes to quickly search for patient information, streamlining the process of accessing patient data.
 - **Search Bar**: Offers a powerful search functionality, allowing healthcare professionals to search for patients by ID.
 - **Patient Information Modification**: Facilitates the updating of patient information, including allergies, vitals, and other health-related data, ensuring that patient records are always up-to-date.
 - **Record Management**: Provides tools for checking existing patient records, adding new records, and managing prescriptions, ensuring that all patient information is accurately documented and accessible.
 - **Diagnosis and Vaccines Management**: Allows the addition of diagnoses, vaccines, and follow-up appointments to patient records, supporting comprehensive patient care.
 - **Sidebar Options**:
   - **Dashboard**: Displays today's appointments, providing a quick overview of the day's schedule.
   - **Search HCW**: Enables the search for other healthcare workers, with the ability to filter results by prescription and role, facilitating collaboration and information sharing among the healthcare team.

The Doc platform is designed to support healthcare professionals in efficiently managing patient information, records, and prescriptions, ensuring that patient care is comprehensive and well-documented.

#### Nurse

- **Purpose**: Facilitates nurses in managing patient information and appointments, with a focus on day-to-day care and record-keeping.
- **Features**:
 - **Patient Profile Management**: Allows nurses to create and manage patient profiles, including personal information, medical history, and contact details.
 - **QR Code Scanning**: Enables the scanning of QR codes to quickly search for patient information, streamlining the process of accessing patient data.
 - **Search Bar**: Offers a powerful search functionality, allowing nurses to search for patients by name, ID, or other relevant criteria.
 - **Patient Information Modification**: Facilitates the updating of patient information, including allergies, vitals, and other health-related data, ensuring that patient records are always up-to-date.
 - **Record Management**: Provides tools for checking existing patient records, adding new records, and managing medical information, ensuring that all patient information is accurately documented and accessible.
 - **Procedure Management**: Allows nurses to mark procedures as performed, documenting the completion of treatments and interventions.
 - **Patient Pinning**: Enables nurses to pin patient profiles for easy access, streamlining the management of frequently visited patients.
 - **Sidebar Options**:
   - **Dashboard**: Displays pinned patients in a list, providing a quick overview of the nurses' most frequently visited patients.
   - **Search HCW**: Enables the search for other healthcare workers, with the ability to filter results by prescription and role, facilitating collaboration and information sharing among the healthcare team.

The Nurse platform is designed to support nurses in efficiently managing patient information, records, and day-to-day care, ensuring that patient care is comprehensive and well-documented.

#### Pharmacist

- **Purpose**: Supports pharmacists in managing prescriptions and medications, ensuring that medications are accurately filled and dispensed according to prescriptions.
- **Features**:
 - **Patient Profile Management**: Allows pharmacists to create and manage patient profiles, including personal information, medical history, and contact details.
 - **QR Code Scanning**: Enables the scanning of QR codes to quickly search for patient information, streamlining the process of accessing patient data.
 - **Search Bar**: Offers a powerful search functionality, allowing pharmacists to search for patients by name, ID, or other relevant criteria.
 - **Vital Creation**: Facilitates the updating of patient vitals, ensuring that health-related data is accurately documented and accessible.
 - **Prescription Management**: Allows pharmacists to mark prescriptions as filled, ensuring that medications are accurately dispensed according to prescriptions.
 - **Sidebar Options**:
   - **Dashboard**: Provides access to search bar, QR code scanning, and patient creation tools, streamlining the process of managing patient information and prescriptions.
   - **Search HCW**: Enables the search for other healthcare workers, with the ability to filter results by prescription and role, facilitating collaboration and information sharing among the healthcare team.

The Pharmacist platform is designed to support pharmacists in efficiently managing prescriptions and medications, ensuring that patient care is comprehensive and well-documented.

#### Patient

- **Purpose**: Allows patients to access and manage their healthcare information.
- **Features**:
 - **View Personal Health Information**: Patients can view their personal health information, including vitals, medical history, and allergies.
 - **Prescription Information**: Provides access to prescription information, including the latest unfilled prescriptions with the option to print them.
 - **Records**: Allows patients to view their own medical records, ensuring transparency and accessibility to their health history.
 - **Sidebar Options**:
   - **Dashboard**: Displays the patient's latest vitals and medical information, including allergies, providing a quick overview of their health status.
   - **Prescription**: Offers a dedicated section for viewing prescriptions and the latest unfilled prescriptions, with a print option for convenience.
   - **Records**: Provides access to the patient's medical records, ensuring they can review their health history.
   - **Search HCW**: Enables the search for healthcare workers, with the ability to view their contact information and redirect to Google Maps for location details, facilitating easy access to healthcare providers.

The Patient platform is designed to support patients in efficiently accessing and managing their healthcare information, ensuring that they have a clear understanding of their health status and can easily navigate their healthcare journey.

## License

This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for details.

## Contact

For any questions or concerns, please open an issue on the GitHub repository.
