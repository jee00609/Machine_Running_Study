import urllib.request
import json
data = {
        "Inputs": {
                "input1":
                [
                    {
                            '지점': "32",   
                            '날짜': "2019-11-05T00:00:00Z",   
                            '온도': "50.1",   
                            '연료비': "1.27",   
                            '소비자물가지수': "300.096357",   
                            '실업률': "5.12",   
                            '부서': "11",   
                            '휴일여부': "true",   
                            '유형': "C",   
                            '규모': "211200",   
                    }
                ],
        },
    "GlobalParameters":  {
    }
}

body = str.encode(json.dumps(data))

url = 'https://ussouthcentral.services.azureml.net/workspaces/2db5dc0d6a6c4177b249d431ea135499/services/c1e18fff34544ac0b58741cc0d913913/execute?api-version=2.0&format=swagger'
api_key = '3CbWcQ5V5bLitC2rek6OxQouD3p2NNgTT9CrNXoiTmNVyPz+xcxyiB9qZRhB3XIfzr1qUJ/2vPiONlOnsKGecA==' # Replace this with the API key for the web service
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
