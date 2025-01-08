Restaurant Management System

The following is a simple architecture of the system
![image](https://github.com/user-attachments/assets/ec3b957c-8022-449a-be84-48ba606aa6a4)


The video below explains in detail about the system and how it works.

[![Watch the video on youtube](https://i9.ytimg.com/vi_webp/nfxVt-8JdW0/mq3.webp?sqp=CKyu-bsG-oaymwEmCMACELQB8quKqQMa8AEB-AH-CYAC0AWKAgwIABABGBQgJSh_MA8=&rs=AOn4CLCT3jFMKUy-oHC93vBlLYUR62PdXg)](https://youtu.be/nfxVt-8JdW0)


Follow the steps to run this application.
1. Clone the repository
2. Create a virtual environment
   ```
   python3 -m venv venv
   ```
3. Install the required packages
   ```
   pip3 install -r requirements.txt
   ```
4. Add the following environment variables
   - POSTGRES_DEV_URI (Postgres database URI)
   - JWT_DEV_SECRET (Secret key for the JWT token) 

5. Create a database in postgres with the following command
   ```
   create database restaurantdb;
   ```
6. Run the migrations for the database with the following commands
   ```
   flask --app restaurant_api db init
   flask --app restaurant_api db migrate
   flask --app restaurant_api db upgrade
   ```
7. Finally run the flask application
   ```
   flask --app restaurant_api run
   ```

