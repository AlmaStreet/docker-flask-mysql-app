# docker-flask-mysql-app

This project was created to gain hands-on experience and familiarity with
Docker, flask, and mysql. In this project, we use docker-compose to assemble
and run multiple containers. In this case, the containers are docker-flask-app
and mysql. When starting, Docker will download the required Images which can
also be found at https://hub.docker.com. The goal was to run a multi-container
project as a proof of concept, but later evolved into a database interface.
I hope you enjoy!

To get started, go to the folder containing the docker-compose file and run the
following command in terminal:

  ```docker-compose -f docker-compose.dev.yml up --build```

When containers are ready, open a browser and navigate here:
http://localhost:8000

From there, click the available options to:
1. count to target number
2. create new database
3. write to database
4. read from database



For more information, checkout out the Docker guide here. 
https://docs.docker.com/language/python/build-images/
