from flask import Flask, request, jsonify
from fcfs import fcfs

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
        "algorithm": "1:FCFS, 2:SSTF, 3:SCAN_ASC, 4:SCAN_DESC, 5:CSCAN_ASC, 6:CSCAN_DESC, 7:LOOK, 8:CLOOK",
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
  
@app.route("/sched", methods=['POST'])
def sched():
  data = request.get_json()
  algorithm = data.get("algorithm")
  tracks = data.get("tracks")
  arm = data.get("arm")
  requests = data.get("requests")
  
  if algorithm == 1:  ## FCFS
    result = fcfs(arm, requests)
  else:
    return jsonify({"error": "Invalid algorithm"}), 400
  
  return jsonify({
    "result": result
  }), 200
      
if __name__ == "__main__":
  app.run(host="0.0.0.0", port=8000)

