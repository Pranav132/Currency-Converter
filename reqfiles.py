#this class is used to create basic functions that will be implemented
#these functions are: request json file, accept input and output currency, accept input amount, output value

from urllib.request import urlopen
import json

def loadjson():
    #requesting json from internet with exchange rates
    with urlopen("http://www.floatrates.com/daily/usd.json") as response:
        source = response.read()

    #loading imported json into local json file
    data = json.loads(source)

    #as usd does not exit on file, making a usd key in dictionary
    data["usd"] = {
        "code": "USD",
        "name": "Unites States Dollar",
        "rate": 1,
        "inverseRate": 1
    }

    return data

#creating a list of currencies
def makeList():
    data = loadjson()

    #making a list with set of names for drop down menu
    lis = []
    
    #adding keys to list
    for key,value in data.items():
        lis.append(key.upper())

    lis = sorted(lis)
    return lis




