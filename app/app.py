from flask import Flask
import redis

app = Flask(__name__)

redis_client = redis.Redis(host="redis", port=6379)


@app.route("/")
def home():
    redis_client.incr("visits")
    visits = redis_client.get("visits").decode("utf-8")

    return {
        "message": "CI/CD Pipeline Working!",
        "visits": visits
    }


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)