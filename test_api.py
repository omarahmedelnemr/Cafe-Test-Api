import requests

# data = {
#     'id':'23',
#     'name': 'my love2',
#     'map_url': 'https://lh3.googleusercontent.com/p/AF1QipOMzXpKAQNyUvrjTGHqCgWk8spwnzwP8Ml2aDKt=s0',
#     'img': 'https://lh3.googleusercontent.com/p/AF1QipOMzXpKAQNyUvrjTGHqCgWk8spwnzwP8Ml2aDKt=s0',
#     'location': 'egypt',
#     'hase_sokects': '1',
#     'has_toilet': '1',
#     'has_wifi': '1',
#     'can_take_calls': '0',
#     'seats': '40',
#     'coffie_price': '10$'
# }
data2 ={
    'name':'your love'
}

# response = requests.get('http://127.0.0.1:5000/random')#,data = data)
response = requests.patch('http://127.0.0.1:5000/update/22',data = data2)


response =response.text


print(response)