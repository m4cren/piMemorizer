from website import create_website, socketio, ip_address, db


app = create_website()
<<<<<<< HEAD

@app.teardown_appcontext
def shutdown_session(exception=None):
        db.session.remove()

if __name__ == '__main__':
     socketio.run(app, host='0.0.0.0')
=======
@app.teardown_appcontext
def shutdown_session(exception=None):
        db.session.remove()
if __name__ == '__main__':
     socketio.run(app,  host = '0.0.0.0')
>>>>>>> 79d7d863f63b152934eeb06418f2775033f8b749
