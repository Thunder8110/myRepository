import requests
import time
import itertools

def check(id):
  while True:
    response = requests.get("https://api.mojang.com/users/profiles/minecraft/" + id)
    status_code = response.status_code
    if status_code == 200:
      return False
    elif status_code == 204:
      return True
    
    print("Some exception has occured. Wait 10 seconds...")
    time.sleep(10)
  
usable_list = []
char_list = [chr(i) for i in range(48, 58)]
char_list.extend([chr(i) for i in range(97, 123)])
for chars in itertools.product(char_list, repeat=3):
  id = "".join(chars)
  usable = check(id)
  print(id + ": " + str(usable))
  if usable:
    usable_list.append(id)
  time.sleep(2)
      
print("--------")
print(usable_list)