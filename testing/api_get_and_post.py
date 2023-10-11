# `pip install requests json`
import requests
import json

# this is in progress

def get_data(api_url, headers):
  """
  Sends a GET request to given API URL with the given headers.

  Returns
  -------
  The JSON response from the API as a Python dictionary (if request was succesful).
  """
  response = requests.get(api_url, headers=headers)
  if response.status_code == 200:
      return response.json()
  else:
      response.raise_for_status()


def process_data(data):
  """
  
  """
  print(data)
  return data


def post_data(api_url, data, headers):
  """
  Sends a POST request to given API URL with the given data and headers.

  Returns
  -------
  `True` if the request was successful, `False` otherwise.
  """

  response = requests.post(api_url, data=json.dumps(data), headers=headers)

  if response.status_code == 200:
      print("Processed data sent successfully - bingo!")
      return True
  else:
      response.raise_for_status()
      return False


def main():

  get_api_url = ''
  post_api_url = ''

  # Ideally get this from a config file or environment variable
  API_KEY = ''

  if(API_KEY == '' or get_api_url == '' or post_api_url == ''):
    raise ValueError("Please provide API key and URLs")
    exit()

  # Headers for GET and POST requests
  HEADERS = {
      'Content-Type': 'application/json',
      'Authorization': f'Bearer {API_KEY}' 
  }

  # Step 1: Fetch data from API
  try:
    fetched_data = get_data(get_api_url, HEADERS)
    print("Data fetched successfully!")

  except requests.RequestException as e:
    print(f"An error occurred when fetching the data: {str(e)}")
    print("Status code: ", e.response.status_code)


  # Step 2: Process data
  processed_data = process_data(fetched_data)
  print("Data processed successfully!")


  # Step 3: Send data to API
  try:
    post_data(post_api_url, processed_data, HEADERS)
  
  except requests.RequestException as e:
    print(f"An error occurred sending the data: {str(e)}")
    print("Status code: ", e.response.status_code)

if __name__ == "__main__":
  main()