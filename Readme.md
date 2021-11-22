# Cafe Test Api

### This IS an Api Build with (100 Days of Python Course)
get all the data

endpoint = 'http://127.0.0.1:5000/all'
request = GET

get random cafe

endpoint = 'http://127.0.0.1:5000/random'
request = GET

search for cafe by location

endpoint = 'http://127.0.0.1:5000/search?loc=(Your_location)'
request = GET


Add new Cafe

endpoint = 'http://127.0.0.1:5000/add'
request = POST
data = {
    'id':'',
    'name': '',
    'map_url': '',
    'img': '',
    'location': '',
    'hase_sokects': '',
    'has_toilet': '',
    'has_wifi': '',
    'can_take_calls': '',
    'seats': '',
    'coffie_price': ''
}

Change specific piece of data

endpoint = 'http://127.0.0.1:5000/update/<id>'
request = PATCH
data={
    'column_name' : 'new_name'
}
