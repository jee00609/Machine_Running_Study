import urllib.request
import json

data = {
        "Inputs": {
                "input1":
                [
                    {
                            '선실등급': "1",   
                            '성별': "female",   
                            '나이': "20",   
                            '형제배우자수': "1",   
                            '부모자식수': "1",   
                            '요금': "230",   
                            '출항지': "C",   
                    }
                ],
        },
    "GlobalParameters":  {
    }
}

body = str.encode(json.dumps(data))

url = 'https://ussouthcentral.services.azureml.net/workspaces/2db5dc0d6a6c4177b249d431ea135499/services/56851aa2f4784142a05820521b87649e/execute?api-version=2.0&format=swagger'
api_key = '0ww4vhygErLQ5T6FI5DhQJW175MMh6WzYAlLNbFnn1GN0+UNforXKhLWuv95lPlnFvthol5qi3mR6FLSVxnJbA==' # Replace this with the API key for the web service
headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}

req = urllib.request.Request(url, body, headers)

try:
    response = urllib.request.urlopen(req)

    result = response.read()
    print(result)
except urllib.error.HTTPError as error:
    print("The request failed with status code: " + str(error.code))

    # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
    print(error.info())
    print(json.loads(error.read().decode("utf8", 'ignore')))
