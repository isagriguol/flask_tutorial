from flask import Flask, flash, redirect, render_template, request, url_for
app = Flask(__name__)
app.secret_key = 'secretkey'

@app.route('/')
def index():
    return 'Página inicial'

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None

    if request.method == 'POST':
        flash('You were successfully logged in')
        return redirect(url_for('index'))
        #return redirect(url_for('success'))
    return render_template('flash_login.html', error=error)

#@app.route('/success')
#def success(username):
#    return 'welcome %s' % username

if __name__ == "__main__":
    app.run(debug=True)