from flask import Flask, request
import socket
import subprocess

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def serve():

    if request.method == 'POST':
        subprocess.Popen(["python", "stress_cpu.py"]) 
        

    if request.method == 'GET':
        ip_address = socket.gethostname()
        return ip_address


if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000)
