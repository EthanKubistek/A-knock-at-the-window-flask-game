from flask import Flask, render_template, request, redirect, url_for
from textwrap import dedent
def create_app(test_config=None):
    app = Flask(__name__)
    app.config.from_mapping(
        SECRET_KEY='dev'
    )

    if test_config is None:
        #load the instance of config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    @app.route('/')
    def start():
        return render_template('intro.html')

    @app.route('/intro')
    def intro():
        return render_template('intro.html')

    @app.route('/bedroom', methods=('GET', 'POST'))
    def bedroom():

        if request.method == 'POST':
            choice = request.form['bedroom_decision']

            if choice == "1":
                return render_template('bedroom_transition.html')
            elif choice == "2":

                  return render_template('death.html')
            elif choice == "3":

                  return render_template('death.html')
        return render_template('bedroom.html')







    @app.route('/bathroom', methods=('GET', 'POST'))
    def bathroom():
        if request.method == 'POST':
            choice = request.form['bathroom_decision']
            if choice == "1":
                return render_template('bathroom_transition.html')
            elif choice == "2":

                  return render_template('death.html')
            elif choice == "3":

                  return render_template('death.html')
        return render_template('bathroom.html')


    @app.route('/kitchen', methods=('GET', 'POST'))
    def kitchen():
        if request.method == 'POST':
            choice = request.form['kitchen_decision']
            if choice == "1":
                return render_template('death.html')
            elif choice == "2":
                  return render_template('death.html')
            elif choice == "3":
                return render_template('kitchen_transition.html')
        return render_template('kitchen.html')

    @app.route('/office', methods=('GET', 'POST'))
    def office():
        if request.method == 'POST':
            choice = request.form['office_decision']
            if choice == "1":
                return render_template('death.html')
            elif choice == "2":
              return render_template('death.html')
            elif choice == "3":
              return render_template('office_transition.html')
        return render_template('office.html')

    @app.route('/livingroom', methods=('GET', 'POST'))
    def livingroom():
        if request.method == 'POST':
            choice = request.form['livingroom_decision']
            if choice == "1":
                return render_template('death.html')
            elif choice == "2":
              return render_template('death.html')
            elif choice == "3":
              return render_template('livingroom_transition.html')
        return render_template('livingroom.html')

    @app.route('/basement', methods=('GET', 'POST'))
    def basement():
        if request.method == 'POST':
            choice = request.form['basement_decision']
            if choice == "1":
                return render_template('death.html')
            elif choice == "2":
              return render_template('death.html')
            elif choice == "3":
              return render_template('win.html')
        return render_template('basement.html')

    @app.route('/win')
    def win():
        return render_template('win.html')

    @app.route('/death')
    def death():
        return render_template('death.html')


    return app
