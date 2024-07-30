from datetime import datetime, timedelta, timezone
import environ
import jwt

env = environ.Env()
environ.Env.read_env()


class JWTAuth:
    def __init__(self):
        self.secret_key = env('JWT_SECRET')
        self.algorithm = 'HS256'

    def encode(self, payload):
        payload['exp'] = datetime.now() + timedelta(hours=1)  # Token kadaluarsa dalam 1 jam
        return jwt.encode(payload, self.secret_key, algorithm=self.algorithm)
    
    def decode(self, token):
        try:
            return jwt.decode(token, self.secret_key, algorithms=[self.algorithm])
        except jwt.ExpiredSignatureError:
            raise Exception("Silakan login kembali")
        except jwt.InvalidTokenError:
            raise Exception("Token yang Anda masukkan salah")