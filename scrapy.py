import requests
from bs4 import BeautifulSoup
import pandas as pd
import time


company_links = []
logos = []
headings = []
descriptions = []
categories = []


for page in range(1,5):
    time.sleep(0.01)
    url = f"https://edgein.io/companies/?page={page}"
    res = requests.get(url)
    soup = BeautifulSoup(res.content,"html.parser")

    companies = soup.select_one('body > div:nth-of-type(1) > div > main > div > div:nth-of-type(2) > div > div:nth-of-type(2) > div:nth-of-type(2)').text
    # print("COMPANIES>=================",''.join(companies))

    logo_element = soup.select_one(
        'html > body > div:nth-child(1) > div > main > div > div:nth-child(2) > div > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div > div:nth-child(1) > a > div:nth-child(1) > div > img')

    if logo_element:
        logo_src = logo_element['src']
        print("LOGO>=======================",logo_src)
    else:
        print('Logo element not found')


    heading = soup.select_one('body > div:nth-child(1) > div > main > div > div:nth-child(2) > div > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div > div:nth-child(1) > a > div:nth-child(1) > h3').text
    # print("HEADING>==================: ",heading)

    description = soup.select_one('body > div:nth-child(1) > div > main > div > div:nth-child(2) > div > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div > div:nth-child(1) > a > div:nth-child(3)').text
    # print("DESCRIPTION==============",description)


    href_value = soup.select_one('html > body > div:nth-child(1) > div > main > div > div:nth-child(2) > div > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div > div:nth-child(1) > a > div:nth-child(1)').text
    comp_links = f"https://edgein.io/{href_value}"

    # print("LINKS=======================",comp_links)

    company_links.append(comp_links)
    logos.append(logo_src)
    headings.append(heading)
    descriptions.append(description)


    print("=========LINKS========",company_links)
    print("=========LOGOS========", logos)
    print("=========HEADINGS========", headings)
    print("=========DESCRIPTION========", descriptions)








    #     # Extract category tags
    #     tags = company.select(".grow .mt-4 .shrink-0")
    #     category = ",".join(tag.text for tag in tags)
    #
    #     # Append data to lists
    #     company_links.append(comp_links)
    #     logos.append(logo)
    #     headings.append(heading)
    #     descriptions.append(description)
    #     categories.append(category)
    #
    #     # Create a DataFrame from the lists
    #     data = {
    #         "company link": company_links,
    #         "logo": logos,
    #         "heading": headings,
    #         "description": descriptions,
    #         "category": categories
    #     }
    #
    #     df = pd.DataFrame(data)
    #
    #     # Write DataFrame to CSV file
    #     df.to_csv('edgin.csv', index=False, encoding="utf-16")
