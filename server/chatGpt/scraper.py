import requests
import os
from dotenv import load_dotenv
from bs4 import BeautifulSoup
from openai import OpenAI

load_dotenv()

# Scrape HTML Content from a Page
URL = "https://www.amazon.com/All-New-release-Smart-speaker-Charcoal/dp/B09B8V1LZ3/ref=pd_ci_mcx_mh_mcx_views_0?pd_rd_w=M1hYW&content-id=amzn1.sym.352fa4e9-2aa8-47c3-b5ac-8a90ddbece20%3Aamzn1.symc.40e6a10e-cbc4-4fa5-81e3-4435ff64d03b&pf_rd_p=352fa4e9-2aa8-47c3-b5ac-8a90ddbece20&pf_rd_r=V0XCAW7K2H716Y192XC5&pd_rd_wg=P6WEm&pd_rd_r=760361b1-d515-438e-bf3d-ede82fbbfce9&pd_rd_i=B09B8V1LZ3"
page = requests.get(URL)

# print(page.text)

# Parse the HTML code with Beautiful Soup
soup = BeautifulSoup(page.content, "html.parser")

# HTML Content
html_content = soup.prettify()

# Pass the HTML content into gpt
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are an expert with product information. Tell me any information from the HTML content such as product description and price"},
        {
            "role": "user",
            "content": {html_content}
        }
    ]
)

print(client.choices[0].message)