# LinkHunter
Extract urls from robots.txt and sitemap.xml files


## Installation
```
git clone https://github.com/0xPugazh/LinkHunter.git
cd LinkHunter/
pip3 install -r requirements.txt
```

## Usage
```
python3 LinkHunter.py -u https://www.google.com -o google -robot -sitemap``
```

## Help
```
    __    _       __        __  __            __           
   / /   (_)___  / /__     / / / /_  ______  / /____  _____
  / /   / / __ \/ //_/    / /_/ / / / / __ \/ __/ _ \/ ___/
 / /___/ / / / / ,<      / __  / /_/ / / / / /_/  __/ /    
/_____/_/_/ /_/_/|_|____/_/ /_/\__,_/_/ /_/\__/\___/_/     
                  /_____/                              @0xPugazh
        
          LinkHunter - URL Extraction Tool

options:
  -h, --help            Show this help message and exit
  -u URL, --url URL     Website URL
  -o OUTPUT, --output OUTPUT
                        Output file name prefix
  -robot, --robots      Extract URLs from robots.txt
  -sitemap, --sitemap   Extract URLs from sitemap.xml
```

## Support Me
<a href="https://www.buymeacoffee.com/0xPugazh" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/default-orange.png" alt="Buy Me A Coffee" height="41" width="174"></a>
