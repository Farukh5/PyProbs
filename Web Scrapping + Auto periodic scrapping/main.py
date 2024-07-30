import requests
from bs4 import BeautifulSoup
import sqlite3
import pandas as pd
import schedule
import time
from selenium import webdriver

# Database setup
def setup_db():
    conn = sqlite3.connect('scraper.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS data (title TEXT, link TEXT)''')
    conn.commit()
    return conn, c

def save_to_db(conn, data):
    c = conn.cursor()
    c.executemany('INSERT INTO data (title, link) VALUES (?, ?)', data)
    conn.commit()

def export_to_csv():
    conn, c = setup_db()
    df = pd.read_sql_query('SELECT * FROM data', conn)
    df.to_csv('scraped_data.csv', index=False)
    conn.close()

# Function to scrape data
def fetch_data(url, use_selenium=False):
    if use_selenium:
        driver = webdriver.Chrome()  # Update path if necessary
        driver.get(url)
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        driver.quit()
    else:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

    items = soup.find_all('a', href=True)
    data = [(item.get_text(), item['href']) for item in items]
    return data

def scrape(use_selenium=False):
    url = 'http://example.com'  # Replace with your target URL
    data = fetch_data(url, use_selenium)
    conn, _ = setup_db()
    save_to_db(conn, data)
    conn.close()
    print(f"Scraped {len(data)} items")

# Scheduling the scraper
def job():
    print("Starting scrape...")
    scrape(use_selenium=False)
    print("Scraping complete")

schedule.every(1).hour.do(job)

if __name__ == "__main__":
    while True:
        schedule.run_pending()
        time.sleep(1)
