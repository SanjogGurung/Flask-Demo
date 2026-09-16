from flask import Flask
import requests

app = Flask(__name__)

@app.route('/author')
def get_author():
    res = requests.get("https://api.restful-api.dev/objects")
    if res.status_code == 200:
        return {"message": "success", "collections": res.json()}, 200
    elif res.status_code == 404:
        return {"message": "error", "collections": "Collections not found"}, 404

    else:
        return {"message": "Something went wrong"}, 500   

if __name__ == '__main__':
    app.run(debug=True) 