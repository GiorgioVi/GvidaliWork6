from flask import Flask, render_template, request

my_app = Flask(__name__)

@my_app.route('/')
def root():
    if request.args:
        user = request.args['user']
        method = request.method
        return render_template('greetings.html', user = user, method = method)
    else:
        return render_template('form.html')

if __name__ == '__main__':
    my_app.debug = True
    my_app.run()
