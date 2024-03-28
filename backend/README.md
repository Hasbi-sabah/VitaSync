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

## API Endpoints

The backend provides a comprehensive set of API endpoints for managing patient healthcare data. Here are some examples of the main endpoints:

### Patients

- `GET /api/patients`: Retrieve a list of all patients.
- `POST /api/patients`: Create a new patient record.
- `GET /api/patients/{id}`: Retrieve a specific patient record by ID.
- `PUT /api/patients/{id}`: Update a specific patient record by ID.
- `DELETE /api/patients/{id}`: Delete a specific patient record by ID.

### Prescriptions

- `GET /api/prescriptions`: Retrieve a list of all prescriptions.
- `POST /api/prescriptions`: Create a new prescription record.
- `GET /api/prescriptions/{id}`: Retrieve a specific prescription record by ID.
- `POST /api/prescriptions/{id}/fill`: Flags a prescription record as filled.
- `PUT /api/prescriptions/{id}`: Update a specific prescription record by ID.
- `DELETE /api/prescriptions/{id}`: Delete a specific prescription record by ID.

### Vaccines

- `GET /api/vaccines`: Retrieve a list of all vaccines.
- `POST /api/vaccines`: Create a new vaccine record.
- `GET /api/vaccines/{id}`: Retrieve a specific vaccine record by ID.
- `PUT /api/vaccines/{id}`: Update a specific vaccine record by ID.
- `DELETE /api/vaccines/{id}`: Delete a specific vaccine record by ID.

### Procedures

- `GET /api/procedures`: Retrieve a list of all procedures.
- `POST /api/procedures`: Create a new procedure record.
- `GET /api/procedures/{id}`: Retrieve a specific procedure record by ID.
- `POST /api/procedures/{id}/perform`: Flags a specific procedure record as performs.
- `PUT /api/procedures/{id}`: Update a specific procedure record by ID.
- `DELETE /api/procedures/{id}`: Delete a specific procedure record by ID.

### Records

- `GET /api/records`: Retrieve a list of all medical records.
- `POST /api/records`: Create a new medical record.
- `GET /api/records/{id}`: Retrieve a specific medical record by ID.
- `PUT /api/records/{id}`: Update a specific medical record by ID.
- `DELETE /api/records/{id}`: Delete a specific medical record by ID.

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

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For any questions or concerns, please open an issue on the GitHub repository.