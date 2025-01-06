# Django Survey API

## Overview
This project is a Django REST API for creating and managing surveys, questions, answer options, iterations (user attempts), and answers. It supports nested relationships and dynamic data handling for real-time survey management.

## Features
- **Survey Management**: Create, retrieve, update, and delete surveys.
- **Nested Questions**: Add and manage questions under specific surveys.
- **Answer Options**: Define multiple answer options for each question.
- **User Iterations**: Track survey completions by different users.
- **Dynamic Status**: Iterations dynamically indicate whether they are completed or incomplete.
- **Freitext Field**: Users can optionally provide additional information while answering questions.
- **Interactive API Documentation**: Explore and test endpoints using Swagger.

## API Documentation
Interactive API documentation is available:

- **Swagger UI**: [http://127.0.0.1:8000/swagger/](http://127.0.0.1:8000/swagger/)
- **ReDoc**: [http://127.0.0.1:8000/redoc/](http://127.0.0.1:8000/redoc/)

These pages allow you to explore the API, test endpoints interactively, and view the OpenAPI specification.

## Main API Endpoints
| Endpoint                                                      | Method | Description                         |
|---------------------------------------------------------------|--------|-------------------------------------|
| `/surveys/`                                                   | GET    | List all surveys                    |
| `/surveys/`                                                   | POST   | Create a new survey                 |
| `/surveys/{survey_id}/questions/`                             | GET    | List questions in a survey          |
| `/surveys/{survey_id}/questions/`                             | POST   | Add a new question to a survey      |
| `/surveys/{survey_pk}/questions/{question_pk}/answeroptions/` | GET    | List answer options for a question  |
| `/surveys/{survey_pk}/questions/{question_pk}/answeroptions/` | POST   | Add an answer option to a question  |
| `/iterations/`                                                | GET    | List all iterations                 |
| `/iterations/`                                                | POST   | Create a new iteration              |
| `/iterations/{iteration_id}/answers/`                         | POST   | Add an answer to an iteration       |


## Requirements
- Python 3.9+
- Django 5.1.4
- Django REST Framework
- drf-yasg (for API documentation)

## Setup Instructions
1. **Clone the Repository**:
```bash
git clone https://github.com/your-repo/django-survey-api.git
cd django-survey-api
```

2. **Install Dependencies**:
```bash
pip install -r requirements.txt
```

3. **Navigate to the recruit Folder to run the following commands**:
```bash
cd recruit
```

4. **Configure a relational database (e.g. PostgreSQL) based on the file recruit/settings.py.**:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_database_name',
        'USER': 'your_database_user',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',  # Or the IP of your database server
        'PORT': '5432',       # Default PostgreSQL port
    }
}
```

5. **Apply Migrations**:
```bash
python manage.py migrate
```

6. **Run the Development Server**:
```bash
python manage.py runserver
```

7. **Access the API**:
API Base URL: http://127.0.0.1:8000/

## Running Tests
**Ensure migrations are applied**:
```bash
python manage.py migrate
```

**Run the tests**:
```bash
python manage.py test
```

# **Example Usage**

## **Create a Survey**

### **For Windows Command Prompt**:
```bash
curl -X POST "http://127.0.0.1:8000/surveys/" -H "Content-Type: application/json" -d "{\"name\": \"Customer Feedback Survey\", \"key\": \"123e4567-e89b-12d3-a456-426614174000\"}"
```

### **For Unix/Linux Shells**:
```bash
curl -X POST "http://127.0.0.1:8000/surveys/" -H "Content-Type: application/json" -d '{"name": "Customer Feedback Survey", "key": "123e4567-e89b-12d3-a456-426614174000"}'
```

## **Add a Question to a Survey**
### **For Windows Command Prompt**:
```bash
curl -X POST "http://127.0.0.1:8000/surveys/123e4567-e89b-12d3-a456-426614174000/questions/" -H "Content-Type: application/json" -d "{\"name\": \"Question 1\", \"text\": \"How satisfied are you with our service?\"}"
```

### **For Unix/Linux Shells**:
```bash
curl -X POST "http://127.0.0.1:8000/surveys/123e4567-e89b-12d3-a456-426614174000/questions
```


# **Error Handling**
**All endpoints return appropriate HTTP status codes with detailed error messages for invalid requests.**

**Examples**:
- 400 Bad Request: Missing required fields in the request.
- 404 Not Found: Resource not found.
- 500 Internal Server Error: Unexpected server error.

**Sample Response**:
```json
{
    "detail": "Resource not found."
}
```

### **Technical Key Features**
```markdown
## Features
- [x] **Survey Management**: Create, retrieve, update, and delete surveys.
- [x] **Nested Questions**: Add and manage questions under specific surveys.
- [x] **Answer Options**: Define multiple answer options for each question.
- [x] **User Iterations**: Track survey completions by different users.
- [x] **Dynamic Status**: Iterations dynamically indicate whether they are completed or incomplete.
- [x] **Freetext Field**: Users can optionally provide additional information while answering questions.
- [x] **Interactive API Documentation**: Explore and test endpoints using Swagger.