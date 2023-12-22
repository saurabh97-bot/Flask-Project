import requests
import lxml
from bs4 import BeautifulSoup
import pandas as pd
import datetime
import csv
import time
# from mongoengine import connect
# from pymongo import MongoClient
import pandas as pd
import asyncio
# import aiohttp
import requests
from requests.adapters import Retry,HTTPAdapter
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# import time
import requests
from requests.adapters import Retry, HTTPAdapter
from tenacity import retry, stop_after_attempt, wait_fixed
import time
import pymongo
from pymongo import MongoClient



client = MongoClient('mongodb://localhost:27017')
db = client['ScrapDB']
collection = db['scraped_data']

webdriver_path = "C:/Users/saura/Downloads/chromedriver.exe"

position_last = ''
company_last = ''
job_link_last = ''
range_s_last = ''
range_end_last = ''

# g = jobs_collection.find()
#
# for doc in g[0:1]:
#     position_last = doc['positon']
#     company_last = doc['company']
#     # company_name.append(company_last)
#     job_link_last = doc['jd_link']
#     range_s_last = doc['range_start']
#     range_end_last = doc['range_end']
#
# comp = company_collection.find()
# company_names_list = []
# for comp_data in comp:
#     company_names_list.append(comp_data["Company"])

# cdf = pd.read_csv("web3-company.csv")

# company_names_list=cdf['Company'].to_list()

session = requests.Session()
retries = Retry(total=5, backoff_factor=1, status_forcelist=[500, 502, 503, 504])
session.mount('http://', HTTPAdapter(max_retries=retries))

@retry(stop=stop_after_attempt(3), wait=wait_fixed(1))
def make_request(url):
    response = session.get(url)
    response.raise_for_status()
    return response



