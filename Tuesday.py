# Luisa timothy 25-02-2018
# is it Tuesday?

import datetime #imports a repository which is builtin but needs to be activated

if datetime.datetime.today().weekday() == 1:
  print("Yay it is Tuesday")
else:
  print("I am sorry it's not Tuesday")