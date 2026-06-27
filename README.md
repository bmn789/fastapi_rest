# FastAPI User CRUD API

A small FastAPI application for managing users with CRUD operations. The project uses SQLAlchemy for database access and exposes REST endpoints for creating, reading, updating, and deleting users.

## Features

- User CRUD endpoints
- Database integration through SQLAlchemy
- Pydantic models for request and response validation
- Easy local development with Uvicorn

## Project Structure

```text
app/
  crud.py
  database.py
  main.py
  models.py
  schemas.py
  routes/
    user.py
  lib/
    none_check.py
```

## Requirements

Install dependencies with:

```bash
pip install -r requirements.txt
```

## Configuration

Create or update the environment file for your database connection:

```bash
cp .env.example .env.prod
```

Then set your database URL in `.env.prod`:

```env
DB_URL=your_database_connection_string
```

## Run the Application

Start the development server with:

```bash
uvicorn app.main:app --reload
```

The API will be available at:

- http://127.0.0.1:8000
- API docs: http://127.0.0.1:8000/docs

## API Endpoints

### User Routes

- `GET /api/user/all` - Get all users
- `GET /api/user/{user_id}` - Get a user by ID
- `POST /api/user` - Create a new user
- `PUT /api/user/{user_id}` - Update a user
- `DELETE /api/user/{user_id}` - Delete a user

### Example Request

Create a user:

```bash
curl -X POST "http://127.0.0.1:8000/api/user" \
  -H "Content-Type: application/json" \
  -d '{"name":"John Doe","email":"john@example.com","is_active":true}'
```

## Notes

The app creates database tables automatically when the application starts, based on the SQLAlchemy models.
