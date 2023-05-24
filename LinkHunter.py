import argparse
import requests
import re
from urllib.parse import urlparse, urljoin
from bs4 import BeautifulSoup

BANNER = r"""
    __    _       __        __  __            __           
   / /   (_)___  / /__     / / / /_  ______  / /____  _____
  / /   / / __ \/ //_/    / /_/ / / / / __ \/ __/ _ \/ ___/
 / /___/ / / / / ,<      / __  / /_/ / / / / /_/  __/ /    
/_____/_/_/ /_/_/|_|____/_/ /_/\__,_/_/ /_/\__/\___/_/     
                  /_____/                              @0xPugazh
                  
"""

def robots(url, output):
    robots_url = urljoin(url, '/robots.txt')
    response = requests.get(robots_url)
    if response.status_code == 200:
        urls = re.findall(r'Disallow: (.+)', response.text)
        urls = [urljoin(url, path) for path in urls]
        with open(output, 'w') as file:
            file.write('\n'.join(urls))
            print("Extracted URLs from robots.txt saved in " + output)
    else:
        print("Failed to retrieve robots.txt from " + url)


def sitemap(url, output):
    sitemap_url = urljoin(url, '/sitemap.xml')
    response = requests.get(sitemap_url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'lxml')  # Use lxml parser
        urls = [loc.text for loc in soup.find_all('loc')]
        with open(output, 'w') as file:
            file.write('\n'.join(urls))
            print("Extracted URLs from sitemap.xml saved in " + output)
    else:
        print("Failed to retrieve sitemap.xml from " + url)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='LinkHunter - URL Extraction Tool')
    parser.add_argument('-u', '--url', help='Website URL', required=True)
    parser.add_argument('-o', '--output', help='Output file name prefix', required=True)
    parser.add_argument('-robot', '--robots', help='Extract URLs from robots.txt', action='store_true')
    parser.add_argument('-sitemap', '--sitemap', help='Extract URLs from sitemap.xml', action='store_true')
    args = parser.parse_args()

    print(BANNER)

    if args.robots:
        url_robot = args.output + "_robot.txt"
        robots(args.url, url_robot)

    if args.sitemap:
        url_sitemap = args.output + "_sitemap.txt"
        sitemap(args.url, url_sitemap)
