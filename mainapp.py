from blueapp.init_app import app

application = app

if __name__ == '__main__':
    app.run(debug=True, port=3535, host='0.0.0.0')
