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
