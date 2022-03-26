![](https://github.com/Alfareiza/calc-payment/actions/workflows/github-actions-conf.yml/badge.svg)

# Calculator of Payments

## Introduction

The company ACME offers their employees the flexibility to work the hours they want. They will pay for the hours worked based on the day of the week and time of day, according to the following table:

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

Once the repository has been cloned, is created a folder with the name of the project `calc-payment`. Go toward this folder using the terminal and execute:

`python -m venv .venv`

Then to activate the isolated environment execute the next command according to your O.S

|          Windows       |         Linux        |
|------------------------|:--------------------:|
| .venv\Scripts\activate |  .venv\bin\activate  |

Finally, execute:

`pip install -r requirements`

All the dependencies and sub-dependencies will be installed on the local project.

## How to execute

Once the environment has been isolated, you can execute the program, yet you need [the txt file](https://github.com/Alfareiza/calc-payment/blob/main/file.txt) with the information for calculating.

With the repository, has been downloaded an example file that you can modify, respecting the pattern of the lines.

So, for the magic to happen, execute the next command:

`python -m calcpayment`

or

`python calcpayment.py`

You will see a message informing what the program does and asking you if you want to start to do the calculation.

Once the program has ended up, you can modify the txt file, in order to force the program to demand more from it. 

This is how it looks:

```
This program calculate the fee of a employee trough information comes from a txt file according to the next pattern:
            					"JANE=MO10:00-12:00,WE08:15-17:51,SU20:00-21:00"
            Then, will be printed on the screen the salary of every employee. Be sure that there is a txt file on the folder.
            
Should I start to calculate the information (S/N): s
Reading information from the file "file.txt"
The amount to pay RENE is: 215 USD
The amount to pay ASTRID is: 85 USD
The amount to pay ALFONSO is: 308 USD
The amount to pay FELIPE is: 85 USD
```

## How to test it

Now that you have experienced the result of the calculation, and remembering the enviroment is isolated, you can test the code executing the next command:

`pytest .`

Will execute 54 tests.










