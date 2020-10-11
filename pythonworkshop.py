from bs4 import BeautifulSoup
from flask import Flask, jsonify, abort
import requests


app = Flask(__name__, static_folder='.', static_url_path='', template_folder='')
app.config['SESSION_TYPE'] = 'filesystem'

...
# homepage
@app.route('/', methods=['GET'])
def root():
    return "Welcome to the UCF Parking API. "
...
# run application
def main():
    app.run(debug=False, port='5000', host='0.0.0.0')


# returns formatted data for garage_name for API
@app.route('/garage/<garage_name>', methods=['GET'])
def get_parking_info(garage_name):
    parking_data = scrape_parking_data()

    if garage_name in parking_data:
        output = parking_data[garage_name]

        return jsonify(output)
    else:
        abort(404)


# scrape parking data from UCF site
def scrape_parking_data():
    url = 'https://secure.parking.ucf.edu/GarageCount/iframe.aspx'

    # fetch HTML like a browser
    html = requests.get(url).content
    # html.parser is the built-in tool to parse HTML
    soup = BeautifulSoup(html, 'html.parser')

    # find html table
    table = soup.find('table')

    # pick out only table rows containing data
    rows = table.find_all('tr', {'class': 'dxgvDataRow_DevEx'})

    availability = {}
    for r in rows:       
        cols = r.find_all('td')
        name = cols[0].text
        spaces_data = cols[1].text.strip()
        free_spaces = spaces_data.split('/')[0]
        total_spaces = spaces_data.split('/')[1]
       
        availability[name] = {
            'free_spaces': int(free_spaces),
            'total_spaces': int(total_spaces),
            'percent_full': 1-(float(free_spaces) / float(total_spaces))
         }

    return availability



if __name__ == '__main__':
   main()
