# VitaSync Frontend

VitaSync is a comprehensive healthcare management system designed to streamline and digitize healthcare processes. This document outlines the frontend components of VitaSync, including how to start each application and a brief overview of their functionalities.

## Overview

VitaSync's frontend is divided into five main applications, each tailored for different user roles within the healthcare system. These applications include:

- **Auth**: Handles authentication and user management.
- **Doc**: Provides documentation-related functionalities.
- **Nurse**: Designed for nurses to manage patient information and appointments.
- **Pharmacist**: Offers functionalities for pharmacists to manage prescriptions and medications.
- **Patient**: Allows patients to access their healthcare information and manage appointments.

## Getting Started

### Prerequisites

Ensure you have the following installed on your system:

- Node.js (v14.0.0 or later)
- npm (v6.14.0 or later)

### Installation

1. Navigate to the `frontend` directory in your project root.
2. Install the dependencies for each application by running `npm install` in each application's directory.

### Starting the Applications

Each frontend application can be started separately. Navigate to the directory of the application you wish to start and run the following command:

```bash
npm start
```

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

This project is licensed under the MIT License. See the [LICENSE](../LICENSE) file for details.

## Contact

For any questions or concerns, please open an issue on the GitHub repository.