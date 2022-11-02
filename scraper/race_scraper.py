"""
This will contain all the logic to scrape race data from the web.
"""

from scraper.web_driver import start_driver, stop_driver

class RaceScraper:
    """
    This class will contain all the logic to scrape race data.
    """

    def __init__(self, data: tuple):
        """
        This is the constructor for the race scraper.
        """
        self.data = data

    def general_scrape(self, link: str):
        """
        This will scrape season race summary pages.
        """
        print("Starting general scrape...")
        print("RaceScraper started...")
        print("Link: " + link)
        print()

        headers = []
        data_array = []

        # Get the content from the link.
        driver, soup = start_driver(link)

        for table in soup.findAll('table', attrs={'class':'resultsarchive-table'}):
            table_head = table.find('thead')
            table_headers = table_head.find_all('th')

            table_body = table.find('tbody')
            table_rows = table_body.find_all('tr')
        
        for header in table_headers:
            if header.text.strip() != "":
                headers.append(header.text)

        for row in table_rows:
            row_data = []
            table_data = row.find_all('td')
            for data_entry in table_data:
                data_span = data_entry.find_all('span')

                if len(data_span) == 3:
                    data_entry = f"{data_span[0].text} {data_span[1].text}"
                else:
                    data_entry = data_entry.text.strip()
                    data_entry = data_entry.replace("\n", "")
                    
                if data_entry != "":
                    row_data.append(data_entry)

            data_array.append(row_data)

        stop_driver(driver)
