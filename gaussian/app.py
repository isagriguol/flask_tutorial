from flask import Flask, render_template, request

import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats
import time
import os

def gaussian(mu, sigma):
    mu = float(mu)
    sigma = float(sigma)
    x = np.linspace(mu - 3*sigma, mu + 3*sigma, 100)
    plt.plot(x, stats.norm.pdf(x, mu, sigma))
    plt.title('mu=%g, sigma=%g' % (mu, sigma))
    plotfile = os.path.join('static', str(time.time()) + '.png')
    plt.savefig(plotfile)
    # What happens if you comment the line 
    # below and run the app
    plt.close()
    return plotfile

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, World!'

@app.route('/graph', methods=['GET', 'POST'])
def graph():
    if request.method == 'POST':
        result = gaussian(request.form['mu'],
                          request.form['sigma'])
    else:
        result = None

    return render_template('view.html',
                           result=result)

if __name__ == '__main__':
    app.run(debug=True)
