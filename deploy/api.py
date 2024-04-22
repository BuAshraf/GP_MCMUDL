from flask import Flask, request, jsonify
from help import predict_image


app = Flask(__name__)


@app.route('/')
def home():
	return "Hello world"

@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
    
    if request.method == 'POST':
        f = request.files['file']
        f.save('deploy\\images\\'+f.filename)
        print(f.filename)
        results = predict_image('deploy\\images\\'+f.filename) 
        return jsonify({'obj':results})

if __name__ == "__main__":
    app.run(debug=True)