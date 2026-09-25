from json import JSONDecodeError
from flask import Flask, request, json

app = Flask(__name__)

from flask import Flask, make_response
app = Flask(__name__)

data = [
    {
        "id": "3b58aade-8415-49dd-88db-8d7bce14932a",
        "first_name": "Tanya",
        "last_name": "Slad",
        "graduation_year": 1996,
        "address": "043 Heath Hill",
        "city": "Dayton",
        "zip": "45426",
        "country": "United States",
        "avatar": "http://dummyimage.com/139x100.png/cc0000/ffffff",
    },
    {
        "id": "d64efd92-ca8e-40da-b234-47e6403eb167",
        "first_name": "Ferdy",
        "last_name": "Garrow",
        "graduation_year": 1970,
        "address": "10 Wayridge Terrace",
        "city": "North Little Rock",
        "zip": "72199",
        "country": "United States",
        "avatar": "http://dummyimage.com/148x100.png/dddddd/000000",
    },
    {
        "id": "66c09925-589a-43b6-9a5d-d1601cf53287",
        "first_name": "Lilla",
        "last_name": "Aupol",
        "graduation_year": 1985,
        "address": "637 Carey Pass",
        "city": "Gainesville",
        "zip": "32627",
        "country": "United States",
        "avatar": "http://dummyimage.com/174x100.png/ff4444/ffffff",
    },
    {
        "id": "0dd63e57-0b5f-44bc-94ae-5c1b4947cb49",
        "first_name": "Abdel",
        "last_name": "Duke",
        "graduation_year": 1995,
        "address": "2 Lake View Point",
        "city": "Shreveport",
        "zip": "71105",
        "country": "United States",
        "avatar": "http://dummyimage.com/145x100.png/dddddd/000000",
    },
    {
        "id": "a3d8adba-4c20-495f-b4c4-f7de8b9cfb15",
        "first_name": "Corby",
        "last_name": "Tettley",
        "graduation_year": 1984,
        "address": "90329 Amoth Drive",
        "city": "Boulder",
        "zip": "80305",
        "country": "United States",
        "avatar": "http://dummyimage.com/198x100.png/cc0000/ffffff",
    }
]


@app.route('/')
def index():
    print("👉 HITTING THE HOME ROUTE 👈")  # Add this line!
    course = request.args.get('course')
    rating = request.args.get('rating')
    return {
        "message": "success",
        "course": course,
        "rating": rating    
    }

@app.route('/no_content')
def no_content():
   return "No Content", 200

@app.route('/data')
def get_data():
    try:
        # Check if data exists and has a length greater than 0
        if data and len(data) > 0:
            return {"message": f"Data of {len(data)} found"}
        else:
            return {"message": f"Data is empty"}, 500
    except NameError:
        return {"message": "Data not found"}, 404

@app.route('/name_search')
def name_search():
    """
    Find a person in the database.

    Returns:
        json: Person if found, with status of 200
        400: If argument 'q' is missing from the request
        422: If argument 'q' is present but invalid (e.g., empty or numeric)
        404: If person is not found in the data
    """

    query = request.args.get('q')

    print(query.lower())

    if query is None:
        return {
            "message": "Query Parameter q is missing"
        }, 400

    if query.strip() == "" or query.isdigit():
        return {
            "message": "Invalid query parameter"
        }, 422

    for person in data:
        print(person["first_name"].lower())
        if query.lower() in person["first_name"].lower():
            return person, 200

    return {
        "message": "Person not found"
    }, 404

@app.route("/person")
def add_by_uuid():
    query_string = request.args.get('q') # http://127.0.0.1:5000/person?q={%22name%22:%22Alice%22,%22age%22:30}

    if not query_string:
        return {
            "error": "Missing query parameter 'q'"
        }, 400

    try:
        data_dict = json.loads(query_string)
        print(data_dict)

        data.append(data_dict)

        return data, 200

    except json.JSONDecodeError:
        return {    
            "error" : "Invalid JSON format in URL"
        }, 400

@app.route("/person/unique_identifier")
def get_by_id():
    query_string = request.args.get('q')

    for each in data:
        if query_string == each['id']:
            return each, 200
    return {"message": "No data found"}, 400


@app.route("/person/count")
def count():
    try: 
        return {"total": len(data)}, 200
    except NameError:
        return {"message": "data not found"}, 400

if __name__ == "__main__":
    app.run(debug=True) 
 