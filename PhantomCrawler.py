import requests
from bs4 import BeautifulSoup

# Function to read proxy IPs from a file
def read_proxy_list(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file]

# Get user input for website URL
website_url = input("Enter the website URL: ") #https://spyboy.blog

# Get user input for the proxy list file
proxy_file_path = input("Enter the path to the proxy list file: ") #valid_proxy.txt

# Read proxy list from the specified file
proxies = read_proxy_list(proxy_file_path)

for proxy_info in proxies:
    # Split the proxy information into IP and port
    proxy_ip, proxy_port = proxy_info.split(":")

    # Set up the proxy
    proxy = f"http://{proxy_ip}:{proxy_port}"
    proxies = {"http": proxy, "https": proxy}

    try:
        # Make a request using the proxy
        response = requests.get(website_url, proxies=proxies)

        # Parse HTML content using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract all links from the page
        links = [link.get('href') for link in soup.find_all('a') if link.get('href')]

        # Visit each link
        for link in links:
            absolute_link = requests.compat.urljoin(website_url, link)
            requests.get(absolute_link, proxies=proxies)
            print(f"Proxy {proxy} - Visiting: {absolute_link}")

    except requests.RequestException as e:
        print(f"Error with proxy {proxy}: {e}")
