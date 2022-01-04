import requests
import json
import yaml

def getAPIKey():
    with open('config.yaml', 'r') as ymlfile:
        cfg = yaml.safe_load(ymlfile)
    return cfg['MAPS_API_KEY']

def getTimes(origins, destinations, mode):
    key = getAPIKey()
    url = "https://maps.googleapis.com/maps/api/distancematrix/json?origins="+origins+"&destinations="+destinations+"&mode="+mode+"&key="+key
    payload={}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    data = response.json()
    
    results = []
    durations = data['rows'][0]['elements']
    for duration in durations:
        results.append(duration['duration']['value'])
    
    return results

def generateText(time, mode):
    mins = time // 60
    if mode == "transit":
        return "Transit takes " + str(mins) + " minutes."
    elif mode ==  "driving":
        return "Driving time is " + str(mins) + " minutes."
    elif mode ==  "walking":
        return "Walking time is " + str(mins) + " minutes."
    elif mode ==  "bicycling":
        return "Bicycling time is " + str(mins) + " minutes."

def main(addresses, target, city, modes=['driving', 'walking', 'bicycling', 'transit']):
    origins = requests.utils.quote(target.strip()+', '+city.strip())
    destinationsList = []
    
    for address in addresses:
        stripped = address.strip()
        withCity = stripped + ", " + city.strip()
        destinationsList.append(withCity)
    destinations = requests.utils.quote("|".join(destinationsList))

    results = {}
    for mode in modes:
        results[mode] = getTimes(origins, destinations, mode)

    
    output = []
    for destNo in range(len(destinationsList)):
        time = results[modes[0]][destNo]
        mode = modes[0]
        for modeNo in range(1,len(modes)):
            if results[modes[modeNo]][destNo] < time:
                time = results[modes[modeNo]][destNo]
                mode = modes[modeNo]
        output.append(generateText(time, mode))
    
    return output

def lambda_handler(event, context):
    
    if not 'add' in event or not 'tgt' in event or not 'city' in event or not 'modes' in event:
        return {
            'statusCode': 200,
            'body': json.dumps("Error: Missing parameter for this API.")
        }
    
    result = main(event['add'], event['tgt'], event['city'], event['modes'])
    #result = "Test"

    return {
        'statusCode': 200,
        'body': {"messages": result}
    }

test = {
    "add": ["Friedrich-Ebert-Strasse", "Kellermannstraße 2 "],
    "tgt": "Bentelerstraße 62",
    "city": "Münster",
    "modes": ["driving", "bicycling", "transit"]
}

print(lambda_handler(test, None))