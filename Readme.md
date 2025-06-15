
#### **Overview**
This is a FastAPI-based Event Management API that allows users to manage events, users, and registrations. The API provides endpoints for creating, updating, retrieving, and deleting users, as well as managing user statuses and event registrations.

---

#### **Features**
- **User Management**:
  - Create new users.
  - Retrieve all users.
  - Update user details.
  - Update user status (active/inactive).
  - Delete users.

- **Event Management**:
  - Create, update, and retrieve events.
  - Check event availability (open/closed).

- **Registration Management**:
  - Register users for events.
  - Prevent duplicate registrations for the same event.
  - Retrieve all registered users.

---

#### **Technologies Used**
- **Framework**: FastAPI
- **Language**: Python
- **Database**: In-memory dictionary (for simplicity)
- **Dependencies**:
  - `fastapi`
  - `pydantic`
  - `uvicorn`

---

#### **Installation**
1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/event-management-api.git
   cd event-management-api
   ```

2. Create a virtual environment and activate it:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install fastapi uvicorn
   ```

4. Run the application:
   ```bash
   uvicorn main:app --reload
   ```

5. Access the API documentation at:
   - Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
   - ReDoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

#### **API Endpoints**

##### **User Endpoints**
- **GET** `/user`: Retrieve all users.
- **POST** `/user`: Create a new user.
- **PUT** `/user/{id}`: Update user details by ID.
- **PUT** `/user/{id}/status`: Update user status (active/inactive).
- **DELETE** `/user/{id}`: Delete a user by ID.

##### **Event Endpoints**
- **GET** `/event`: Retrieve all events.
- **POST** `/event`: Create a new event.
- **PUT** `/event/{id}`: Update event details by ID.

##### **Registration Endpoints**
- **GET** `/registration`: Retrieve all registered users.
- **POST** `/registration/{user_id}`: Register a user for an event.

---

#### **Example Request**
**Create a User**:
```bash
POST /user
Content-Type: application/json

{
    "id": 1,
    "name": "John Doe",
    "email": "john.doe@example.com",
    "is_active": true
}
```

**Response**:
```json
{
    "message": "User Created Successfully",
    "details": {
        "id": 1,
        "name": "John Doe",
        "email": "john.doe@example.com",
        "is_active": true
    }
}
```

---

#### **Future Improvements**
- Add persistent database support (e.g., PostgreSQL, MongoDB).
- Implement authentication and authorization.
- Add pagination for large datasets.
- Improve error handling and validation.

---

#### **Contributing**
1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add feature-name"
   ```
4. Push to your branch:
   ```bash
   git push origin feature-name
   ```
5. Open a pull request.

---

#### **License**
This project is licensed under the MIT License. See the `LICENSE` file for details.

