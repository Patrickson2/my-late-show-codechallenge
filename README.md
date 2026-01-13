# LATE SHOWS CODE CHALLENGE

A comprehensive Flask REST API for managing late show episodes, guests, and their appearances. This application provides a complete backend solution for tracking television show data with full CRUD operations and proper data relationships.

## Project Overview

This project implements a many-to-many relationship between Episodes and Guests through an Appearance join table. The API allows users to manage show episodes, celebrity guests, and track guest appearances with ratings. Built with Flask and SQLAlchemy, it follows RESTful principles and includes proper error handling and data validation.

## Features

- **Episode Management**: Create and retrieve episodes with unique dates and episode numbers
- **Guest Management**: Store guest information including names and occupations
- **Appearance Tracking**: Record guest appearances on specific episodes with user ratings
- **Data Relationships**: Proper many-to-many relationships with cascade delete functionality
- **Input Validation**: Server-side validation for rating values (1-5 scale)
- **Error Handling**: Comprehensive error responses with appropriate HTTP status codes
- **JSON Serialization**: Clean JSON responses with controlled serialization depth
- **Database Migrations**: Flask-Migrate integration for database schema management

## Technical Architecture

### Database Schema
The application uses a three-table relational database design:
- **Episodes Table**: Stores episode information (id, date, number)
- **Guests Table**: Stores guest information (id, name, occupation)
- **Appearances Table**: Join table linking episodes and guests with ratings

### API Design
Follows RESTful conventions with proper HTTP methods and status codes:
- GET requests for data retrieval
- POST requests for resource creation
- Appropriate status codes (200, 201, 400, 404)
- JSON request/response format

## Prerequisites

- Python 3.8 or higher
- Pipenv for dependency management
- SQLite (included with Python)
- Postman or similar API testing tool (recommended)

## Installation & Setup

### 1. Clone the Repository
```bash
git clone <repository-url>
cd Late-shows
```

### 2. Set Up Virtual Environment
```bash
pipenv install
pipenv shell
```

### 3. Install Dependencies
The following packages will be installed:
- Flask: Web framework
- Flask-SQLAlchemy: ORM for database operations
- Flask-Migrate: Database migration management
- SQLAlchemy-Serializer: JSON serialization for models

### 4. Initialize Database
```bash
# Initialize migration repository
flask db init

# Create initial migration
flask db migrate -m "Initial migration with Episode, Guest, and Appearance models"

# Apply migrations to database
flask db upgrade
```

### 5. Seed Database with Sample Data
```bash
python seed.py
```
This will populate the database with sample episodes, guests, and appearances for testing.

### 6. Start the Application
```bash
python app.py
```
The API server will start on `http://localhost:5555`

## API Documentation

### Base URL
```
http://localhost:5555
```

### Endpoints Overview

| Method | Endpoint | Description | Status Codes |
|--------|----------|-------------|-------------|
| GET | `/episodes` | Retrieve all episodes | 200 |
| GET | `/episodes/<id>` | Retrieve specific episode with appearances | 200, 404 |
| GET | `/guests` | Retrieve all guests | 200 |
| POST | `/appearances` | Create new appearance | 201, 400 |

### Detailed Endpoint Documentation

#### 1. GET /episodes
**Description**: Retrieves all episodes in the database

**Response Format**:
```json
[
  {
    "id": 1,
    "date": "1/11/99",
    "number": 1
  },
  {
    "id": 2,
    "date": "1/12/99",
    "number": 2
  }
]
```

#### 2. GET /episodes/<id>
**Description**: Retrieves a specific episode with all associated appearances and guest details

**Success Response (200)**:
```json
{
  "id": 1,
  "date": "1/11/99",
  "number": 1,
  "appearances": [
    {
      "episode_id": 1,
      "guest": {
        "id": 1,
        "name": "Michael J. Fox",
        "occupation": "actor"
      },
      "guest_id": 1,
      "id": 1,
      "rating": 4
    }
  ]
}
```

**Error Response (404)**:
```json
{
  "error": "Episode not found"
}
```

#### 3. GET /guests
**Description**: Retrieves all guests in the database

