from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import re
import requests
from selenium_setup import get_driver

# Initialize the WebDriver
driver=get_driver()


def get_robots_url(website_url):
    # Get the robots.txt URL for the given website.
    robots_url = website_url.rstrip('/') + '/robots.txt'
    try:
        response = requests.head(robots_url)
        if response.status_code == 200:
            return robots_url
        else:
            return None
    except requests.RequestException as e:
        print(f"Error checking robots.txt for {website_url}: {e}")
        return None



def get_sitemap_url(website_url):
    # Get the sitemap URL from the robots.txt file of the given website.
    try:
        driver.get(website_url + "/robots.txt")
        robots_txt = driver.page_source
        sitemap_urls = re.findall(r'Sitemap: (.*)', robots_txt)
        if sitemap_urls:
            return sitemap_urls[0]
        else:
            return None
    except Exception as e:
        print(f"Error extracting sitemap URL for {website_url}: {e}")
        return None



def is_valid_address(address):
    # Verify if an address is valid based on common keywords.
    keywords = ['street', 'st.', 'road', 'rd.', 'avenue', 'ave.', 'boulevard', 'blvd.', 'lane', 'ln.', 'town', 'village', 'city', 'state', 'zip', 'postal', 'country']
    return any(keyword in address.lower() for keyword in keywords)

def get_contact_info(website_url):
    # Extract contact information (email, address, phone number) from the website.
    contact_email = None
    contact_address = None
    contact_number = None
    
    try:
        driver.get(website_url)
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        
        # Extract all links from the main page
        links = [a_tag['href'] for a_tag in soup.find_all('a', href=True)]

        # Filter links to include only those related to 'Contact' and 'About' pages
        filtered_links = [link for link in links if 'contact' in link.lower() or 'about' in link.lower()]

        unique_emails = set()
        unique_numbers = set()
        unique_addresses = set()

        # Extract email addresses, contact numbers, and contact addresses from the filtered links
        for link in filtered_links + [website_url]:  # Include main page URL in the search
            driver.get(link)
            soup = BeautifulSoup(driver.page_source, 'html.parser')
            
            # Extract email addresses
            email_list = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', str(soup))
            unique_emails.update(email_list)
            
            # Extract phone numbers
            phone_list = re.findall(r'\+\d{1,3}\s?[-.\s]?\(?\d{1,4}\)?[-.\s]?\d{1,4}[-.\s]?\d{1,9}', str(soup))
            unique_numbers.update([''.join(phone) for phone in phone_list])

            # Extract addresses
            address_list = re.findall(r'\d{1,4}\s\w+\s\w+\s\w+,\s\w+\s\w+\s\d{5}(?:-\d{4})?', str(soup))
            for address in address_list:
                if is_valid_address(address):
                    unique_addresses.add(address)

        # Filter out unwanted email addresses
        final_emails = [email for email in unique_emails if '.com' in email or '.in' in email or 'info' in email or 'org' in email]

        # Verify contact addresses
        verified_addresses = [address for address in unique_addresses if is_valid_address(address)]
        
        # Select the first email, phone number, and address if available
        contact_email = final_emails[0] if final_emails else None
        contact_number = list(unique_numbers)[0] if unique_numbers else None
        contact_address = verified_addresses[0] if verified_addresses else None

    except Exception as e:
        print(f"Error extracting contact info for {website_url}: {e}")
    
    return contact_email, contact_address, contact_number



def get_language(url):
    #Get the language of the website.
    try:
        driver.get(url)
        lang = driver.find_element(By.XPATH, '//html').get_attribute('lang')
        return lang if lang else 'Not specified'
    except Exception as e:
        print(f"Error extracting language for {url}: {e}")
        return 'Not specified'



def get_cms_mvc(url):
    #Get the CMS and MVC framework used by the website.
    driver.get(url)
    page_source = driver.page_source.lower()
    
    cms = None
    mvc = None

    # Check for CMS indicators
    if re.search(r'wp-content|wordpress', page_source):
        cms = 'WordPress'
    elif re.search(r'joomla', page_source):
        cms = 'Joomla'
    elif re.search(r'drupal', page_source):
        cms = 'Drupal'
    elif re.search(r'magento', page_source):
        cms = 'Magento'
    
    # Check for MVC indicators
    if re.search(r'rails', page_source):
        mvc = 'Ruby on Rails'
    elif re.search(r'django', page_source):
        mvc = 'Django'
    elif re.search(r'asp.net', page_source):
        mvc = 'ASP.NET MVC'
    elif re.search(r'laravel', page_source):
        mvc = 'Laravel'
    
    return cms, mvc



def get_category(url):
    #Categorize the website based on its content.
    
    categories = {
        'technology': ['tech', 'software', 'hardware','technology'],
        'education': ['edu', 'school', 'university','institute'],
        'health': ['health', 'hospital', 'clinic','medical'],
        'ecommerce': ['shop', 'store', 'buy'],
        'news': ['news', 'headline', 'breaking', 'article'],
        'entertainment': ['entertainment', 'movies', 'music', 'celebrity'],
        'sports': ['sports', 'football', 'basketball', 'cricket'],
        'travel': ['travel', 'tourism', 'destination', 'hotel'],
        'food': ['food', 'recipe', 'restaurant', 'cuisine'],
        'fashion': ['fashion', 'style', 'clothing', 'apparel'],
        'finance': ['finance', 'money', 'investment', 'banking'],
        'government': ['government', 'official', 'public service'],
        'socialmedia': ['social', 'media', 'facebook', 'twitter', 'instagram'],
        'technology': ['technology', 'gadget', 'innovation', 'digital']
    }

    category = 'Other'
    driver.get(url)
    for cat, keywords in categories.items():
        for keyword in keywords:
            if keyword in driver.page_source.lower():
                category = cat
                break

    return category

def close_driver():
    # Close the Selenium WebDriver.
    driver.quit()
