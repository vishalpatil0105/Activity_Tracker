# import requests and date time modules
import requests
import datetime

# Grabbing today's date in such a format that we can work with api

today = datetime.date.today().strftime("%Y%m%d")

# All constants for this code

USER_NAME = "vishal1683"
PASS = "vishal1clasdbsadldsa"
GRAPH_NAME = "Graph1"
GRAPH_ID = "abc176"

# API Request for creating user

USER_REQ = "https://pixe.la/v1/users"

# Parameters

user_param = {
    "token": PASS,
    "username": USER_NAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# Sending post request {after sending request please comment this line else it
# will throw error user already exists }

      # reate_acc = requests.post(url=USER_REQ, json=user_param)
      #print(create_acc.text)

# URL for creating graph

graph_url = f"{USER_REQ}/{USER_NAME}/graphs"

# parameters

graph_param = {
    "id": GRAPH_ID,
    "name": GRAPH_NAME,
    "unit": "hour",
    "type": "int",
    "color": "sora"
}
# It's kwargs Type of argument {in this case its kind of pass for our user name}
headers = {
    "X-USER-TOKEN": PASS
}

# Sending post request {after sending request please comment this line else it
# will throw error user already exists }

      # graph_data = requests.post(url=graph_url, json=graph_param, headers=headers)
      # print(graph_data.text)
      # get_graph_url = f"{USER_REQ}/{USER_NAME}/graphs/{GRAPH_ID}"
      # graph = requests.post(get_graph_url)

# URL for actually putting data in our graph

put_data_in_graph_url = f"{USER_REQ}/{USER_NAME}/graphs/{GRAPH_ID}"

# {date: "it wil automatically fetch current date via datetime module in API required format using strftime method"
#  quantity: " input from user side to specify that how much time he/she did activity in a day"
param = {
    "date": today,
    "quantity": input("Enter Hour of coding: ")
}

# sending data to graph
put_data = requests.post(url=put_data_in_graph_url, json= param, headers= headers)
print(put_data.text)

# using this ur we can see actual graph of our working
# https://pixe.la/v1/users/put_user_name/graphs/put_graph_id.html