**Response Format**:
```json
[
  {
    "id": 1,
    "name": "Michael J. Fox",
    "occupation": "actor"
  },
  {
    "id": 2,
    "name": "Sandra Bernhard",
    "occupation": "Comedian"
  }
]
```

#### 4. POST /appearances
**Description**: Creates a new appearance linking a guest to an episode with a rating

**Request Headers**:
```
Content-Type: application/json
```

**Request Body**:
```json
{
  "rating": 5,
  "episode_id": 1,
  "guest_id": 2
}
```

**Success Response (201)**:
```json
{
  "id": 3,
  "rating": 5,
  "guest_id": 2,
  "episode_id": 1,
  "episode": {
    "date": "1/11/99",
    "id": 1,
    "number": 1
  },
  "guest": {
    "id": 2,
    "name": "Sandra Bernhard",
    "occupation": "Comedian"
  }
}
```

**Error Response (400)**:
```json
{
  "errors": ["Rating must be between 1 and 5"]
}
```

## Testing the API

### Using Postman
1. Import the provided Postman collection
2. Set the base URL to `http://localhost:5555`
3. Test each endpoint with the provided examples

### Using cURL
```bash
# Get all episodes
curl http://localhost:5555/episodes

# Get specific episode
curl http://localhost:5555/episodes/1

# Get all guests
curl http://localhost:5555/guests

# Create new appearance
curl -X POST http://localhost:5555/appearances \
  -H "Content-Type: application/json" \
  -d '{"rating": 4, "episode_id": 1, "guest_id": 2}'
```

## Data Models

### Episode Model
- **id**: Primary key (Integer)
- **date**: Episode air date (String)
- **number**: Episode number (Integer)
- **appearances**: Relationship to Appearance model

### Guest Model
- **id**: Primary key (Integer)
- **name**: Guest full name (String)
- **occupation**: Guest profession (String)
- **appearances**: Relationship to Appearance model

### Appearance Model
- **id**: Primary key (Integer)
- **rating**: Guest performance rating 1-5 (Integer)
- **episode_id**: Foreign key to Episode (Integer)
- **guest_id**: Foreign key to Guest (Integer)
- **episode**: Relationship to Episode model
- **guest**: Relationship to Guest model

## Validation Rules

### Appearance Validations
- **Rating**: Must be an integer between 1 and 5 (inclusive)
- **Episode ID**: Must reference an existing episode
- **Guest ID**: Must reference an existing guest

## Error Handling

The API implements comprehensive error handling:
- **400 Bad Request**: Invalid input data or validation failures
- **404 Not Found**: Requested resource does not exist
- **500 Internal Server Error**: Server-side errors (automatically handled by Flask)

## Database Relationships

- **Episode ↔ Guest**: Many-to-many relationship through Appearance
- **Episode → Appearance**: One-to-many (one episode can have multiple appearances)
- **Guest → Appearance**: One-to-many (one guest can appear on multiple episodes)
- **Cascade Deletes**: Deleting an episode or guest removes associated appearances

## Technologies Used

- **Flask**: Lightweight web framework for Python
- **SQLAlchemy**: Python SQL toolkit and Object-Relational Mapping (ORM)
- **Flask-Migrate**: Database migration management for Flask applications
- **SQLAlchemy-Serializer**: Automatic JSON serialization for SQLAlchemy models
- **SQLite**: Lightweight database engine (default)
- **Pipenv**: Python dependency management and virtual environment tool

## Project Structure

```
Late-shows/
├── app.py                 # Main Flask application
├── models.py              # Database models
├── seed.py                # Database seeding script
├── Pipfile                # Pipenv dependencies
├── Pipfile.lock           # Locked dependency versions
├── README.md              # Project documentation
├── migrations/            # Database migration files
└── instance/
    └── app.db            # SQLite database file
```

## Development Notes

- The application uses SQLite for development (production should use PostgreSQL or MySQL)
- Database migrations are handled through Flask-Migrate
- JSON serialization is controlled to prevent circular references
- All endpoints return JSON responses with appropriate HTTP status codes
- The seed file provides sample data for testing and development

## Future Enhancements

- Add authentication and authorization
- Implement pagination for large datasets
- Add search and filtering capabilities
- Include episode descriptions and guest photos
- Add rating statistics and analytics endpoints
- Implement caching for improved performance