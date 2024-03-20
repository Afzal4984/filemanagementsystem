import time
import sqlite3
import requests
from flask import Flask, render_template, request

app = Flask(__name__)

# Create/connect to the database
conn = sqlite3.connect('price_data.db')
c = conn.cursor()

# Create table if it doesn't exist
c.execute('''CREATE TABLE IF NOT EXISTS prices
             (product text, amazon_price real, google_price real, amazon_url text, google_url text)''')

def insert_into_db(product, amazon_price, google_price, amazon_url, google_url):
    c.execute("INSERT INTO prices VALUES (?, ?, ?, ?, ?)", (product, amazon_price, google_price, amazon_url, google_url))
    conn.commit()

def get_price_and_url(source, job_id):
    url = f"https://price-analytics.p.rapidapi.com/poll-job/{job_id}"
    headers = {
        "X-RapidAPI-Key": "b3d1423e7bmsh64ac78ee3adc8ddp10ef9djsn48535059df90",
        "X-RapidAPI-Host": "price-analytics.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers)
    result = response.json()

    try:
        price = result["results"][0]['content']['offers'][0]['price']
        url = result["results"][0]['content']['offers'][0]['url']
    except (KeyError, IndexError):
        price = None
        url = None

    return price, url

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        product = request.form['product']

        url = "https://price-analytics.p.rapidapi.com/search-by-term"

        payload = {
            "source": "google",
            "country": "in",
            "values": product
        }
        headers = {
            "content-type": "application/x-www-form-urlencoded",
            "X-RapidAPI-Key": "b3d1423e7bmsh64ac78ee3adc8ddp10ef9djsn48535059df90",
            "X-RapidAPI-Host": "price-analytics.p.rapidapi.com"
        }

        response = requests.post(url, data=payload, headers=headers)
        googleid = response.json().get('job_id', None)

        payload = {
            "source": "amazon",
            "country": "in",
            "values": product
        }

        response = requests.post(url, data=payload, headers=headers)
        amzid = response.json().get('job_id', None)

        # Wait for the jobs to complete
        time.sleep(120)

        # Get Amazon price and URL
        amazon_price, amazon_url = get_price_and_url("amazon", amzid)

        # Get Google price and URL
        google_price, google_url = get_price_and_url("google", googleid)

        # Insert data into the database
        insert_into_db(product, amazon_price, google_price, amazon_url, google_url)

        finalUrl = amazon_url if amazon_price and amazon_price < google_price else google_url

        return render_template('index.html', amazon_price=amazon_price, google_price=google_price, final_url=finalUrl, amazon_url=amazon_url, google_url=google_url)
    return render_template('index.html', amazon_price=None, google_price=None, final_url=None, amazon_url=None, google_url=None)

if __name__ == '__main__':
    app.run(debug=False)
