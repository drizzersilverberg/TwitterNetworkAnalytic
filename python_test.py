import requests

r = requests.get('http://tna-api.herokuapp.com/user?q=barackobama&row=10')
print r