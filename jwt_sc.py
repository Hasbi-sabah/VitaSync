#!/usr/bin/env python3
import jwt
import sys

payload = {
    "user_id": sys.argv[1]
}

secret_key = "SOmeRandomKeySeriouslySecureRandom"
token = jwt.encode(payload, secret_key, algorithm="HS256")
print(token)
