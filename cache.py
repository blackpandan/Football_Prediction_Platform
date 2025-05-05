import redis
import json

r = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)

def cache_set(key: str, value: dict, ttl: int = 60):
    r.setex(key, ttl, json.dumps(value))

def cache_get(key: str):
    data = r.get(key)
    if data:
        return json.loads(data)
    return None