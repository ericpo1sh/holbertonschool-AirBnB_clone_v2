<center> <h1>HBNB - The Console</h1> </center>

This repository contains the initial stage of a student project to build a clone of the AirBnB website. This stage implements a backend interface, or console, to manage program data. Console commands allow the user to create, update, and destroy objects, as well as manage file storage. Using a system of JSON serialization/deserialization, storage is persistent between sessions.

---

<center><h3>Repository Contents by Project Task</h3> </center>

| Tasks | Files | Description |
| ----- | ----- | ------ |
| 0: Authors/README File | [AUTHORS](https://github.com/justinmajetich/AirBnB_clone/blob/dev/AUTHORS) | Project authors |
| 1: Pep8 | N/A | All code is pep8 compliant|
| 2: Unit Testing | [/tests](https://github.com/justinmajetich/AirBnB_clone/tree/dev/tests) | All class-defining modules are unittested |
| 3. Make BaseModel | [/models/base_model.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/models/base_model.py) | Defines a parent class to be inherited by all model classes|
| 4. Update BaseModel w/ kwargs | [/models/base_model.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/models/base_model.py) | Add functionality to recreate an instance of a class from a dictionary representation|
| 5. Create FileStorage class | [/models/engine/file_storage.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/models/engine/file_storage.py) [/models/_ _init_ _.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/models/__init__.py) [/models/base_model.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/models/base_model.py) | Defines a class to manage persistent file storage system|
| 6. Console 0.0.1 | [console.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/console.py) | Add basic functionality to console program, allowing it to quit, handle empty lines and ^D |
| 7. Console 0.1 | [console.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/console.py) | Update the console with methods allowing the user to create, destroy, show, and update stored data |
| 8. Create User class | [console.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/console.py) [/models/engine/file_storage.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/models/engine/file_storage.py) [/models/user.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/models/user.py) | Dynamically implements a user class |
| 9. More Classes | [/models/user.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/models/user.py) [/models/place.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/models/place.py) [/models/city.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/models/city.py) [/models/amenity.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/models/amenity.py) [/models/state.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/models/state.py) [/models/review.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/models/review.py) | Dynamically implements more classes |
| 10. Console 1.0 | [console.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/console.py) [/models/engine/file_storage.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/models/engine/file_storage.py) | Update the console and file storage system to work dynamically with all  classes update file storage |
<br>
<br>
<center> <h2>General Use</h2> </center>

1. First clone this repository.

3. Once the repository is cloned locate the "console.py" file and run it as follows:
```
/AirBnB_clone$ ./console.py
```
4. When this command is run the following prompt should appear:
```
(hbnb)
```
5. This prompt designates you are in the "HBnB" console. There are a variety of commands available within the console program.

##### Commands
    * create - Creates an instance based on given class

    * destroy - Destroys an object based on class and UUID

    * show - Shows an object based on class and UUID

    * all - Shows all objects the program has access to, or all objects of a given class

    * update - Updates existing attributes an object based on class name and UUID

    * quit - Exits the program (EOF will as well)


##### Alternative Syntax
Users are able to issue a number of console command using an alternative syntax:

	Usage: <class_name>.<command>([<id>[name_arg value_arg]|[kwargs]])
Advanced syntax is implemented for the following commands: 

    * all - Shows all objects the program has access to, or all objects of a given class

	* count - Return number of object instances by class

    * show - Shows an object based on class and UUID

	* destroy - Destroys an object based on class and UUID

    * update - Updates existing attributes an object based on class name and UUID

# AirBnB Console :house:
### Description :pen:
 The AirBnB Console is a command-line interpreter created for the purpose of handling objects similar to those found on Airbnb. It offers an easy-to-use interface for performing actions like creating, viewing, modifying, and removing instances of different classes like BaseModel, User, State, City, Amenity, Place, and Review. The Console involves the development of a console-driven application meant for the management of objects like the ones found on Airbnb. The Console includes a range of capabilities, including instance creation, information presentation, attribute modification, and instance removal. All the data is serialized and deserialized to and from JSON files to ensure effective data management.

#

### Features :pushpin:
- Create Instances - Creates new object/instance of the BaseModel class and save them into a JSON file.
- Display Information - The console lets you see in-depth information about specific objects/instances using their class name and ID.
- Delete Instances - You can remove object/instances by providing their class name and ID, and the console will automatically save the changes to the JSON file.
- List Instances - The console provides the option to list all object/instances or filter them by class name or ID.
- Update Attributes - You can modify object/instance attributes by providing their class name, ID, the attribute name, and the new value and the console saves the changes to JSON.

#

### Installation! :file_folder:
**REQUIREMENT: Make sure that you have a working terminal with [python3](https://realpython.com/installing-python/) or greater installed!**

**Clone the repository; example below:**
```
root@user$ git clone https://github.com/ericpo1sh/holbertonschool-AirBnB_clone.git
```
**Then navigate to the projects root directory and run console.py; example below:**
```
holbertonschool-AirBnB_clone$ ./console.py
```
**The application should be running and the following promp should display:**
```
(hbnb)
```
#

#### Command Usage, Syntax, Descriptions :blue_book:

| Syntax | Description |
| -------| ----------- |
| `create <class_name>` | Creates new object/instance of the BaseModel class and save them into a JSON file. |
| `show <class_name> <id>` | See information about specific objects/instances using their class name and ID. |
| `destroy <class_name> <id>` | Destroy object/instances with class name and ID. |
| `all` ***or*** `all <class_name>` | Prints string representation of all instances or all instances of a specific class. |
| `update <class_name> <id> <atr_name> <atr_value>` | Update a specific instance and add a attribute name and value. |
| `clear` | Clear the screen. |
| `quit` | Exit the program. |
#

### List of availiable Classes :round_pushpin:
- BaseModel
- User
- State
- City
- Amenity
- Place
- Review

#

### Examples! :bulb:
**In this example, we create a new instance of BaseModel, a new ID is returned.**

```
(hbnb) create BaseModel
ab763e7e-4bc8-4380-bb07-0a07a8f1a56d
```
**Now lets use the show command on this newly created instance.**
```
(hbnb) show BaseModel ab763e7e-4bc8-4380-bb07-0a07a8f1a56d
[BaseModel] (ab763e7e-4bc8-4380-bb07-0a07a8f1a56d) {'id': 'ab763e7e-4bc8-4380-bb07-0a07a8f1a56d',
'created_at': datetime.datetime(2023, 10, 9, 10, 38, 1, 900183),
'updated_at': datetime.datetime(2023, 10, 9, 10, 38, 1, 900224)}
```
**Now lets update the instance and add a new object to it.**
```
(hbnb) update BaseModel ab763e7e-4bc8-4380-bb07-0a07a8f1a56d Name "Eric"
(hbnb) show BaseModel ab763e7e-4bc8-4380-bb07-0a07a8f1a56d
[BaseModel] (ab763e7e-4bc8-4380-bb07-0a07a8f1a56d) {'id': 'ab763e7e-4bc8-4380-bb07-0a07a8f1a56d',
'created_at': datetime.datetime(2023, 10, 9, 10, 38, 1, 900183),
'updated_at': datetime.datetime(2023, 10, 9, 11, 3, 0, 44871),
'Name': 'Eric'}
```
**Now lets use the all command to display any instance of any Class!**
```
(hbnb) create BaseModel
a8259ae7-2ecb-4fb9-aafc-0e4244adf089
(hbnb) create User
2e2244f0-4f38-4c5e-9ecd-fe3f452bf7b8
(hbnb) create Place
af95611c-9ab1-459d-809c-f371eac2a5ef
(hbnb) all
[BaseModel] (a8259ae7-2ecb-4fb9-aafc-0e4244adf089) {'id': 'a8259ae7-2ecb-4fb9-aafc-0e4244adf089',
'created_at': datetime.datetime(2023, 10, 9, 11, 43, 8, 384959),
'updated_at': datetime.datetime(2023, 10, 9, 11, 43, 8, 384984)}
[User] (2e2244f0-4f38-4c5e-9ecd-fe3f452bf7b8) {'id': '2e2244f0-4f38-4c5e-9ecd-fe3f452bf7b8',
'created_at': datetime.datetime(2023, 10, 9, 11, 43, 11, 498325),
'updated_at': datetime.datetime(2023, 10, 9, 11, 43, 11, 498340)}
[Place] (af95611c-9ab1-459d-809c-f371eac2a5ef) {'id': 'af95611c-9ab1-459d-809c-f371eac2a5ef',
'created_at': datetime.datetime(2023, 10, 9, 11, 43, 14, 199276),
'updated_at': datetime.datetime(2023, 10, 9, 11, 43, 14, 199337)}
(hbnb) 
```

**Now lets destroy the instance!**
```
(hbnb) destroy BaseModel ab763e7e-4bc8-4380-bb07-0a07a8f1a56d
(hbnb) show BaseModel ab763e7e-4bc8-4380-bb07-0a07a8f1a56d
** no instance found **
```
#
# To Run Unittests, you can do the following! :test_tube:
```
root@user:~/AirBnB$ python3 -m unittest discover tests
................................................
----------------------------------------------------------------------
Ran 48 tests in 0.232s

OK
root@user:~/AirBnB$
```
#
![image](https://github.com/ericpo1sh/holbertonschool-AirBnB_clone/assets/126730794/e82771fe-bb0a-44b1-935c-99efbf0877d3)
## Authors/Contact info :phone: :mailbox:
* **Eric Dzyk** **|** [Github](https://github.com/ericpo1sh) **|** [LinkedIn](https://linkedin.com/in/eric-dzyk-1b8976213) **|** [Email](mailto:ericpo1sh@gmail.com)  
* **Sammy Ansari** **|** [Github](https://github.com/O-01) **|** [LinkedIn](https://linkedin.com/in/sam-ansari-579553287) **|** [Email](mailto:na.01goli@gmail.com)
##
![Holberton School - School of Computer Science and Programming](https://uploads-ssl.webflow.com/6105315644a26f77912a1ada/63eea844ae4e3022154e2878_Holberton.png)
##
