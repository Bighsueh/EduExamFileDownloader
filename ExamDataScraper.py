import requests
from bs4 import BeautifulSoup
import pandas as pd

class ExamDataScraper:
    def __init__(self, domain_url, search_page, page):
        self.domain_url = domain_url
        self.url = domain_url + search_page
        self.page = page
        self.soup = None
        self.tds = None
        self.rows = []
        self.columns = ["Region", "School", "Grade", "Term", "Subject_Area", "Subject", "Exam", "Publisher", "Score", "File_1", "File_2"]
        self.df = None

    def fetch_data(self):
        payload = {
            "page": self.page,
            "orderBy": "lastest",
            "keyword": "",
            "selCountry": "",
            "selCategory": "0",
            "selTech": "0",
            "selYear": "",
            "selTerm": "",
            "selType": "",
            "selPublisher": ""
        }
        headers = {
            "Content-Type": "application/x-www-form-urlencoded",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8"
        }
        response = requests.post(self.url, data=payload, headers=headers)
        response.encoding = 'utf-8'
        self.soup = BeautifulSoup(response.text, 'html.parser')

    def parse_data(self):
        self.tds = self.soup.find_all(class_='t4')
        count = 1
        row = []
        for td in self.tds:
            if str(td) == '<td bgcolor="#FFFFFF" class="t4"></td>' and (count % 11 -1 == 0):
                continue
            if count % 11 != 0:
                row.append(td)
            if count % 11 == 0:
                row.append(td)
                self.rows.append(row)
                row = []
            count += 1

    def process_data(self):
        parsed_rows = []
        for row in self.rows:
            count = 2
            parsed_row = []
            for cell in row:
                if count % 11 >= 2:
                    parsed_row.append(cell.text)
                if count % 11 < 2:
                    cell_soup = BeautifulSoup(str(cell), "html.parser")
                    if cell_soup.find("a"):
                        parsed_row.append(self.domain_url + cell_soup.find("a")["href"])
                    else:
                        parsed_row.append(0)
                count += 1
            parsed_rows.append(parsed_row)
        self.df = pd.DataFrame(parsed_rows, columns=self.columns)

    def get_dataframe(self):
        self.fetch_data()
        self.parse_data()
        self.process_data()
        return self.df

# Example usage:
# scraper = ExamDataScraper('https://exam.naer.edu.tw', '/searchResult.php', page=4)
# df = scraper.get_dataframe()
# print(df)
