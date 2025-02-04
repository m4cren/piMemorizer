from website import create_website, socketio, ip_address


app = create_website()

if __name__ == '__main__':
     socketio.run(app,  host = ip_address, debug=True)