from flask import Flask

app = Flask(__name__)

@app.route("/", methods=['GET'])
def hello():
  return {
    "message": "use /usage to get information"
  }
  
@app.route("/usage", methods=['GET'])
def help():
  return {
    "message": "use FIFO, SSTF, SCAN or CSCAN algorithms",
    "instructions":{
      "endpoint":"/sched",
      "method": "POST",
      "payload":{
        "algorithm": "1:FCFS, 2:SSTF, 3:SCAN, 4:CSCAN, 5:LOOK, 6:CLOOK",
        "tracks": "number of cylinders",
        "arm": "initial position",
        "requests":"list of tracks"
      },
      "payload_example":{
        "algorithm": 1,
        "tracks":200,
        "arm": 96,
        "requests":[125,17,23,67,90,128,189,115,97]
      },
      "description": "This endpoint perform disk scheduling algorithms"
    }
  }
  
if __name__ == "__main__":
  app.run(host="0.0.0.0", port=8000)

