# PhantomCrawler
PhantomCrawler lightweight Python tool designed for Proof of Concept (POC) testing, allowing users to simulate website interactions through different proxy IP addresses. It leverages Python, requests, and BeautifulSoup to offer a simple and effective way to test website behaviour under varied proxy configurations.

**Features:**
- Utilizes a list of proxy IP addresses from a specified file.
- Supports both HTTP and HTTPS proxies.
- Allows users to input the target website URL, proxy file path, and a static port.
- Makes HTTP requests to the specified website using each proxy.
- Parses HTML content to extract and visit links on the webpage.
- Logs proxy information, HTTP status codes, and errors for analysis.

**Usage:**
ProxyVoyage is a versatile tool with various applications, including:
- **POC Testing:** Simulate website interactions to assess functionality under different proxy setups.
- **Web Traffic Increase:** Boost website hits by generating requests from multiple proxy IPs.
- **Proxy Rotation Testing:** Evaluate the effectiveness of rotating proxy IPs.
- **Web Scraping Testing:** Assess web scraping tasks under different proxy configurations.
- **DDoS Awareness:** Caution: The tool has the potential for misuse as a DDoS tool. Ensure responsible and ethical use.

**How to Use:**
1. Clone the repository: `git clone https://github.com/yourusername/ProxyVoyage.git`
2. Install dependencies: `pip install -r requirements.txt`
3. Run the script: `python proxies.py`

**Disclaimer:**
ProxyVoyage is intended for educational and testing purposes only. Users are cautioned against any misuse, including potential DDoS activities. Always ensure compliance with the terms of service of websites being tested and adhere to ethical standards.
