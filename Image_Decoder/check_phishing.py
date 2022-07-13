import os
import pandas as pd 
import requests
import json
import base64


headers = {
        'format': 'json',
        'app_key': 'https://data.phishtank.com/data/8bf7ccdbfb3eb4ad75996fe1d616efc4406f321cba361844b88402f3ee01c8cd/online-valid.csv',
        }

def get_url_with_ip(URI):
    """Returns url with added URI for request"""
    url = "http://checkurl.phishtank.com/checkurl/"
    new_check_bytes = URI.encode()
    base64_bytes = base64.b64encode(new_check_bytes)
    base64_new_check = base64_bytes.decode('ascii')
    url += base64_new_check
    return url

def send_the_request_to_phish_tank(url, headers):
    """This function sends a request."""
    response = requests.request("POST", url=url, headers=headers)
    return response

start_urls = []
input_urls_directory = os.path.abspath("/home/server/QRcode_Crawler/Image_Crawler/Imagecapture/spiders/test_record.csv")
# Read a URL file
df = pd.read_csv(input_urls_directory, usecols = ["image_urls"], encoding= 'unicode_escape')
start_urls = df["image_urls"].tolist()
for url in start_urls:
    #new_check = 'https://gfdsc.3wz0b62.cn'
    new_check = url
    url = get_url_with_ip(new_check)
    r = send_the_request_to_phish_tank(url, headers)
    print(r.text)
