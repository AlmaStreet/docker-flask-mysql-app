# docker-flask-mysql-app

This project was created to gain hands-on experience and familiarity with
Docker, flask, and mysql. In this project, we use docker-compose to assemble
and run multiple containers. In this case, the containers are docker-flask-app
and mysql. When starting, Docker will download the required Images which can
also be found at https://hub.docker.com. The goal was to run a multi-container
project as a proof of concept, but later evolved into a database interface.
I hope you enjoy!

For more information, checkout out the Docker guide here.
Most of this project was built on it!
https://docs.docker.com/language/python/build-images/

Prerequisite:
- Docker installed


To get started, go to the folder containing the docker-compose file:

<img width="387" alt="Screen Shot 2022-05-05 at 7 42 31 PM" src="https://user-images.githubusercontent.com/6599619/167058170-5e0845a7-89b4-451f-a043-5bb90bfbb488.png">

Run the following command in terminal:

```docker-compose -f docker-compose.dev.yml up --build```


Wait for the containers to finish starting. When the output looks like this, we know the containers are ready.
<img width="710" alt="Screen Shot 2022-05-05 at 7 43 56 PM" src="https://user-images.githubusercontent.com/6599619/167058317-0252baef-aeb5-4b1f-81bd-751de5389520.png">

Open a browser and navigate to http://localhost:8000

<img width="531" alt="Screen Shot 2022-05-05 at 7 46 18 PM" src="https://user-images.githubusercontent.com/6599619/167058589-f08454bc-42eb-4ebe-abb9-d7854ed0f51d.png">

From there, click the available options to:
1. count to target number
2. create new database
3. write to database
4. read from database

<img width="530" alt="Screen Shot 2022-05-05 at 7 47 19 PM" src="https://user-images.githubusercontent.com/6599619/167058811-463ea2b6-61e9-449f-9b22-862990b7430b.png">

<img width="525" alt="Screen Shot 2022-05-05 at 7 47 32 PM" src="https://user-images.githubusercontent.com/6599619/167058823-44f0f165-90de-4e33-9a8f-008dff901d7b.png">

<img width="523" alt="Screen Shot 2022-05-05 at 7 48 12 PM" src="https://user-images.githubusercontent.com/6599619/167058834-c2a6f0b5-81d2-4146-97c2-19b6b4ec9c71.png">

<img width="529" alt="Screen Shot 2022-05-05 at 7 48 24 PM" src="https://user-images.githubusercontent.com/6599619/167058840-f86ec6c0-95ed-46cc-bb5d-af8abceab735.png">






