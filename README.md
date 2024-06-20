
# Website Information Extraction

This project automates the extraction of information from websites using Selenium and stores it in a MySQL database.

## Setup

### 1. Clone the repository to your local machine

```bash
git clone https://github.com/shubhamgupta0903/Web_Scraper
```

### 2. Install the required Python packages

```bash
pip install -r requirements.txt
```
or
```bash
pip3 install -r requirements.txt
```

### 3. Database Setup

```bash
mysql -u root -p < sql/create_table.sql
```

Note: Make sure you have MySQL installed on your machine.

### 4. Database Connection

Update the MySQL connection details in `database.py`

```python
connection = mysql.connector.connect(
        host='your_host',              # Change 'your_host' to your database host, e.g., '127.0.0.1'
        port='your_port',              # Change 'your_port' to your database port, e.g., 3306
        user='your_username',          # Change 'your_username' to your database username
        password='your_password',      # Change 'your_password' to your database password
        database='internship_project'  # Don't change database name
    )
```

### 5. Chromedriver setup

Users should download the ChromeDriver executable compatible with their operating system from the [official ChromeDriver website](https://chromedriver.chromium.org/downloads) or if they are using Chrome version 115 or newer(https://googlechromelabs.github.io/chrome-for-testing/).

Extract the ChromeDriver and copy the path to the chromedriver executable.

Update the path to the chromedriver executable in `main.py`

```python
service = Service('/path/to/chromedriver')
```

### 6. Run the main file

```bash
python main.py
```
or
```bash
python3 main.py
```

## Note:

- Ensure that your MySQL server is running before executing the code.
- Make sure to review and comply with the website's terms of service and legal requirements when extracting information.

