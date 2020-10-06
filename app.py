import urllib.request, json 
from time import sleep
import datetime

safka_url = "https://eliittisafka.herokuapp.com/stats"
safka_file = "safka.jfa"

def load():
    contents = ""
    with open(safka_file, "r+") as f:
        for i in f.readlines():
            contents = contents + i + "\n"
    f.close()
    print("Pre-existing data: " + str(contents))
    return json.loads(contents)
def save(data):
    contents = json.dumps(data)
    with open(safka_file, "w+") as f:
        f.write(contents)
    f.close()
def get():
    data = {}
    print("Getting data...")
    with urllib.request.urlopen(safka_url) as url:
        data = json.loads(url.read().decode())
    return data
def getDate():
    return datetime.datetime.today().day + ((datetime.datetime.today().hour + (datetime.datetime.today().minute / 60)) / 24.0)
if __name__ == "__main__":
    print(getDate(), datetime.datetime.today().hour)
    input("Press enter to start.\n")
    data = {}
    try:
        print("Loading pre-existing data...")
        data = load()
    except Exception as e:
        print("Loading pre-existing data FAILED.")
    print("Starting the clock!")
    for i in range(10000):
        if str(datetime.datetime.today().hour) in ["8", "9", "10", "11", "12", "13", "14", "15", "18"]:
            print("Wake up!")
            data[getDate()] = get()
            print(str(len(data)) + " indicies collected total!")
            save(data)
        sleep(10000)
