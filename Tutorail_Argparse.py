"""
What is Argparse ?

The argparse module makes it easy to write user-friendly command-line interfaces.
The program defines what arguments it requires, 
and argparse will figure out how to parse those out of sys.argv .
The argparse module also automatically generates help and usage messages.

"""
# Step 1

# import argparse

# parser = argparse.ArgumentParser(description= 'This is a tutorail for argument parser.')
# parser.add_argument('filename')
# argument = parser.parse_args()
# print(argument)
# print(argument.filename)

# End of the step

# Step 2

# import argparse

# parser = argparse.ArgumentParser(description= 'This is a tutorail for argument parser.')
# parser.add_argument('filename', help='The name of the file that we want to work with.')
# argument = parser.parse_args()
# print(argument)
# print(argument.filename)

# End of the step

# Step 3

# import argparse
# # First run without givinig a file.
# parser = argparse.ArgumentParser(description= 'This is a tutorail for argument parser.')
# parser.add_argument('filename', help='The name of the file that we want to work with.')
# argument = parser.parse_args()
# print(argument)
# file = argument.filename
# print(file)

# End of the step

# Step 4

# import argparse
# # we can remove the help of argparse but it does not make sense
# parser = argparse.ArgumentParser(description= 'This is a tutorail for argument parser.')
# parser.add_argument('filename', help=argparse.SUPPRESS)
# argument = parser.parse_args()
# print(argument)
# file = argument.filename
# print(file)

# End of the step

"""
Attention, we can use -f for abbreviation of file name but after that we should use -- and full name of the 
argument and remember this argument is optional due to it's notation * -f *. But if do not use - the
argument will be required
"""
# Step 5 

# import argparse
# # write -c file.txt to get an error
# parser = argparse.ArgumentParser(description= 'This is a tutorail for argument parser.')
# parser.add_argument('filename', help='The name of the file that we want to work with.')
# parser.add_argument('-c', '--copy', help='Make N copy.')
# argument = parser.parse_args()
# print(argument)
# file = argument.filename
# print(file)

# End of the step

"""
We can have two or any argument that is required, but remember argparse pick up in order from left to 
right that argument which is without label for positional arguments. And optional arguments always pick up
after their label(abbriviation or --fullname).
"""
# Step 6
# import argparse

# parser = argparse.ArgumentParser(description= 'This is a tutorail for argument parser.')
# parser.add_argument('filename', help='The name of the file that we want to work with.')
# parser.add_argument('filepath', help='The path of the file that we want to work with.')
# parser.add_argument('-c', '--copy', help='Make N copy.')
# argument = parser.parse_args()
# print(argument)
# file = argument.filename
# file1 = argument.filepath
# print(file)
# print(file1)

# End of the step

"""
there is a prameter called /action/ in .add_argument and by defult it is 'store' which means expect value 
after label in optional or left to right for positional arguments. If get -h you can see the help and that shows you 
how to enter value/ -c COPY, --copy COPY  Make N copy.

Also, we can change the action to do other thing that we will learn in continue. But what is metavar,
metavar actually is the notation of the value after name in optional arguments.
For better understanding see below.
"""
# Step 7
# import argparse

# parser = argparse.ArgumentParser(description= 'This is a tutorail for argument parser.')
# parser.add_argument('filename', help='The name of the file that we want to work with.')
# parser.add_argument('-c', '--copy', metavar='N', help='Make N copy.')
# argument = parser.parse_args()
# print(argument)
# file = argument.filename
# print(file)

# -c N, --copy N  Make N copy. with metavar.
# End of the step

"""
Let's get familiar with action = 'store_const'
If write -s in terminal size == 15 
If do not write -s size == None
How about writing -s 12 ????
"""
# Step 8

# import argparse

# parser = argparse.ArgumentParser(description= 'This is a tutorail for argument parser.')
# parser.add_argument('filename', help='The name of the file that we want to work with.')
# parser.add_argument('-c', '--copy', metavar='N', help='Make N copy.')
# parser.add_argument('-s', '--size', action='store_const', help='The size of it.', const=15)
# argument = parser.parse_args()
# print(argument)
# file = argument.filename
# print(file)

# python3 Tutorail_Argparse.py -s file.txt |run this command and check it
# python3 Tutorail_Argparse.py -sfile.txt  |run this command and check it
# End of the step


"""
Now, check action = 'store_true' and 'store_false'
for store_true:
If you give a flag it will be True
Else it will be False.
And for store_false it is reverse
"""
# Step 9

