from flask import Flask 

app = Flask(__name__)

from app import doc_routes
from app import patient_routes