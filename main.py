from distutils.log import error
from flask import Flask, send_file , render_template
from display import plot
import pandas as pd

app = Flask(__name__)

labels = []
values = []

@app.route('/python', methods=['GET'])
def display():
    bytes_obj = plot()
    
    return send_file(bytes_obj,       
                     attachment_filename='plot.png',
                     #as_attachment=True ,
                     mimetype='image/png')



@app.route('/',methods=['GET', 'POST'])
def home():
    try:
        df  = pd.read_csv('plot.csv')

        labels = [x for x in df['labels']]
        values = [x for x in df['values']]

        print(values)
        return render_template('graph.html', labels = labels, values = values)
    except:
        raise print(error)

if __name__ == '__main__':
    app.run(debug=True)