# import argparse

# parser = argparse.ArgumentParser(description= 'This is a tutorail for argument parser.')
# parser.add_argument('filename', help='The name of the file that we want to work with.')
# parser.add_argument('-c', '--copy', metavar='N', help='Make N copy.')
# parser.add_argument('-w','--wake_up', action='store_true', help='has she woken up?.')
# argument = parser.parse_args()
# print(argument)
# file = argument.wake_up
# print(file)

# python3 Tutorail_Argparse.py -c 6 -w file.txt
# python3 Tutorail_Argparse.py -c 6 file.txt
# End of the step

"""
What is the argument dest?
with tihs argument we easily can acsses the values of our inputs with costomize name.
"""
# Step 10

# import argparse
# # use .n_d and .copy to see what will happend.
# parser = argparse.ArgumentParser(description= 'This is a tutorail for argument parser.')
# parser.add_argument('filename', help='The name of the file that we want to work with.')
# parser.add_argument('-c', '--copy', dest='n_d', metavar='N', help='Make N copy.')
# parser.add_argument('-w','--wake_up', action='store_true', help='has she woken up?.')
# argument = parser.parse_args()
# print(argument)
# file = argument.n_d
# print(file)

# python3 Tutorail_Argparse.py -c 6 -w file.txt
# End of the step

"""
Action = version, use it when you want to specify the version of your python file.
-v has the highest priority.
"""
# # Step 11

# import argparse

# parser = argparse.ArgumentParser(description= 'This is a tutorail for argument parser.')
# parser.add_argument('filename', help='The name of the file .')
# parser.add_argument('-c', '--copy', dest='n_d', metavar='N', help='Make N copy.')
# parser.add_argument('-w','--wake_up', action='store_true', help='has she woken up?.')
# parser.add_argument('-v', '--version', action='version', help='The version of the file.', version= 'python 10.2')

# argument = parser.parse_args()
# print(argument)
# file = argument.n_d
# print(file)

# you should run python3 Tutorail_Argparse.py -v
# python3 Tutorail_Argparse.py -c 4 -w file.txt -v run this and check the output
# End of the step


"""
Let's work with 'type', type is used for changing the type of the values from string and if it's not
possible give us a nice error. 
"""

# Step 12

# import argparse

# parser = argparse.ArgumentParser(description= 'This is a tutorail for argument parser.')
# parser.add_argument('filename', help='The name of the file .')
# parser.add_argument('-c', '--copy', dest='n_d', metavar='N', help='Make N copy.', type=int)
# parser.add_argument('-w','--wake_up', action='store_true', help='has she woken up?.')
# parser.add_argument('-v', '--version', action='version', help='The version of the file.', version= 'python 10.2')

# argument = parser.parse_args()
# print(argument)
# file = argument.n_d
# print(file)

# End of the step




# Step 13

# working with datatime
# import argparse, datetime


# parser = argparse.ArgumentParser(description= 'This is a tutorail for argument parser.')
# parser.add_argument('filename', help='The name of the file .')
# parser.add_argument('-c', '--copy', dest='n_d', metavar='N', help='Make N copy.', type=int)
# parser.add_argument('-d', '--date', help='the date of file', type=datetime.date.fromisoformat)
# parser.add_argument('-w','--wake_up', action='store_true', help='has she woken up?.')
# parser.add_argument('-v', '--version', action='version', help='The version of the file.', version= 'python 10.2')

# argument = parser.parse_args()
# print(argument)
# file = argument.date
# print(file)

# End of the step


"""
Argparse has a argumnet that is called defult, and it set a defult value for one argument.
"""

# Step 14

# import argparse


# parser = argparse.ArgumentParser(description= 'This is a tutorail for argument parser.')
# parser.add_argument('filename', help='The name of the file .')
# parser.add_argument('-c', '--copy', dest='n_d', metavar='N', help='Make N copy.', type=int)
# parser.add_argument('-w','--wake_up', action='store_true', help='has she woken up?.')
# parser.add_argument('-v', '--version', action='version', help='The version of the file.', version= 'python 10.2')
# parser.add_argument('-n', '--name', help='what is your name?', default='armin')

# argument = parser.parse_args()
# print(argument)
# file = argument.name
# print(file)

# End of the step


"""
You can set an optional argument required and it behave like a positional argument.
"""

# Step 15

# import argparse


