import os
import firebase_admin
from firebase_admin import firestore, credentials
from flask import jsonify, Flask
from flask_cors import CORS

# Initialize a Flask application
app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

# Initialize Firebase Admin SDK
firebase_admin.initialize_app()
# Retrns a client object connected to Firestore db
db = firestore.client()

@app.route("/")
def count_visitors():
    # Reference to a document in a specific collection
    ref = db.collection('visitorcount').document('qF1aQrKv29nPMAn0463m')
    # Update field in database
    ref.update({'VisitorCount': firestore.Increment(1)})

    visitor_count = ref.get().to_dict()['VisitorCount']
    response = jsonify({'Visitor Count!!': visitor_count})
    return response

if __name__ == "__main__":
    app.run(debug=True)
