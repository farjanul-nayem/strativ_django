# Strativ Django
In this project,
* retrive data from a ```source/manually (http://127.0.0.1:8000/fetched)``` input and store to database
* ```create``` new item, ```read```, ```update```, ```delete``` operations
* ```CRUD REST APIs``` with ```token authentication```
* display the information in a simple ```HTML/Webpage``` with ```login & signup```

## Features
* Retrive Data
* RESTful APIs
* Webpages

### Retrive
 retrive data from this API https://restcountries.eu/rest/v2/all and ```store to database``` specific fields.
 ```
 name, alphacode2, capital, population, timezone, flag, languages and neighbouring countries
 ```

### RESTfull APIs
build ```RESTful APIs``` with ```Token Authentication```
* Login
* Signup
* List of all countries
* Details of an specific country
* Create a new country
* Update an existing country
* Delete an existing country
* List of neighbouring countries of an specific country
* List of countries who speaks the same language based on a specific language
* Searching a country by its name (should be able to search partial name)

### Webpages
* Login page
* Signup page
* Logout
* List item with respective information
```
name, alphacode2, capital, population, timezone, flag
```
* Filter country by searching option on table
* detail page

## Requirements

To run the project you need to make sure that the following requirements are full-filled on your machine.
* Python3
* Virtualenv

Note: ```SqLite``` database has been used in this project.

## Installing

Then clone the project with the following command:
```
git clone git@github.com:farjanul-nayem/strativ_django.git
```

```Create a specific environment``` for the project using the following command. ```virtualenv <name>```
```
virtualenv StrativVenv
```

Use the following command to activate the ```virtual environment``` for this project.
```
source StrativVenv/bin/activate
```

You can easily see in the ```requirements.txt``` file what tools have been used in this project. Now it's time to install these tools in the new environment. Use the following command to install.
```
pip3 install -r requirements.txt
```

If you use the following command, the project will run. Then you can see the ```application/website``` by typing http://127.0.0.1:8000 in the browser.
```
./manage.py runserver
```

<img src="https://github.com/farjanul-nayem/strativ_django/blob/master/demo/Screenshot%201.png?raw=true"/>
<img src="https://github.com/farjanul-nayem/strativ_django/blob/master/demo/Screenshot%202.png?raw=true"/>
<img src="https://github.com/farjanul-nayem/strativ_django/blob/master/demo/Screenshot%203.png?raw=true"/>

## Existing Database
This project already has some data in its database. 
If you want to see existing data you need to ```login``` using valid information.

username: ```admin```

password: ```helloadmin```

## Remove Existing Database
If you want to remove the previous database, Than delete this file ```db.sqlite3``` from the project ```root directory``` and follow the commands below.

* New databases and tables will be created.
```
./manage.py migrate
```

* Use this command to ```create a new superuser``` & input necessary informations.
```
./manage.py createsuperuser
```

* For run server again:
```
./manage.py runserver
```

Now use this link to ```get data from the source``` and ```save into database``` automatically. http://127.0.0.1:8000/fetched

Finally use browsing this url & enjoy. http://127.0.0.1:8000

### RESTful APIs
If your machine does not have ```Postman software``` installed, download and install it from here. [Download](https://www.postman.com/downloads/)

Now download this file * [Postman File](https://github.com/farjanul-nayem/strativ_django/blob/master/demo/Strativ.postman_collection.json) and import it on ```Postman```, you will get all the RESTful APIs.


# Thank You!!!
