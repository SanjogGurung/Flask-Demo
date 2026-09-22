from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    course = request.args.get('course')
    rating = request.args.get('rating')
    return {
        "message": "success",
        "course": course,
        "rating": rating    
    }

@app.route('/no_content')
def no_content():
   return "", 204 

if __name__ == '__main__':
    app.run(debug=True) 
 