# for page in range(2,310):
for page in range(1, 3):
    print("\npage number : ", page)

    url = f"https://web3.career/?page={page}"

    try:
        res = make_request(url)
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        continue

    data_to_insert = []


    soup = BeautifulSoup(res.content, 'html.parser')
    v = soup.select(".my-wrapper .row-cols-2 .col .table .tbody .table_row ")

    des = []
    des_link = []

    for jjjj in v:
        link = jjjj.select_one("a")
        link_out = f"https://web3.career{link['href']}"
        des_link.append(link_out)
        # print(link_out)
        textt = jjjj.select_one("h2").text
        # print(textt)
        des.append(textt)

    # print(des)
    # print(des_link)

    print(f"\n{len(des_link)}\n")

    print(f"\n{type(des_link)}\n")

    leng = len(des_link)

    # job_list = pd.DataFrame(
    #     {'Job': des,
    #     'Job_Link': des_link,
    #     })

    # print(job_list)

    # job_list.to_csv("web3_job.csv")

    ################################################################

    nu = 0
    row = []
    for i in des_link:

        try:
            print("no :", nu)
            respp = requests.get(i)

        # async with session.get(i) as respp:

        # res =await respp.content

            soup = BeautifulSoup(respp.content, 'html.parser')
        # try:
        #     job_link.append(des_link[i])
        # except:
        #     job_link.append("")
        # try:
        #     job_name.append(des[i])
        # except:
        #     job_name.append("")
        except requests.exceptions.RequestException as e:
            print(f"Request failed for {i}: {e}")
            continue

        try:
            driver = webdriver.Chrome(executable_path=webdriver_path)
            driver.get(i)
            apply_button = driver.find_element_by_link_text("Apply Now")
            apply_button.click()
            time.sleep(6)
            driver.switch_to.window(driver.window_handles[1])
            new_url = driver.current_url
            applyyyy2 = new_url
            driver.quit()
            print("\npos", position)
        except:
            applyyyy2 = ""

        try:
            # Remove unwanted text from strings
            long_desc = long_desc.replace("Apply now:", "")
            prettified_description = prettified_description.replace("Apply now:", "")
            qualification_f = qualification_f.replace("Apply now:", "")
            response_ = response_.replace("Apply now:", "")
        except:
            pass


        # scrapped_date.append(datetime.datetime.now())

        l = soup.select("#job .mysticky ")

        k = soup.select("#job .mx-auto")

        n = soup.select("#job")

        com_link = ""
        com_name = ""
        compn_sation = ""
        loc = ""
        ben = ""
        short_desc = ""
        long_desc = ""
        prettified_description = ''
        d_ = ""
        apply = ""
        imag = ""
        taggg = ''
        comp_l = ''

        for j in l:

            # logo = j.select_one("img[src]")['src']
            # print(logo)
            try:
                comp_link = f'https://web3.career{j.select_one(".position-sticky a")["href"]}'
            except:
                comp_link = ""

            com_link = comp_link
            # print(comp_link)
            try:
                comp_name = j.select_one(".position-sticky a").text
            except:
                comp_name = ""
            com_name = comp_name

            # print(comp_name)
            try:
                compansation__ = j.select_one(".mt-4 p").text
            except:
                compansation__ = ''
            compn_sation = compansation__
            try:
                location = j.select_one(".mt-3 p").text
            except:
                location = ""
            loc = location

            ####################logo link##########################3
            # '.profile_info_container img[src]')['src']
            try:
                img = j.select_one(".rounded.align-self-baseline.mb-2.mb-md-4")['src']
            except:
                img = ''
            # print(img)
            imag = img

            ############################################3##########3

            try:
                apply_link_ = f'https://web3.career{j.select_one(".mt-4.d-flex.justify-content-center.gap-3.mb-4 a")["href"]}'
            except:
                apply_link_ = ""
            apply = apply_link_

            # print(apply_link)
            try:
                benifits = j.select_one(".text-start p").text
            except:
                benifits = ""
            ben = benifits

            # print(benifits)

        for m in k:
            try:
                desc = m.select_one(".mb-5 .fw-bold").text
            except:
                desc = ""
            short_desc = desc
            try:
                description = m.select_one(".text-dark-grey-text").text
                description2 = m.select_one(".text-dark-grey-text").text
            except:
                description = ""
            long_desc = description
            long_desc2 = description2

            try:
                description_ = m.select_one(".text-dark-grey-text")
                description2 = description_.get_text()
            except:
                description2 = ""

            prettified_description = description2

        for v in n:
            try:
                days_ = v.select_one("div.mx-auto div.mb-3 time")['datetime']
            except:
                days_ = ""
            d_ = days_

            print("\ndate..", d_)

            ####################tag###################################

            try:

                tag = v.select("div.mt-3 .my-badge.my-badge-secondary a")

                c_loc_list = ""
                for lk in tag:
                    h = lk.text.replace("\n", "")
                    c_loc_list += "," + h
                    # print(i.text)
                taggg = c_loc_list
            except:
                taggg = ''

            # print("tags",c_loc_list)

            ####################tag###################################
            ####################company loc###################################
            try:
                company_loc = v.select("div.mt-3")[-2]
                loc_ = ""
                for oo in company_loc:
                    loc_ += oo.text.replace("\n", "")
                    # print(oo.text)
                comp_l = loc_
            except:
                comp_l = ''

            # print("company_location",loc_)

            ####################company loc###################################

            # try:

            # areas=str(i.select('a span'))

            # area_of_activity.append(t)

            # print(days_)

        # company_link.extend(com_link)
        # company_name.extend(com_name)
        # compansation_.extend(compn_sation)
        # location_.extend(loc)
        # benifits_.extend(ben)
        # short_description.extend(short_desc)
        # long_description.extend(long_desc)
        # days.extend(d_)
        # apply_link.extend(apply)

        # job_name=[]  #Position
        # job_link = [] #JD Link
        # company_link = [] #Company URL
        # company_name = [] #Company
        # compansation_ = [] #Range Start , Range End , Payment Type , Currency
        # location_=[]#Location
        # benifits_=[] #Benifits
        # short_description = [] #Job Short Description
        # long_description = [] #Job Full Description
        # apply_link=[] #Apply Link
        # days =[] #Posted
        # scrapped_date =[] #Scrapping Date

        ###################################

        position = des[nu].replace('\n', "")
        if nu == len(des_link):
            nu = 0
        else:
            nu += 1

        # print(f"\n{position}\n")

        jdlink = i
        companylink = com_link
        compname = com_name.replace('\n', "")

        # print(position)
        # print(compname)
        ###########################################################33

        long_di = long_desc2
        try:
            keywords = ["Your mission", "💻 Role", "Your Impact", "Immediate Responsibilities", "Responsibilities",
                        "SPECIAL REQUIREMENTS", "Special Requirements", "Key responsibilities", "WHAT YOU WILL DO",
                        "What You Will Do", "What will you be doing", "Position Overview"]

            response_ = ''
            for yk in keywords:
                if yk in long_di:
                    r = long_di.split(yk)
                    # print(r[1])
                    response_ = "Responsibilities" + "\n\n" + r[1]
                    break
        except:
            response_ = ""

        # print(response_)
        try:
            qual = ["What we’re looking for", "👋 You", "Requirements", "Qualifications", "Who You Are",
                    "Required Experience"]

            qualification_f = ''
            for zz in qual:
                if zz in long_di:
                    q = long_di.split(zz)
                    # print(q[1])
                    qualification_f = "Qualifications" + "\n\n" + q[1]
                    break
        except:
            qualification_f = ""

        #############################about company####################################

        try:

            keywords = ["Responsibilities", "SPECIAL REQUIREMENTS", "Special Requirements", "Key responsibilities",
                        "WHAT YOU WILL DO", "What You Will Do", "What will you be doing", "Position Overview"]
            full_descr = long_desc2
            changed = False
            descc = ""
            ou = ''
            for pp in keywords:
                if pp in long_di:
                    r = long_di.split(pp)
                    pppp = full_descr.replace(r[1], "")
                    # changed=True
                    descc = pppp
                    ou = pppp
                    # print("reduced text",pppp)
                    break

            qual_ = ["Requirements", "Qualifications", "Who You Are", "Required Experience"]

            # qualification_ll=''
            out_text = ''
            for zzc in qual_:
                if zzc in descc:
                    q = descc.split(zzc)
                    out_text = ou.replace(q[1], "")
                    break




        except:
            out_text = ""

        # print("about_company..........",descc)
        # print(q[1])
        # qualification_f ="Qualifications" + "\n\n"+ q[1]
        # break

        # response_ ="Responsibilities" + "\n\n"+ r[1]
        # try:
        #     zxc = long_di.split("   ")
        #     for cdf in zxc:
        #         if compname in cdf:
        #             print("\ncompanyyyy....",cdf.split("\n\n")[0])
        # except:
        #     print("error in about company......")

        ################################################################################

        # if compname+" "+"is a " in long_di:
        #     print(compname+" "+"is a ")

        ################################################################

        #################################################################
        compansations = compn_sation.strip('\n').strip('*')

        # print(compansations)

        try:
            range = compansations.split(":")[1].strip("\n").split("-")
            start_range = range[0].replace(" ", "")[1::]
            end_range = range[1].replace(" ", "")[1::]

            currency_symbol = ["$", "€", "£", "₹", "د.ك", "د.إ"]
            currency_word = ["Dollar", "Euro", "Pound", "Rupee", "Dinar", "Dirham"]

            currency = range[0].replace(" ", "")[0]
            curr = ''
            if currency in currency_symbol:
                ind = currency_symbol.index(currency)
                curr = currency_word[ind]
            else:
                curr = currency
        except:
            start_range = ""
            end_range = ""
            curr = ""

        # print("currency",curr)
        # print("start range",start_range)
        # print("currency",end_range)
        #################################################################

        ########################################################################

        ###########################################################################

        # print("currency",curr)

        ####################################################################3
        # print(loc)
        try:
            job_locations = loc.strip('\n').split(":")[1]
        except:
            job_locations = ''

        # print("job location",job_locations)

        #######################################################################3

        ###############################################################
        benif = ben

        benifits_f = benif.split(":")
        # print(benifits_f)
        ben_z = ""
        if benifits_f:
            if benifits_f == [""]:
                # print("yess")
                pass
            else:
                ben_z = benifits_f[1]
        # print("benifits",ben_z)

        ##############################################################3

        short_d = short_desc
        applyyyy = apply

        ######################posted date####################################
        dayysss = d_

        try:

            posted__ = ""
            if "m" in dayysss and "mo" not in dayysss:
                # print("same day")
                minutes_passed = int(dayysss.split("m")[0])
                today = datetime.datetime.today()
                posted__ = today - datetime.timedelta(minutes=minutes_passed)
            elif "h" in dayysss:
                # print("same day")
                hours_passed = int(dayysss.split("h")[0])
                today = datetime.datetime.today()
                posted__ = today - datetime.timedelta(hours=hours_passed)

            elif "d" in dayysss:
                days_passed = int(dayysss.split("d")[0])
                today = datetime.datetime.today()
                # print(today)
                posted__ = today - datetime.timedelta(days=days_passed)
            elif "mo" in dayysss:
                months_passed = int(dayysss.split("mo")[0])
                days_p = months_passed * 30
                today = datetime.datetime.today()
                # print(today)
                posted__ = today - datetime.timedelta(days=days_p)
            elif "y" in dayysss:
                year_passed = int(dayysss.split("y")[0])
                days_p = year_passed * 365
                today = datetime.datetime.today()
                # print(today)
                posted__ = today - datetime.timedelta(days=days_p)
        except:
            posted__ = ''
        # print("posted date",posted__)

        ######################posted date####################################

        scr_date = datetime.date.today()

        # print("\nposition\n",position)

        # print("\ncompany\n",compname)

        # print("\nlogo link\n",imag)

        # print("\nabout company\n",descc)

        # print("\ncompany url\n",companylink)

        # print("\nJD Link\n",jdlink)

        # print("\nAbout Job\n",long_di)

        # print("\nAbout Job\n",ben_z)
        # print("\ncurrency Job\n",curr)
        # print("\nrange starts Job\n",start_range)
        # print("\nrange ends Job\n",end_range)
        # print("\ntagg Job\n",taggg[1::])
        # print("\nposted date Job\n",posted__)
        # print("\nlocation Job\n",job_locations)

        # print("\n date",d_)

        try:
            driver = webdriver.Chrome(
                executable_path="C:/Users/saura/Downloads/chromedriver.exe")

            driver.get(i)

            # locate the "Apply" button on the page and click it
            apply_button = driver.find_element_by_link_text("Apply Now")
            apply_button.click()

            # switch to the new tab that opens
            time.sleep(6)  # wait for 2 seconds to allow the new tab to open
            driver.switch_to.window(driver.window_handles[1])

            # get the URL of the new tab
            new_url = driver.current_url
            print(new_url)
            # print(new_url)
            # print(new_url)
            applyyyy2 = new_url

            driver.quit()

            print("\npos", position)
        except:
            applyyyy2 = ""

        try:
            long_desc = long_desc.replace("Apply now:", "")
            prettified_description = prettified_description.replace("Apply now:", "")
            qualification_f = qualification_f.replace("Apply now:", "")
            response_ = response_.replace("Apply now:", "")

        except:
            pass

        # roww = {"Position":[position],
        #     "Company":[compname],
        # "Logo Link":[imag],
        # "About Company":[descc],
        # "Company URL":[companylink],
        # "JD Link":[jdlink],
        # "About Job":[long_desc],
        # "Responsiblites":[response_],
        # "Qualifications":[qualification_f],
        # "Benefits":[ben_z],
        # "Payment Type":[""],
        # "Currency":[curr],
        # "Range Start":[start_range],
        # "Range End":[end_range],
        # "Apply Link":[applyyyy],
        # "Tags":[taggg[1::]],
        # "Post Date":[d_],
        # "Location":[job_locations],
        # "About Job Prettified":[prettified_description],
        # "JD Link External":[applyyyy2]
        # }

        # company_row ={
        #     "Company":[compname],
        #     "Logo Link":[imag],
        #     "Company URL":[companylink],
        #     "About Job":[long_desc],
        #     "Job Location":[job_locations]
        # }

        # if position == position_last and compname == company_last and jdlink==job_link_last and start_range==range_s_last and end_range==range_end_last:
        #     break

        # print(roww)

        # df =pd.DataFrame(roww)

        roww = {"Position": position,
                "Company": compname,
                "Logo Link": imag,
                "About Company": descc,
                "Company URL": companylink,
                "JD Link": jdlink,
                "About Job": long_desc,
                "Responsiblites": response_,
                "Qualifications": qualification_f,
                "Benefits": ben_z,
                "Payment Type": "",
                "Currency": curr,
                "Range Start": start_range,
                "Range End": end_range,
                "Apply Link": applyyyy,
                "Tags": taggg[1::],
                "Post Date": d_,
                "Location": job_locations,
                "About Job Prettified": prettified_description,
                "JD Link External": applyyyy2
                }
        collection.insert_one(roww)


        # df2 =pd.DataFrame(company_row)

        # with open('web4-jobs.csv', mode='a', newline='', encoding='utf-16') as file:
        #     writer = csv.writer(file, delimiter='\t')
        #     if page == 1:  # Add header only on the first page
        #         writer.writerow(roww.keys())
        #     writer.writerow(roww.values())
        # jobs_collection.insert_one(roww)
        # if comp_name in company_names_list:
        #
        #     pass
        # else:
        #
        #     insert_company = {
        #         "Company": compname,
        #         "Logo_Link": imag,
        #         "Company_URL": companylink,
        #         "About_Job": long_desc,
        #         "Job_Location": job_locations
        #
        #     }

            # company_collection.insert_one(insert_company)

            # company_names_list.append(compname)

        # print("company_list..", company_names_list)