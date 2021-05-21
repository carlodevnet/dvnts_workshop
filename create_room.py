import requests
import json


'''
TO DO: Complete the script to open the JSON file and get the token
'''
with open(f"./token.json", "r") as file:
    get_token = json.load([TO_DO])

access_token = [TO_DO]


# DO NOT MODIFY THIS CODE UNLESS INSTRUCTED TO DO SO
name = input("Inserire il proprio nome: ")
surname = input("Inserire il proprio cognome: ")

# Create a Room
print("Creating the Room....")

'''
TO DO: Complete the URL for the HTTP Request to create a room
'''
url = 'https://webexapis.com/v1/[TO_DO]'


'''
TO DO: Add the missing items to complete the headers
'''
headers = {
    'Authorization': f'Bearer [TO_DO]'
}

'''
Create the body to add to the API request
For example: if the name and the surname are Carlo DevNet
then the name of the room should be "DevNet Scholarship - Carlo DevNet"
TO DO: Add the missing items
'''
body = {
  "title": f"DevNet Scholarship - [TO_DO] [TO_DO]"
}


'''
TO DO: Add the missing items to complete the HTTPs request and make sure to use the correct method
'''
res = requests.[TO_DO](url, headers=headers, data=[TO_DO])


'''
TO DO: Record the name of room id into the room_id variable and show the ID
'''
if res.status_code == [TO_DO]:
    room_id = res.json()['id']
    print(f"Room ID is: {room_id}")
else:
    print("Something went wrong! Please retry!")
