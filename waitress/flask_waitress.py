from dataclasses import dataclass
from flask import Flask
import logging
import time


filename = f'logs/{time.strftime("%Y-%m-%d")}.log'
logging.basicConfig(filename=filename, level=logging.INFO)
logging.debug("This message should go to the log file")


@dataclass
class Item:
    name: str
    age: int


def test(item: Item):
    print(item.name, item.age, sep="|", end=">>")


# item_one = Item(name="ben", age=32)
# test(item_one)


app = Flask(__name__)


@app.route("/")
def index():
    logging.info("Hello World" "")
    return "Hello World 1"


wsgi_app = app.wsgi_app

# if __name__ == '__main__':
#     app.run(debug=True)
