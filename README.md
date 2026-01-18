# Music Backend

A backend API for managing music data, users, plays, and analytics.
Built with **FastAPI**, **Uvicorn**, and **Python**, following a layered architecture with clear separation of concerns.

## Tech Stack

* Python 3.7+
* FastAPI
* Uvicorn
* SQLAlchemy
* Pytest (for testing)

## Project Structure

```
.
├── app/
│   ├── main.py              # FastAPI application entry point
│   ├── core/                # Core configuration
│   │   └── config.py
│   ├── db/                  # Database setup and session management
│   │   ├── connection.py
│   │   ├── database.py
│   │   ├── init_db.py
│   │   └── session.py
│   ├── models/              # SQLAlchemy models
│   │   ├── artist.py
│   │   ├── play.py
│   │   ├── song.py
│   │   └── user.py
│   ├── schemas/             # Pydantic schemas
│   │   ├── artist.py
│   │   ├── play.py
│   │   ├── song.py
│   │   └── user.py
│   ├── routers/             # API route definitions
│   │   ├── analytics.py
│   │   ├── artist_analytics.py
│   │   ├── plays.py
│   │   ├── songs.py
│   │   └── users.py
│   └── services/            # Business logic layer
│       ├── analytics_service.py
│       ├── artist_analytics_service.py
│       ├── artist_service.py
│       ├── play_service.py
│       ├── song_service.py
│       └── user_service.py
├── docs/
├── tests/                   # Test suite
│   ├── conftest.py
│   ├── test_health.py
│   ├── test_users.py
│   ├── test_songs.py
│   ├── test_artists.py
│   ├── test_plays.py
│   └── test_analytics.py
├── requirements.txt
└── README.md
```

## Architecture Overview

This project follows a layered backend architecture:

* **Routers** handle HTTP requests and responses
* **Schemas** define request/response validation with Pydantic
* **Services** contain business logic
* **Models** define database entities
* **DB** handles database connections, sessions, and initialization

## Getting Started

### Prerequisites

* Python 3.7 or newer
* pip

### Installation

Clone the repository:

```bash
git clone https://github.com/lkorsman/music_backend.git
cd music_backend
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Running the Application

Start the FastAPI server using Uvicorn:

```bash
uvicorn app.main:app --reload
```

The API will be available at:

```
http://127.0.0.1:8000
```

Interactive API documentation:

* Swagger UI: `http://127.0.0.1:8000/docs`

## API Overview

The API provides endpoints for:

* Users
* Songs
* Artists
* Plays
* Analytics and Artist analytics

Example endpoint categories:

| Method | Path                    | Description               |
| ------ | ----------------------- | ------------------------- |
| GET    | /health                 | Health check              |
| GET    | /users                  | List users                |
| POST   | /songs                  | Create a song             |
| POST   | /plays                  | Record a play             |
| GET    | /analytics              | General analytics         |
| GET    | /artists/{id}/analytics | Artist-specific analytics |

Refer to `/docs` when the server is running for full details.

## Database

Database configuration and initialization are handled in:

```
app/db/
```

You may need to configure environment variables (e.g., database URL) depending on your setup.

## Running Tests

Run the full test suite with:

```bash
pytest
```

Tests are organized by feature and cover API routes and core functionality.

## Future Improvements

Possible enhancements include:

* Authentication and authorization
* Pagination and filtering
* Async database support
* Deployment configuration (Docker, CI/CD)
* Improved analytics queries

## License

This project is licensed under the MIT License.