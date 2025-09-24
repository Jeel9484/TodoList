# Todo API Backend

A FastAPI backend for the Todo application with SQLite/PostgreSQL database support.

## Features

- ✅ RESTful API for todo management
- ✅ SQLite for local development
- ✅ PostgreSQL for production
- ✅ CORS enabled for frontend integration
- ✅ Auto-generated database tables

## Local Development

### Prerequisites

- Python 3.11+
- pip

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Jeel9484/TodoList.git
   cd TodoList
   ```

2. **Create virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application:**
   ```bash
   uvicorn main:app --reload
   ```

5. **Access the API:**
   - API: http://localhost:8000
   - API Documentation: http://localhost:8000/docs
   - Alternative Docs: http://localhost:8000/redoc

## API Endpoints

- `GET /` - Welcome message
- `GET /todos/` - Get all todos
- `POST /todos/` - Create a new todo
- `GET /todos/{todo_id}` - Get a specific todo
- `PUT /todos/{todo_id}` - Update a todo
- `DELETE /todos/{todo_id}` - Delete a todo

## Deployment to Heroku

### Prerequisites

- Heroku CLI installed
- Git repository

### Deploy Steps

1. **Login to Heroku:**
   ```bash
   heroku login
   ```

2. **Create Heroku app:**
   ```bash
   heroku create your-todo-api-name
   ```

3. **Add PostgreSQL addon (required for production):**
   ```bash
   heroku addons:create heroku-postgresql:hobby-dev
   ```

4. **Set environment variables:**
   ```bash
   heroku config:set ENVIRONMENT=production
   ```

5. **Deploy to Heroku:**
   ```bash
   git add .
   git commit -m "Configure for Heroku deployment"
   git push heroku master
   ```

6. **Open your deployed app:**
   ```bash
   heroku open
   ```

### Alternative: Deploy via GitHub

1. **Connect to GitHub:**
   - Go to Heroku Dashboard
   - Create new app
   - Connect to your GitHub repository
   - Enable automatic deploys

2. **Configure environment variables in Heroku:**
   - Go to Settings → Config Vars
   - Add: `ENVIRONMENT` = `production`

## Environment Variables

- `ENVIRONMENT` - Set to "production" for production deployment
- `DATABASE_URL` - Automatically set by Heroku PostgreSQL addon

## Database

- **Local Development**: SQLite (todos.db)
- **Production**: PostgreSQL (provided by Heroku)

## CORS Configuration

- **Development**: Allows `http://localhost:3000`
- **Production**: Allows all origins (`*`)

## Project Structure

```
├── main.py          # FastAPI application
├── models.py        # Database models
├── crud.py          # CRUD operations
├── database.py      # Database configuration
├── requirements.txt # Python dependencies
├── Procfile         # Heroku deployment config
├── runtime.txt      # Python version for Heroku
└── README.md        # This file
```

## Technologies Used

- FastAPI - Modern Python web framework
- SQLAlchemy - ORM for database operations
- Uvicorn - ASGI server
- SQLite - Local development database
- PostgreSQL - Production database

## Testing the API

You can test the API using:

1. **Swagger UI**: http://localhost:8000/docs
2. **cURL**:
   ```bash
   curl -X GET "http://localhost:8000/todos/"
   curl -X POST "http://localhost:8000/todos/" \
        -H "Content-Type: application/json" \
        -d '{"title": "Test Todo", "description": "Test description"}'
   ```

## Troubleshooting

### Common Issues

1. **Port already in use**: Kill the process using the port or use a different port
2. **Database connection issues**: Check DATABASE_URL environment variable
3. **CORS errors**: Ensure frontend URL is in allowed origins

### Logs

Check Heroku logs:
```bash
heroku logs --tail
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test locally
5. Submit a pull request

## License

This project is licensed under the MIT License.