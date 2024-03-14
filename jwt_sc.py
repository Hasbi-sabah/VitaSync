#!/usr/bin/env python3
import jwt
import sys

payload = {
    "user_id": sys.argv[1],
    "iat": 1710419384,
    "exp": 1710419385,
}

secret_key = "SOmeRandomKeySeriouslySecureRandom"
token = jwt.encode(payload, secret_key, algorithm="HS256")
print(token)
