import re
from database import create_connection, execute_query
from web_scraper import get_robots_url, get_sitemap_url, get_contact_info, get_language, get_cms_mvc, get_category, close_driver



def validate_url(url):

    # Validate the given URL using a regular expression.
    regex = re.compile(
        r'^(?:http|ftp)s?://'  # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'  # domain...
        r'localhost|'  # localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}|'  # ...or ipv4
        r'\[?[A-F0-9]*:[A-F0-9:]+\]?)'  # ...or ipv6
        r'(?::\d+)?'  # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    return re.match(regex, url) is not None



def main():
    
    # Main function to read websites from a file, validate them, scrape information, and insert data into the database.
    
    # Create database connection
    connection = create_connection()
    if connection is None:
        print("Failed to create database connection.")
        return

    try:
        # Read websites from the file
        with open("websites.txt", "r") as file:
            websites = [line.strip().replace('"', '') for line in file.readlines()]

        for website in websites:
            if not validate_url(website):
                print(f"Invalid URL: {website}")
                continue
            
            # Scrape information from the website
            robots_url = get_robots_url(website)
            sitemap_url = get_sitemap_url(website)
            contact_email, contact_address, contact_number = get_contact_info(website)
            language = get_language(website)
            cms, mvc = get_cms_mvc(website)
            category = get_category(website)
            
            # Insert data into the database
            insert_web_query = """
                INSERT INTO website_info 
                (website_url, robots_url, sitemap_url, contact_email, contact_address, contact_number, language, cms, mvc, category)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            data = (website, robots_url, sitemap_url, contact_email, contact_address, contact_number, language, cms, mvc, category)
            
            execute_query(connection, insert_web_query, data)
            print(f"Data inserted for {website}")

    finally:
        # Close the database connection
        if connection and connection.is_connected():
            connection.close()
            print("MySQL connection is closed")
        
        # Close the web driver
        close_driver()



if __name__ == "__main__":
    main()
