<h1 align="center" >
    <img src="https://user-images.githubusercontent.com/63620799/165868020-7021fdfe-4363-4ec5-9bc8-89dfb0a9d56a.gif">
</h1>



<h2 align="center" >
    Calculator of Payments<br>
    <img alt="GitHub stars" src="https://img.shields.io/github/stars/Alfareiza/calc-payment?style=social">
    <img alt="GitHub followers" src="https://img.shields.io/github/followers/Alfareiza?label=Follow%20me%20%3A%29&style=social">
</h2>

## Introduction

Certain company offers their employees the flexibility to work the hours they want. They will pay for the hours worked based on the day of the week and time of day, according to the following table:

| Monday - Friday      |  Saturday and Sunday |
|----------------------|:--------------------:|
| 00:01 - 09:00 25 USD | 00:01 - 09:00 30 USD |
| 09:01 - 18:00 15 USD | 09:01 - 18:00 20 USD |
| 18:01 - 00:00 20 USD | 18:01 - 00:00 25 USD |

The goal of this exercise is to calculate the total that the company has to pay an employee, based on the hours they worked and the times during which they worked. The following abbreviations will be used for entering data:

    MO: Monday, TU: Tuesday, WE: Wednesday TH: Thursday, FR: Friday, SA: Saturday, SU: Sunday

Input: the name of an employee and the schedule they worked, indicating the time and hours. This should be a .txt file with at least five sets of data. You can include the data from our two examples below.

Output: indicate how much the employee has to be paid

For example:

Case 1:

    INPUT

    RENE=MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00-21:00

    OUTPUT:

    The amount to pay RENE is: 215 USD

Case 2:

    INPUT
    
    ASTRID=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00
    
    OUTPUT:
    
    The amount to pay ASTRID is: 85 USD

## Prerequisites

Git, Pip, Python (^3.8) installed and configured as environment variables.

### 1. Clone the Project

Execute the next command on your terminal

`git clone https://github.com/Alfareiza/calc-payment.git`

### 2. Isolate the environment

Once the repository has been cloned, a folder is created with the name of the project `calc-payment`. 

Go toward this folder using the terminal :

`cd calc-payment`

And execute:

`python -m venv .venv`

Then to activate the isolated environment execute the next command according to your O.S

|          Windows       |              Linux          |
|------------------------|:---------------------------:|
| .venv\Scripts\activate |  source .venv/bin/activate  |

Finally, execute:

`pip install -r requirements.txt`

All the dependencies and sub-dependencies will be installed on the local project.

## How to execute

Once the environment has been isolated, you can execute the program, you will need [the txt file](https://github.com/Alfareiza/calc-payment/blob/main/file.txt) with the information for the calculation to work.

With the repository, has been downloaded a file sample file that you can modify, respecting the pattern of the lines.

So, for the magic to happen, execute the next command:

`python -m calcpayment`

or

`python calcpayment.py`

You will see a message informing what the program does and asking you if you want to start to do the calculation.

Once the program has finished, you can modify the txt file, in order to force the program to demand more from it. 

This is how it looks:

```
This program calculates the fee of a employee based on information fed by txt file according to the next pattern:
            					"JANE=MO10:00-12:00,WE08:15-17:51,SU20:00-21:00"
            Then, will be printed on the screen the salary of every employee. Be sure that there is a txt file on the folder.
            
Should I start to calculate the information (S/N): s
Reading information from the file "file.txt"

RENE ↓
	Payment of : 30.0 on Monday
	Payment of : 30.0 on Tuesday
	Payment of : 50.0 on Thursday
	Payment of : 80.0 on Saturday
	Payment of : 25.0 on Sunday
The amount to pay RENE is: 215 USD

ASTRID ↓
	Payment of : 30.0 on Monday
	Payment of : 30.0 on Thursday
	Payment of : 25.0 on Sunday
The amount to pay ASTRID is: 85 USD

ALFONSO ↓
	Payment of : 144.75 on Monday
	Payment of : 132.58 on Wednesday
	Invalid date/time format -> ""
	Payment of : 30.83 on Sunday
The amount to pay ALFONSO is: 308 USD

```

## How to test it

Now that you have experienced the result of the calculation, and keep in mind the enviroment is isolated, you can test the code executing the next command:

`pytest .`

Will execute 54 tests.
