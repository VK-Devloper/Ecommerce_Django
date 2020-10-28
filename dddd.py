b = {'1': {
              'id': '1',
              'title': 'foot',
              'price': '23',
              'quantity': '9',
              'total_price': '999'
          }
     }

# b['1']['vk'] = 'vaibhav'
#
# print(b['1']['vk'])

for i in b.values():
    print(i['id'])