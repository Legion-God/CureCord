from app import app 
#TODO: Remove the debug option in production.
if __name__ == '__main__':
    app.run(debug=True)