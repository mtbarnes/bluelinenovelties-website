from blueapp.init_app import app, manager

application = app

if __name__ == '__main__':
    manager.run()
    # app.run(debug=True, port=3535, host='0.0.0.0')
