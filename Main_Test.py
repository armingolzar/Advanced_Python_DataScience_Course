import Main_Tutorial

Main_Tutorial.Hi()

print(Main_Tutorial.add(8, 9))

"""
So, as you can see there is a big problem here because when we import another python file, python run
all the file first and after that python run commands in this file.

what should we do???

It would be great if there was a flag that we could show Python
and let Python know which file we want to run.

Baaaaaaaaaaam :) name is here.
"""

# First do this practis
# print(__name__)


"""
So, after doing these practises you can realize that by defult __name__ is __main__ but, if you import one 
file in another file at first __name__ is the name of the file that is imported(* at running import *) and
after that in file which we run __name__ is __main__.
Please be careful about it.

At last yes __name__ is flag
"""

# Main_Tutorial.Hi()
# print(Main_Tutorial.add(8, 9))
# print(Main_Tutorial.sub(50, 20))

# here we go. Now you know what is main() function.
