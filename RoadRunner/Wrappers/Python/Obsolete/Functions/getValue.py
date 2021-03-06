import rrPython
import os
import csv
os.chdir('C:\\RoadRunner\\bin')

function = 'getValue'
rrPython.loadSBMLFromFile('C:\\RoadRunner\\Models\\feedback.xml')

species = 'S1'

try:
    concentration = rrPython.getValue(species)
    if str(concentration) is not False:
        result = 'True'
    else:
        result = 'False'
except:
    result = 'False'


PythonTestResults = open('C:\\RoadRunner\\PythonTestResults.csv','a')
writer = csv.writer(PythonTestResults)
writevar = function + '=' + result
writer.writerow([writevar])
PythonTestResults.close()