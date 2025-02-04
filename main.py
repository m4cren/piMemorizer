from website import create_website, socketio, ip_address, db


app = create_website()


@app.teardown_appcontext
def shutdown_session(exception=None):
        db.session.remove()

if __name__ == '__main__':
     socketio.run(app, host='0.0.0.0')



