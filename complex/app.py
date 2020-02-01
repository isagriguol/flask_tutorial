from flask import Flask, render_template

import plotly.graph_objs as go
import pandas as pd
from plotly.offline import plot
import plotly
import json
import numpy as np

class NpEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.integer):
            return int(obj)
        elif isinstance(obj, np.floating):
            return float(obj)
        elif isinstance(obj, np.ndarray):
            return obj.tolist()
        else:
            return super(NpEncoder, self).default(obj)

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, World!'

@app.route('/graph')
def graph():
    df = pd.read_csv('Advertising.csv', index_col=0)
    df.sort_values(['Sales'], inplace=True)
    fig = go.Figure()
    for cname in df.columns[:-1]:
        fig.add_scatter(x=df[cname], y=df['Sales'], name=cname, mode="markers")

    fig.update_layout(width=1600, height=800)
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return render_template('graph.html',
                           ids='invest',
                           graphJSON=graphJSON)


@app.route('/table')
def table():
    df = pd.read_csv('Advertising.csv', index_col=0)

    #meas = [dffinal.iloc[i].to_dict() for i in range(dffinal.shape[0])]
    meas = [list(map(str, df.iloc[i].values)) for i in range(df.shape[0])]
    #meas = {'data': meas}
    ddffinal = json.dumps(meas, cls=NpEncoder)
    return render_template('table.html',
                           dffinal=ddffinal)



if __name__ == '__main__':
    #app.run(debug=True)
    app.run()
