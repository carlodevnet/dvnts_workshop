import requests

'''
TO DO: Assign the values to the variables from the create_room.py script
you can simply copy and paste the values. No need to get them from the file.
'''
access_token = [TO_DO]
room_id = [TO_DO]


'''
TO DO: Complete the URL for the HTTP Request to add an user to the room
'''
url = 'https://webexapis.com/v1/[TO_DO]'

header_req = {
    'Authorization': f'Bearer [TO_DO]',
    'Content-Type': 'application/json',
}


'''
Create the body to add to the API request
TO DO: Add the missing items
'''
body = {
    "roomId": [TO_DO],
    "text": "This is a test message!"
}

'''
TO DO: Add the missing items to complete the HTTPs request and make sure to use the correct method
'''
res = requests.[TO_DO](url, headers=[TO_DO], json=[TO_DO])


'''
TO DO: Complete the snippet checking the response status code
'''
if res.status_code == [TO_DO]:
    print("Message Sent!")
else:
    print("Something went wrong! Please retry!")