# parser = argparse.ArgumentParser(description= 'This is a tutorail for argument parser.')
# parser.add_argument('filename', help='The name of the file .')
# parser.add_argument('-c', '--copy', dest='n_d', metavar='N', help='Make N copy.', type=int)
# parser.add_argument('-w','--wake_up', action='store_true', help='has she woken up?.')
# parser.add_argument('-v', '--version', action='version', help='The version of the file.', version= 'python 10.2')
# parser.add_argument('-n', '--name', help='what is your name?', default='armin', required=True)

# argument = parser.parse_args()
# print(argument)
# file = argument.name
# print(file)

# End of the step


"""
Now we're going to learn 'choices' argument.
choices gives us a list of choice and we can choose one of the choices. 
"""

# Step 16

# import argparse


# parser = argparse.ArgumentParser(description= 'This is a tutorail for argument parser.')
# parser.add_argument('filename', help='The name of the file .')
# parser.add_argument('-c', '--copy', dest='n_d', metavar='N', help='Make N copy.', type=int)
# parser.add_argument('-w','--wake_up', action='store_true', help='has she woken up?.')
# parser.add_argument('-v', '--version', action='version', help='The version of the file.', version= 'python 10.2')
# parser.add_argument('-n', '--name', help='what is your name?', default='armin', choices=['arta', 'mohammad'])

# argument = parser.parse_args()
# print(argument)
# file = argument.name
# print(file)

# End of the step


"""
We want to use 'nargs' argument.
we can enter two or more data using nargs.
"""


# Step 17

# import argparse


# parser = argparse.ArgumentParser(description= 'This is a tutorail for argument parser.')
# parser.add_argument('filename', nargs=2, help='The name of the file .')
# parser.add_argument('-c', '--copy', dest='n_d', metavar='N', help='Make N copy.', type=int)
# parser.add_argument('-w','--wake_up', action='store_true', help='has she woken up?.')
# parser.add_argument('-v', '--version', action='version', help='The version of the file.', version= 'python 10.2')
# parser.add_argument('-n', '--name', help='what is your name?', default='armin', choices=['arta', 'mohammad'])

# argument = parser.parse_args()
# print(argument)
# file = argument.name
# print(file)

# python3 Tutorail_Argparse.py -w -c 4 file.txt file2.txt run these commands
# python3 Tutorail_Argparse.py -w file.txt -c 4 file2.txt
# End of the step


"""
There is a great team work between nargs'?' and defult and const. in ? when you do not use defult value and
you do not give a value to the positional argument it return None.
"""

# Step 18

# import argparse


# parser = argparse.ArgumentParser(description= 'This is a tutorail for argument parser.')
# parser.add_argument('filename', nargs='?', default='file.txt', help='The name of the file.')
# parser.add_argument('-c', '--copy', dest='n_d', metavar='N', help='Make N copy.', type=int)
# parser.add_argument('-w','--wake_up', action='store_true', help='has she woken up?.')
# parser.add_argument('-v', '--version', action='version', help='The version of the file.', version= 'python 10.2')
# parser.add_argument('-n', '--name', help='what is your name?', default='armin', choices=['arta', 'mohammad'])
# parser.add_argument('-d', '--dirname', nargs='?', default='root', help='The name of the directory.', const='root1')

# argument = parser.parse_args()
# print(argument)
# file = argument.dirname
# print(file)


# python3 Tutorail_Argparse.py -w -c 4 file1.txt -d root3
# python3 Tutorail_Argparse.py -w -c 4 file1.txt -d           run all of these commands
# python3 Tutorail_Argparse.py -w -c 4 file1.txt 
# End of the step

"""
Nargs * or + do the same thin you can enter input as many as you want. Just they have one diffrence
and it is when you do not use defult value and you do not give a value to positional 
argument * return an empty list, but + return an error.
"""

# Step 19

# import argparse


# parser = argparse.ArgumentParser(description= 'This is a tutorail for argument parser.')
# parser.add_argument('filename', nargs='*', help='The name of the file.')
# parser.add_argument('-c', '--copy', dest='n_d', metavar='N', help='Make N copy.', type=int)
# parser.add_argument('-w','--wake_up', action='store_true', help='has she woken up?.')
# parser.add_argument('-v', '--version', action='version', help='The version of the file.', version= 'python 10.2')
# parser.add_argument('-n', '--name', help='what is your name?', default='armin', choices=['arta', 'mohammad'])

# argument = parser.parse_args()
# print(argument)
# file = argument.filename
# print(file)

# End of the step




# Step 20

# import argparse


