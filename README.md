# Exam Data Scraper and Downloader

This project provides tools to scrape examination data from a web source and download associated files for further analysis or storage. The tools are implemented in Python and consist of two main modules: `ExamDataScraper` and `ExamFileDownloader`.

---

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Modules](#modules)
  - [ExamDataScraper](#examdatascraper)
  - [ExamFileDownloader](#examfiledownloader)
- [Requirements](#requirements)
- [Contributing](#contributing)
- [License](#license)

---

## Features

- **Data Scraping:** Extract examination metadata (e.g., region, school, grade, term, subject, publisher, etc.) from a specified webpage.
- **File Downloading:** Download exam-related files using the scraped metadata.
- **Multi-threaded Downloads:** Accelerate file downloads with multi-threading.
- **CSV Support:** Export and read data in CSV format.

---

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/Bighsueh/EduExamFileDownloader.git
   cd EduExamFileDownloader
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

## Usage

### 1. Data Scraping

Use the `ExamDataScraper` module to scrape data from a webpage:

```python
from ExamDataScraper import ExamDataScraper

# Initialize scraper
scraper = ExamDataScraper(
    domain_url='https://exam.naer.edu.tw',
    search_page='/searchResult.php',
    page=1
)

# Get the scraped data as a DataFrame
dataframe = scraper.get_dataframe()
print(dataframe)

# Save the data to a CSV file
dataframe.to_csv('exam_data.csv', index=False)
```

### 2. File Downloading

Use the `ExamFileDownloader` module to download files based on a CSV input:

```python
from ExamFileDownloader import ExamFileDownloader

# Initialize downloader
downloader = ExamFileDownloader(
    csv_file='exam_data.csv',
    download_folder='downloaded_files',
    max_threads=10
)

# Download files
downloader.download_files()

# Save the file mapping
mapping_file = 'file_mapping.csv'
downloader.save_mapping(mapping_file=mapping_file)
```

---

## Modules

### ExamDataScraper

The `ExamDataScraper` module scrapes examination data from a specified web page.

#### Key Features:
- Extracts metadata such as region, school, grade, subject, and publisher.
- Handles pagination.

#### Example:
```python
scraper = ExamDataScraper(domain_url, search_page, page)
dataframe = scraper.get_dataframe()
dataframe.to_csv('output.csv')
```

### ExamFileDownloader

The `ExamFileDownloader` module downloads files from URLs listed in a CSV file.

#### Key Features:
- Supports multi-threaded downloads for faster performance.
- Renames files and stores them in a designated folder.
- Saves the mapping of original URLs to renamed files.

#### Example:
```python
downloader = ExamFileDownloader(csv_file, download_folder)
downloader.download_files()
downloader.save_mapping()
```

---

## Requirements

- Python 3.7+
- Required Python packages are listed in `requirements.txt`:
  - `pandas`
  - `requests`
  - `beautifulsoup4`

---

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork this repository.
2. Create a new branch for your feature or bug fix.
3. Submit a pull request with a detailed explanation of your changes.

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

