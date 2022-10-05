#!/usr/bin/python3
'''Task 1'''

 def write_file(filename="", text=""):
      ''' a function that writes a text file'''
       with open(filename, encoding="utf-8") as file:
            file.write(text)
        return len(text)
