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
        return render_template('bedroom.html')
        if request.method == 'POST':
            bedroom_decision = request.form['Choice']
            image=None

            if Choice == 1:
                ⠀⠀⠀image="""⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⡟⠫⣉⠉⠉⡩⠋⢹⡇⠛⠉⠉⠉⠉⠉⠉⠉⠙⠛⢻⢶⠒⠛⠛⠛⣻⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⡇⠀⠘⡦⠊⠀⠀⢸⡧⠀⠠⠤⠄⠀⠤⠀⠤⠄⠤⢼⠀⠣⡀⠀⡐⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⡇⠀⠀⡇⠀⠀⠀⠸⡃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⠈⡞⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣧⠀⠀⡁⠀⠀⠀⢸⣇⣀⣀⣀⣐⣉⣐⣀⡔⠲⡤⢼⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠞⡟⠿⢻⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣿⠀⠀⠆⠀⠀⠀⠈⡇⠀⠀⡀⢀⡘⢄⠘⡡⠴⠁⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠋⠠⠀⡆⡌⣷⡄⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣿⠀⠀⠅⠀⠀⠀⢸⡇⣐⣀⠢⣠⠤⣄⡁⢄⢀⣀⢸⠀⠀⠀⢀⠀⠀⡄⠀⠀⠉⠉⡟⠉⠉⠙⢿⡋⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣿⠀⠀⠇⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠉⠉⠁⠐⢺⠀⠀⠀⢸⠀⠀⡀⠀⠀⠀⠈⣇⣀⢀⣀⣸⣃⣀⣀⣀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣿⠀⠀⡇⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀⢸⠀⠀⣿⠉⠉⠉⠉⠉⠉⠉⠉⠀⠀⠁⠈⠉⠉⠱⡄⠀⠀
⠀⠀⠀⠀⠀⡏⠀⠀⠃⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀⢸⠀⠀⣿⠀⠒⠒⠒⠂⠀⠀⠀⠀⠀⠀⠀⠐⠂⠀⡇⠀⠀
⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠘⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀⠀⠀⣿⠀⠐⠂⠀⠀⠀⠀⡀⡀⠀⠐⠂⠀⠀⠀⠁⠀⠀
⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠈⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀⠀⠀⡏⠀⠀⠀⠀⠀⠀⠀⠀⠤⠀⠀⠀⠀⠂⠀⡀⠀⠀
⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⢠⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠠⠀⠀⠀⠀⠀⠰⠀⠂⠀⠀⠀⠀⠀⠀⠀⠐⠐⠒⠀⠀⠀⡇⠀⠀
⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠀⠀⠀⠀⠀⠀⠀⠀⠂⠀⠀⠀⡇⠀⠀
⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠠⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠀⠀⡇⠀⠀
⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⡆⠀⠀⠀⡄⠀⢠⠠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⠁⠀⠀
⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⡆⠀⢸⠀⠀⠠⠀⠀⠀⠀⠀⠀⠀⠀⠠⠀⠁⠸⠀⠀⠀
⠀⠀⠀⠀⠀⡇⠀⠀⢀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⡇⠀⢸⠀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⠇⢀⠀⠀⠀
⠀⠀⠀⠀⠨⡇⠀⠀⢸⠀⠀⠀⠀⣰⠄⠀⠀⠀⠄⠠⢀⠀⠀⢠⠤⣧⠀⠀⠀⡃⠀⢸⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠄⠤⡀⢸⠀⠀⠀
⠀⠀⠀⠀⠀⣿⠀⠀⢸⠀⠀⠀⠀⡯⡀⢠⠁⠀⠀⣂⠀⠀⠀⠀⠈⢸⠀⠀⠀⠀⠀⢸⠀⠀⠀⠄⠀⠀⠀⠀⠀⠀⠀⠠⠀⡇⢸⠀⠀⠀
⠀⠀⠀⠀⠀⣿⠀⠀⠀⡄⠀⠀⠀⡇⠄⠀⠉⢁⠀⠀⠀⠐⠀⠀⠄⢺⠀⠀⠀⠀⠀⢸⠀⢀⣀⡀⣀⣀⠀⡀⠀⠀⠀⠀⣀⡆⢸⠀⠀⠀
⠀⠀⠀⠀⠀⠉⠷⣤⣀⡇⠀⣠⠔⠃⠀⠰⢂⠀⠀⠘⠏⠉⢈⠐⢣⡛⣦⡀⠀⠀⠀⣸⡀⠀⠀⠀⠀⠀⠀⠀⣀⣁⣀⣀⣀⣀⣸⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠂⠁⠙⠷⠚⠑⡉⠀⠈⠀⠀⠀⠈⠀⠀⠁⠀⠀⠐⠀⠀⠉⢦⡦⠌⠀⠈⠉⠉⠉⠉⠍⡉⡍⠁⡉⠬⡈⠉⠉⠁⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠀⠀⠀⠁⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀

            You made a good choice and avoided the killer this time.
            Lets hope next time you are just as lucky.
            """
            return render_template('bedroom.html', image=image)
            elif Choice == "2":
                """
                Bad choice looks like the killer saw your feet under the bed
                """
                return render_template('death.html, Choice=Choice')
            elif choice == "3":
                """
                Bad choice looks like the killer cut
                the line and now cut your throat.
                """
                return render_template('death.html, Choice=Choice')





    @app.route('/bathroom', methods=('GET', 'POST'))
    def bathroom():
        return render_template('bathroom.html')


    @app.route('/kitchen')
    def kitchen():
        return render_template('kitchen.html')

    @app.route('/office')
    def office():
        return render_template('office.html')

    @app.route('/livingroom')
    def livingroom():
        return render_template('livingroom.html')

    @app.route('/basement')
    def basement():
        return render_template('basement.html')

    @app.route('/win')
    def win():
        return render_template('win.html')

    @app.route('/death')
    def death():
        return render_template('death.html')


    return app
