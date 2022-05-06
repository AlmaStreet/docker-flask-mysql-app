"""
This project was created to gain hands-on experience and familiarity with
Docker, flask, and mysql. In this project, we use docker-compose to assemble
and run multiple containers. In this case, the containers are docker-flask-app
and mysql. When starting, Docker will download the required Images which can
also be found at https://hub.docker.com. The goal was to run a multi-container
project as a proof of concept, but later evolved into a database interface.
I hope you enjoy!

To get started, go to the folder containing the docker-compose file and run the
following command in terminal:
  docker-compose -f docker-compose.dev.yml up --build

When containers are ready, open a browser and navigate here:
http://localhost:8000

From there, click the available options to:
1. count to target number
2. create new database
3. write to database
4. read from database


By Jason Chen

inspired by:
https://docs.docker.com/language/python/build-images/
"""

import mysql.connector
import json
from flask import Flask, request, render_template

app = Flask(__name__)


# Read from database
@app.route("/read")
def show_data():
    mydb = mysql.connector.connect(
        host="mysqldb",
        user="root",
        password="p@ssw0rd1",
        database="inventory",
    )

    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM widgets")

    # this will extract row headers
    row_headers = [x[0] for x in cursor.description]

    results = cursor.fetchall()
    json_data = []
    for result in results:
        json_data.append(dict(zip(row_headers, result)))

    cursor.close()

    dump = json.dumps(json_data, indent=4)
    print(dump)

    return render_template("read-db.html", dump=f"<pre>{dump}</pre>")


# Write to database
@app.route("/write", methods=["POST", "GET"])
def insert_data():
    if request.method == "POST":

        name = request.form.get("name")
        description = request.form.get("description")

        mydb = mysql.connector.connect(
            host="mysqldb",
            user="root",
            password="p@ssw0rd1",
            database="inventory",
        )

        cursor = mydb.cursor()
        cursor.execute(
            f'INSERT INTO widgets (name, description) \
            VALUES ("{name}", "{description}");'
        )
        mydb.commit()

        cursor.close()
        return render_template(
            "write-db.html",
            dump=f"Storing <br>name: {name}<br>description: {description} \
            <br><br>Click 'Display Data' button to see your entry.",
        )
    else:
        return render_template("write-db.html", dump="")


# Clear database
@app.route("/init")
def db_init():
    mydb = mysql.connector.connect(
        host="mysqldb", user="root", password="p@ssw0rd1",
    )
    cursor = mydb.cursor()

    cursor.execute("DROP DATABASE IF EXISTS inventory")
    cursor.execute("CREATE DATABASE inventory")
    cursor.close()

    mydb = mysql.connector.connect(
        host="mysqldb",
        user="root",
        password="p@ssw0rd1",
        database="inventory",
    )
    cursor = mydb.cursor()

    cursor.execute("DROP TABLE IF EXISTS widgets")
    cursor.execute(
        "CREATE TABLE widgets \
    (name VARCHAR(255), description VARCHAR(255))"
    )
    cursor.close()

    return render_template("init-db.html", dump="Clearing database!")


# Home page
@app.route("/", methods=["POST", "GET"])
def hello_world():
    content = ""
    number = request.form.get("number")

    if request.method == "POST":
        try:
            nums = int(number)
            content += f"<br>Counting to {number}."
            sign = ""
            if nums == 0:
                content += "<br>0"
            else:
                if nums < 0:
                    sign = "-"
                for num in range(abs(nums)):
                    content += f"<br>{sign}{num + 1}"
        except Exception:
            pass
    return render_template("index.html", dump=content)