# parser = argparse.ArgumentParser(description= 'This is a tutorail for argument parser.')
# parser.add_argument('filename', nargs='*', help='The name of the file.')
# parser.add_argument('-c', '--copy', dest='n_d', metavar='N', help='Make N copy.', type=int)
# parser.add_argument('-w','--wake_up', action='store_true', help='has she woken up?.')
# parser.add_argument('-v', '--version', action='version', help='The version of the file.', version= 'python 10.2')
# parser.add_argument('-n', '--name', help='what is your name?', default='armin', choices=['arta', 'mohammad'])

# argument = parser.parse_args()
# print(argument)
# file = argument.filename
# print(file)

# End of the step



"""
Now we learn action = append.
with this we can use one label more than once.
"""

# Step 21

# import argparse


# parser = argparse.ArgumentParser(description= 'This is a tutorail for argument parser.')
# parser.add_argument('filename', nargs='*', help='The name of the file.')
# parser.add_argument('-c', '--copy', dest='n_d', metavar='N', help='Make N copy.', type=int)
# parser.add_argument('-w','--wake_up', action='store_true', help='has she woken up?.')
# parser.add_argument('-v', '--version', action='version', help='The version of the file.', version= 'python 10.2')
# parser.add_argument('-n', '--name', help='what is your name?', default='armin', choices=['arta', 'mohammad'])
# parser.add_argument('-a', '--age', help='enter you age.', action='append')

# argument = parser.parse_args()
# print(argument)
# file = argument.age
# print(file)

# End of the step


"""
what is dest argument?
we can send our values to a same destination even from 2 diffrent argument.
And also we have action = 'append_const'.
"""

# Step 22

# import argparse


# parser = argparse.ArgumentParser(description= 'This is a tutorail for argument parser.')
# parser.add_argument('filename', nargs='*', help='The name of the file.')
# parser.add_argument('-c', '--copy', dest='n_d', metavar='N', help='Make N copy.', type=int)
# parser.add_argument('-w','--wake_up', action='store_true', help='has she woken up?.')
# parser.add_argument('-v', '--version', action='version', help='The version of the file.', version= 'python 10.2')
# parser.add_argument('-n', '--name', help='what is your name?', default='armin', choices=['arta', 'mohammad'])
# parser.add_argument('-a', '--age', help='enter you age.', action='append', dest='list1')
# parser.add_argument('-o', '--other', help='other things.', action='append', dest='list1')
# parser.add_argument('-t', '--test', help='other things.', action='append_const', dest='list1', const=11)

# argument = parser.parse_args()
# print(argument)
# file = argument.list1
# print(file)

# End of the step


"""
Action = 'count'
It count the repeat of the label
"""

# Step 23

# import argparse

# parser = argparse.ArgumentParser(description= 'This is a tutorail for argument parser.')
# parser.add_argument('filename', nargs='*', help='The name of the file.')
# parser.add_argument('-c', '--copy', dest='n_d', metavar='N', help='Make N copy.', type=int)
# parser.add_argument('-w','--wake_up', action='store_true', help='has she woken up?.')
# parser.add_argument('-v', '--version', action='version', help='The version of the file.', version= 'python 10.2')
# parser.add_argument('-n', '--name', help='what is your name?', default='armin', choices=['arta', 'mohammad'])
# parser.add_argument('-a', '--age', help='enter you age.', action='count', default=0)



# argument = parser.parse_args()
# print(argument)
# file = argument.age
# print(file)

# End of the step

"""
action = append vs action = extend.
these are the same with one diffrence that we show it below.
"""


# Step 24

# import argparse

# parser = argparse.ArgumentParser(description= 'This is a tutorail for argument parser.')
# parser.add_argument('filename', nargs='*', help='The name of the file.')
# parser.add_argument('-c', '--copy', dest='n_d', metavar='N', help='Make N copy.', type=int)
# parser.add_argument('-w','--wake_up', action='store_true', help='has she woken up?.')
# parser.add_argument('-v', '--version', action='version', help='The version of the file.', version= 'python 10.2')
# parser.add_argument('-n', '--name', help='what is your name?', default='armin', choices=['arta', 'mohammad'])
# parser.add_argument('-a', '--age', help='enter you age.', action='append', nargs='*')
# parser.add_argument('-o', '--other', help='other thing.', action='extend', nargs='*')



# argument = parser.parse_args()
# print(argument)
# file = argument.age
# file1 = argument.other
# print(file)
# print(file1)

# python3 Tutorail_Argparse.py -w -c 4 file.txt -a 2 -o 4 -a 0 7 9 -o 20 30 40
# End of the step

