import jwt
from datetime import datetime, timedelta, timezone

def create_jwt():
    secret_key = 'your_secret_key'  # Use a secure key in production
    payload = {
        'sub': '1234567890',
        'name': 'John Doe',
        'iat': datetime.now(timezone.utc),
        'exp': datetime.now(timezone.utc) + timedelta(minutes=30)  # Token expires in 30 minutes
    }
    token = jwt.encode(payload, secret_key, algorithm='HS256')
    return token

if __name__ == "__main__":
    print(create_jwt())
