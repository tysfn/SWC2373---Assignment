import requests
import json

def test_webex_connection(token):
    webex_api_url = "https://webexapis.com/v1/ping"

    headers = {"Authorization": f"Bearer {token}"}

    response = requests.get(webex_api_url, headers=headers)

    if response.status_code == 200:
        print("Connection to Webex server successful!")
        return True
    else:
        print("Connection to Webex server failed. Please check your Webex token.")
        return False
    
def get_user_info(token):
      user_info_url = "https://webexapis.com/v1/people/me"
      headers = {"Authorization": f"Bearer {token}"}
      response = requests.get(user_info_url, headers=headers)

      if response.status_code ==200:
         user_data = response.json()
         print("User Information:")
         print("Displayed Name:", user_data.get("displayName"))
         print("Nickname:", user_data.get("nickName"))
         print("Emails:", user_data.get("emails"))

      else:
         print("User information failed.Please check your Webex token.")

def list_rooms(token):
      list_rooms_url = "https://webexapis.com/v1/rooms"

      headers = {"Authorization": f"Bearer {token}"}
      response = requests.get(list_rooms_url, headers=headers)
      
      if response.status_code == 200:
        rooms_data = response.json()
        print("List of Rooms:")
        for room in rooms_data["items"][:5]:
            print("Room ID:", room["id"])
            print("Room Title:", room["title"])
            print("Date Created:", room["created"])
            print("Last Activity:", room["lastActivity"])
            print()

      else:
        print("List failed. Please check your token")
       
            

def create_room(token, room_title):
      create_room_url = "https://webexapis.com/v1/rooms"

      headers = {
         "Authorization": f"Bearer{token}",
         "Content-Type": "application/json"
      }

      data = {"title": room_title}
      response = requests.post(create_room_url, headers=headers, json=data)

      if response.status_code == 200:
          print(f"Room '{room_title}' created successfully!")

      else:
          print("Failed. Please check your token and try again.")

def send_message(token, room_id, message):
    send_message_url ="https://webexapis.com/v1/messages"

    headers = {
         "Authorization": f"Bearer{token}",
         "Content-Type": "application/json"
      }
    
    data ={"roomId": room_id, "text": message}

    response = requests.post(send_message_url, headers=headers, json=data)
    
    if response.status_code == 200:
          print("Message sent!!")
          
    else:
          print("Failed to send the message")

def main():
        print("Main Menu: ")
        print("0. Test Webex Connection")
        print("1. User Information")
        print("2. List top 5 rooms")
        print("3. Create a room")
        print("4. Send Message")
        choice = input("Please select an option (0/1/2/3/4): ")

        if choice =="0":
            webex_token = input("Please enter your Webex token: ")
            if test_webex_connection(webex_token):
                print("Connection successfull")
            else:
                print("Connection failed. Please check and try again")
            main()
        
        elif choice == "1":
            webex_token = input("Please enter your Webex token number: ")
            get_user_info(webex_token)
            main()

        elif choice == "2":
            webex_token = input("Please enter your Webex token number: ")
            rooms = list_rooms(webex_token)
            main()

        elif choice == "3":
            webex_token = input("Please enter your Webex token number: ")
            room_title = input("Enter the title for the new room: ")
            create_room(webex_token, room_title)
            main()

        elif choice == "4":
            webex_token = input("Please enter your Webex token number: ")
            rooms = list_rooms(webex_token)
            if rooms:
                room_choice = input("Please select a room (1-5): ")
                if room_choice.isdigit() and 1 <= int(room_choice) <= 5:
                            room_id = rooms[int(room_choice) - 1]["id"]
                            message = input("Enter the message you want to send: ")
                            send_message(webex_token, room_id, message)
                else:
                    print("Invalid room. Please choose a room (1-5).")
            main()

if __name__ == "__main__":
     main()