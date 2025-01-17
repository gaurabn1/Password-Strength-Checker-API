# API Documentation with Swagger

This project provides a set of API endpoints for user authentication and password strength checking. The Swagger UI allows you to see all available endpoints, their parameters, and their responses, and test them directly from your browser.

## How to Access the API Documentation

### 1. **Run the Project**:
   - Ensure your Django project is running. If you're running it locally, navigate to your project directory and run the following command to start the server:

   ```bash
   python manage.py runserver
```
### 2. **Access Swagger UI**:
Open your browser and navigate to the following URL to access the Swagger UI:
```bash
http://127.0.0.1:8000/api/swagger/
```

This will bring up the Swagger UI, where you can explore and interact with all available API endpoints.

### 3. **Using the API in Swagger UI**:

   - **Explore Available Endpoints**: Once you're on the Swagger UI, you will see a list of available API endpoints. These are categorized by their functionality.

   - **Sending Requests**: You can click on any endpoint to expand it, view its description, parameters, and responses. You can send test requests directly from Swagger UI and see the responses without needing to write any code.

## API Endpoints

### 4. **Signup API**:

   - **Endpoint**: `POST /api/signup/`
   - **Description**: This endpoint allows users to sign up by providing the following fields: `first_name`, `last_name`, `username`, `email`, `password`, and `password2`.

   - **Request Body Example**:

     ```json
     {
       "first_name": "John",
       "last_name": "Doe",
       "username": "johndoe",
       "email": "johndoe@example.com",
       "password": "password123",
       "password2": "password123"
     }
     ```

   - **Responses**:
     - `200 OK`: When the user is successfully created.
     - `400 Bad Request`: If there are any validation errors (e.g., missing fields or passwords not matching).
   
   - **Swagger UI**: You can interact with this API by entering values into the fields and clicking on the "Execute" button.

### 5. **Token Authentication API**:

   - **Endpoint**: `POST /api/token/`
   - **Description**: This endpoint allows users to obtain a token after providing their username and password.

   - **Request Body Example**:

     ```json
     {
       "username": "johndoe",
       "password": "password123"
     }
     ```

   - **Responses**:
     - `200 OK`: The user receives an authentication token in response.
     - `400 Bad Request`: If the credentials are invalid or missing.
   
   - **Swagger UI**: You can use this endpoint by providing your username and password fields in the request body and clicking "Execute" to obtain a token.

### 6. **Password Strength Checker API**:

   - **Endpoint**: `POST /api/password-strength-checker/`
   - **Description**: This endpoint allows users to check the strength of a password. It will assess the password’s strength and return feedback on how to improve it.

   - **Request Body Example**:

     ```json
     {
       "password": "password123"
     }
     ```

   - **Responses**:
     - `200 OK`: If the password strength is returned successfully with recommendations for improvement.
     - `400 Bad Request`: If the password field is missing or invalid.

### 7. **Getting Started with Authentication**:

   - **Token Authentication**: For endpoints requiring authentication (like the password strength checker), you need to provide the token in the `Authorization` header.

     **Example**:

     ```
     Authorization: Token <your-token-here>
     ```

   - **Token Generation**: To authenticate, use the `/api/token/` endpoint to obtain a token, and then provide that token when making requests to the password strength checker or other protected endpoints.
