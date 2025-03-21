from flask import Flask, jsonify
app= Flask(__name__)
@app.route('/run-script',methods=['GET'])
def run_script():
    print(3.14*(80**2))
    return jsonify({"message": "Python script executed"})