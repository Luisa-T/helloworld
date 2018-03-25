# Luisa Timothy 01-03-2018
# homework task week 6 Iris data

with open("irisdata.csv") as f: #create block of python code where f is a variable and everything indented after can access the variable
  for line in f: # for each line in the data set do the following (Thank you Sarah), I spent several weeks trying to solve this but could not
   print('{:8}{:8}{:8}{:8}'.format(line.split(',')[0], line.split(',')[1], line.split(',')[2], line.split(',')[3]))