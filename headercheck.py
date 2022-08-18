#imports required modules
import csv
import numpy as np
#function for checking headers
def check_headers(fileName):
    file = open(fileName, 'r')
    data = list(csv.reader(file))
    if len(data[0])!=12: #check header number
        return False
    #headers required
    headers = "batch_id","timestamp","reading1","reading2","reading3","reading4","reading5","reading6","reading7","reading8","reading9","reading10" #expected headers

    for i in range(0,len(data[0])): #check header value
        if data[0][i] != headers[i]:
            print(data[0][i])
            return False
    
    return True