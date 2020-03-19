## Award
This application will allow a user to post a project he/she has created and get it reviewed by his/her peers.

## Requirements
Clone the the repository by running

```
git clone https://github.com/monicaoyugi/Awards
or download a zip file of the project from github then unzip.
```

Navigate to your project directory

## Create a virtual environment
Install Virtualenv

```
pip install virtual venv
```

To create a virtual environment named virtual, run

```
virtualenv virtual
```
To activate the virtual environment we just created,
run

```
source virtual/bin/activate
```

## Create a database
You'll need to create a new postgress database, Type the following command to access postgress

 $ psql

 Then run the following query to create a new database named award

```
create database award
```

## Database diagram

![picture](https://dbdiagram.io/d/5e7371fe4495b02c3b887852)



## Install dependencies
To install the requirements from requirements.txt file,

```
pip install -r requirements.txt
```

## Create Database migrations
Making migrations on postgres using django
run

```
python3 manage.py makemigrations  award
```
then run the command below;

```
python3 manage.py migrate
```
## Run the app
To run the application on your development machine,

```
python3 manage.py runserver
```
## Running Tests
To run tests

```
python3 manage.py test
```

## Technologies Used
- Django
- Django rest
- Python
- Html
- Css
- Javascript
- Bootstrap

## User stories

As a user of the application I should be able to:

- View posted projects and their details.
- Post a project to be rated/reviewed
- Rate/ review other users' projects
- Search for projects
- View projects overall score
- View my profile page


## Codebeat

[![codebeat badge](https://codebeat.co/badges/ed88bffe-c97b-436a-8747-29bff5ce5938)](https://codebeat.co/projects/github-com-monicaoyugi-awards-master)


## LICENSE
[LICENSE](license)

__Copyright (c) {2020} Monica Oyugi.__
