import pickle
import requests

url='https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'

resp = requests.get(url)
text1 = resp.text.splitlines()
text = [[i] for i in text1]

file = 'iris.pkl'
# Pickling data
fileObj = open(file, 'wb')
pickle.dump(text, fileObj)
fileObj.close()

# Getting data 
fileObj1 = open(file, 'rb')
d = pickle.load(fileObj1)
print(d)
fileObj1.close()