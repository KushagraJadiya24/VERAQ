import json

try:
    with open("data.json","r") as file:
        data = json.load(file)

    print("original Data: ",data)

    print(data[0]["name"])

    print(data[0]["projects"][0]["status"])
    data[0]["projects"][0]["status"] = "Completed"
    print(data[0]["projects"][0]["status"])

    data[0]["projects"].append({
        "name":"fedsentry",
        "status":"Development"
    })


    
    with open("data.json", "w") as file:
        json.dump(data, file, indent=4)
except Exception as e:
    print(f"Unexpected error: {e}")