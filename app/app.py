from flask import Flask
import redis

app = Flask(__name__)

try:
    redis_client = redis.Redis(host="redis", port=6379)
    redis_client.ping()
except Exception:
    redis_client = None


@app.route("/")
def home():
    if redis_client:
        redis_client.incr("visits")
        visits = redis_client.get("visits").decode("utf-8")
    else:
        visits = "Redis unavailable"

    return {
        "message": "CI/CD Pipeline Working!",
        "visits": visits
    }


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
