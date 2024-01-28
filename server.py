from flask import Flask, request
import socket
import subprocess

seed = 0
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def serve():
    global seed

    if request.method == 'POST':
        seed = request.get_json().get('num')
        # subprocess.Popen(["python3", "stress_cpu.py"]) 
        return str(seed)
        

    if request.method == 'GET':
        ip_address = socket.gethostname()
        return str(seed)


if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000)


# curl -X POST -H "Content-Type: application/json" -d '{"num": }' http://3.19.26.145:5000
# curl -X GET http://3.19.26.145:5000
# curl -X GET http://18.218.145.23:5000

# ssh -i /Users/aishi_huang/Desktop/aishuang_ec2_01.pem ec2-user@3.19.26.145
# ssh -i /Users/aishi_huang/Desktop/aishuang_ec2_01.pem ec2-user@18.218.145.23
# ssh -i /Users/aishi_huang/Desktop/aishuang_ec2_01.pem ubuntu@13.59.63.110

# python3 -m venv venv
# source venv/bin/activate
# pip install flask