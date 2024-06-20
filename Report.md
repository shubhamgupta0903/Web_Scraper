# Task Report

## Task Overview
The task assigned was to develop a solution to extract specific information from a list of 100 websites. The information to be extracted included the robots.txt URL, sitemap URL, contact email, contact address, contact number with country code, language by HTML, CMS/MVC, and category of the website. The solution was required to use web scraping techniques, store the extracted information in a MySQL database, provide clear documentation, and maintain code quality.

## Approach
### Web Scraping
I chose to use Python for web scraping due to its simplicity and the availability of libraries like Selenium and BeautifulSoup. I used these libraries to parse the HTML content of each website and extract the required information.

### Data Storage
For storing the extracted information, I utilized a MySQL database. I created a table named `website_info` with columns corresponding to the extracted information. I used the `mysql.connector` Python library to establish a connection to the database and insert the data.

### Documentation
I provided clear and concise documentation in the README file, including setup instructions and code explanations. This was done to ensure that anyone reviewing the project could easily understand and run the solution.

### Code Quality
I ensured that the code was well-organized, readable, and followed best practices. I used meaningful variable names and comments to make the code more understandable.

## Challenges
One of the main challenges I encountered was handling the different structures of websites. Not all websites followed the same HTML structure, which required me to adapt my scraping logic for each website.

Another challenge was ensuring the accuracy of the extracted information. Some websites had obfuscated or dynamically generated content, which required additional processing to extract the correct data.

## Conclusion
Overall, this task provided me with an opportunity to apply my web scraping skills and gain hands-on experience with data extraction and storage. I believe that the solution I developed meets the requirements of the task and demonstrates my ability to tackle complex tasks.

