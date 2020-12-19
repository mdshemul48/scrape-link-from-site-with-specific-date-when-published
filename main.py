from selenium import webdriver
from bs4 import BeautifulSoup
import re
import optparse


def get_argument():
    parsar = optparse.OptionParser()
    parsar.add_option("-u", "--user_id", dest="user_id", help="enter your user id like 26,23,45")
    parsar.add_option("-d", "--date", dest="date", help="Enter date and time")
    parsar.add_option("-p", "--page", dest="page", help="Enter page which you want to scan")
    options, arguments = parsar.parse_args()
    if not options.user_id:
        parsar.error("[-] Please Enter your user id correctly.")
    if not options.date:
        parsar.error("[-] Please Enter Date correctly.")
    if not options.page:
        options.page = 1
    return options


def get_html_code(user_id, page):
    chrome_default_path = r"C:\Users\mdshe\AppData\Local\Google\Chrome\User Data\Default"
    options = webdriver.ChromeOptions()
    options.add_argument(f"user-data-dir={chrome_default_path}")
    browser = webdriver.Chrome(executable_path="chromedriver.exe", options=options)
    browser.implicitly_wait(500)
    while True:
        try:
            browser.get(f"http://circleftp.net/wp-admin/edit.php?post_type=movie&author={user_id}&paged={page}")
            browser.maximize_window()
            browser.find_element_by_xpath('//*[@id="wpbody-content"]/div[3]/ul/li[2]/a/span')
            break
        except:
            browser.find_element_by_xpath('//*[@id="wpbody-content"]/div[3]/ul/li[2]/a/span')
            break
    html_code = browser.page_source
    browser.quit()
    return html_code


def get_data_from_html(html_data, date):
    html_data = BeautifulSoup(html_data, 'html.parser')
    all_post_code = html_data.find_all("tr")
    print(f"\n----------------{date}---------------")
    for post in all_post_code:
        try:
            link = BeautifulSoup(str(post.find("span", {"class": "view"})), "html.parser").find("a").get('href')
        except:
            continue
        time = re.search(r"\d\d\d\d/\d\d/\d\d",
                         BeautifulSoup(str(post.find("td", {"class": "date column-date"})), "html.parser").text)[0]
        if date == time:
            print(link)
    print(f"-------------------------------------")


options = get_argument()
html_data = get_html_code(options.user_id, options.page)
get_data_from_html(html_data, options.date)
