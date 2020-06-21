#funcs for making a map and table
import pandas as pd
def find_top_confirmed(n = 15):
    corona_df = pd.read_csv("https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/06-20-2020.csv")
    # corona_dfa_df.head(2)
    by_country = corona_df.groupby('Country_Region').sum()[['Confirmed','Deaths','Recovered']]
    cdf = by_country.nlargest(n,'Confirmed')[['Confirmed']]
    # print(cdf)
    return cdf



cdf = find_top_confirmed().to_html(classes='table table-dark text-center')

import pandas as pd
corona_df = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/06-20-2020.csv')
corona_df.head()
import folium
#!pip install folium
m = folium.Map(location = [13.052399635314941,80.25080108642578],
            tiles="Stamen Toner",
           zoom_start = 8)
folium.Circle(location = [13.052399635314941,80.25080108642578], radius = 10000, color = 'red', fill = True,
              popup = 'confirmed {}'.format(20)).add_to(m)
def circle_maker(x):
  folium.Circle(location = [x[0], x[1]],
                radius = float(x[2])*10,
                popup = '{}\nConfirmed Cases: {}'.format(x[3], x[2])).add_to(m)
corona_df[['Lat', 'Long_', 'Confirmed', 'Combined_Key']].dropna(subset = ['Lat', 'Long_']).apply(lambda x: circle_maker(x), axis = 1)

html_map = m._repr_html_()





from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html', table= cdf,areamap = html_map)

if __name__ == '__main__':
    app.run(debug=True) 