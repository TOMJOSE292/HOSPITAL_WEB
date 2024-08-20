import os
from app import create_app

app = create_app()

if __name__ == "__main__":
    # Print environment variables on startup
    print("SECRET_KEY:", os.getenv('SECRET_KEY'))
    print("DATABASE_URI:", os.getenv('DATABASE_URI'))

    app.run()
