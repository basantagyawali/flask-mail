from app import create_app
import os

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
print("Inside")

#if any problem occur then uncomment app.run() and run this file python 
app.run()
