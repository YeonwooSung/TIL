from functools import wraps
from flask import Flask
import asyncio

def async_action(f):
    @wraps(f)
    def wrapped(*args, **kwargs):
        return asyncio.run(f(*args, **kwargs))
    return wrapped

app = Flask(__name__)

@app.route('/')
@async_action
async def index():
    await asyncio.sleep(2)
    return 'Hello world !'

app.run()
