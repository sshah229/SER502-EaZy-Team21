
# SER502-EaZy-Team21

## Description

It is no secret that python is one of the most popular programming languages out there. What new improvements can be made to this language? What if that language was just, *EaZy* (not a good pun, but okay ;) ). Our aim is to build on the already existing user-friendly nature of python and add minor changes on top of it. 

**Parsing Technique:** The parser is going to be implemented using DCG rules using python3. We aim to build the parse tree recursively and check its validity in similar fashion as prolog. 

**Compiler / Interpreter runtime:** The runtime environment is also going to be implemented in python3. 

**Data Structures:** We have implemented the environment using Dictionary data structure and all the tokens are stored as elements in an array.

## Team Members

- Aum Garasia
- Samit Shah
- Shubham Shah
- Siddesh Shetty


## System Requirements:
* Windows or MacOS

## Tools used:
* SWI-Prolog
* Python

## Prerequisites:
* SWI-Prolog must be installed on the device.
* Python should be installed.

## Installation

To get started with **EaZy**, follow these simple steps:

1. Clone the repository:
	```
	git clone https://github.com/sshah229/SER502-EaZy-Team21.git
	```	
2. Redirect to the ```src``` folder of the project directory.
3. Open terminal and write following commands in the ```src``` directory. These will help create and activate a virtual environment for the project's runtime:
	```
	python3 -m venv pyswip_env
	```
	  Then, if you are on Windows:
	 ```
	pyswip_env\bin\activate
   ```
	 Or, if you are on MacOS:
	 ```
	source pyswip_env/bin/activate
	 ```
	 You will notice that ```pyswip_env``` is now active.
 4. Install the latest version of ```pyswip``` library using the following command:
	 ```
	 pip install git+https://github.com/yuce/pyswip@master#egg=pyswip
	 ```

## Usage

It is suggested to use **EaZy** from command line.
1. Copy and Paste the ```.ez``` program file you want to execute in ```src``` folder.
2. Open ```EaZy.py``` and modify line number 8 to read your file:
	```
	file  =  open("hello-world.ez", "r")
	```
	Here, instead of ```hello-world```, write the name of your file. Save and close the ```EaZy.py``` file.
3. Now, in the terminal, activate the virtual environment as mentioned above in steps 3 and 4.
4. Once activated, try executing the file using following command:
	```
	python EaZy.py
	```

You just executed your first EaZy program!!
