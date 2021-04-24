
from flask import *
import pandas as pd
import numpy as np
app = Flask(__name__)

@app.route("/")
def show_tables():
    pd.set_option("expand_frame_repr", False)
    #pd.set_option('max_colwidth', None)
    df = pd.read_excel(r'sampleData.xlsx',header=1)
    df.fillna('', inplace=True)
    df.rename(columns = {'Unnamed: %d'%i : '' for i in range(1,11)}, inplace = True)
    #print(df)

    #print(clean_df)
    #data.set_index(['Name'], inplace=True)
    #data.index.name=None
    #females = data.loc[data.Gender=='f']
    #males = data.loc[data.Gender=='m']
    return render_template('view.html',tables=[df.to_html(classes='female')], #, males.to_html(classes='male')],
    titles = ['na', 'Report card'])

if __name__ == "__main__":
    app.run(debug=True, port=7000, host="0.0.0.0")


#import pandas as pd
#data = pd.read_excel('/home/govind/python/Class_11_A_Annual_Exam.xlsx', sheet_name="Sheet2", skiprows=13, nrows=32)
#print(data.head(1).to_html(classes='result'))
