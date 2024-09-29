from flask import Flask, jsonify
from server_metrics import get_cpu_usage, get_process_info, get_memory_usage, get_disk_usage, get_health_status

app = Flask(__name__)

@app.route('/cpu', methods=['GET'])
def cpu_usage():
    cpu_percent = get_cpu_usage()
    return jsonify(cpu_usage=cpu_percent)

@app.route('/process', methods=['GET'])
def process_info():
    processes = get_process_info()
    return jsonify(processes=processes)

@app.route('/memory', methods=['GET'])
def memory_usage():
    memory_stats = get_memory_usage()
    return jsonify(memory_usage=memory_stats)

@app.route('/dist', methods=['GET'])
def disk_usage():
    disk_stats = get_disk_usage()
    return jsonify(disk_usage=disk_stats)

@app.route('/healthz', methods=['GET'])
def healthz():
    status = get_health_status()
    return jsonify(health_status=status)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)  

