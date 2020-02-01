import os
from flask import Flask, flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import time

UPLOAD_FOLDER = 'static/uploads'
ALLOWED_EXTENSIONS = {'txt', 'tsv'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def heatmap(df, scale=True):
    if scale:
        df = (df-df.mean())/df.std()

    #metric="canberra"
    cg = sns.clustermap(df,  method="ward",
                        cmap="Blues")
    ax = cg.ax_heatmap
    plotfile = os.path.join('static', str(time.time()) + '.png')
    plt.savefig(plotfile)
    plt.close()
    return plotfile


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            df = pd.read_csv(request.files.get('file'), sep='\t', index_col=0)
            # If you want to save the file 
            #filename = secure_filename(file.filename)
            #file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            #return redirect(url_for('uploaded_file',
            #                        filename=filename))
            result = heatmap(df)
            return render_template('view.html',
                                   result=result)
    else:
        result = None

    return render_template('view.html',
                           result=result)

if __name__ == '__main__':
    app.run(debug=True)
