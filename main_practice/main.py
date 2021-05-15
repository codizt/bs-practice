from bs4 import BeautifulSoup
import requests
import time

print("Put some skill you are unfamiliar with: ")
unfamiliar_skill = input('>')
print(f"Filtering out {unfamiliar_skill}")


def find_jobs():
    html_text = requests.get(
        'https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text
    soup = BeautifulSoup(html_text, 'lxml')
    jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')

    for index, job in enumerate(jobs):
        published_date = job.find('span', class_="sim-posted").text
        if 'few' in published_date:
            skills = job.find(
                'span', class_="srp-skills").text.replace(" ", '')
            if unfamiliar_skill not in skills.split(','):
                company_name = job.find(
                    "h3", class_='joblist-comp-name').text.replace(" ", '')
                more_info = job.header.h2.a['href']

                with open(f"{index}.txt", "w+") as f:
                    f.write(f"Complany Name: {company_name.strip()}\n")
                    f.write(f"Required skills: {skills.strip()}\n")
                    f.write(f"More Info: {more_info}\n")
                print(f"File No. {index} saved!")


if __name__ == "__main__":
    while True:
        find_jobs()
        wait = int(input("Enter minutes to wait: "))
        print(f"Waiting for {wait} minutes.......")
        time.sleep(wait*60)
