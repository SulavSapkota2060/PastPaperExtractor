from bs4 import BeautifulSoup as bs
import requests
import argparse
import os
from termcolor import cprint
import datetime

parser = argparse.ArgumentParser()
parser.add_argument('-s', '--subject', required=True, type=str, action='store')
parser.add_argument('-y', '--year', required=True, type=int, action='store', help="Select a year.")
parser.add_argument('-pt', '--paper_type', required=False, type=str, action='store', help="Leave empty to download all")

args = parser.parse_args()


def makedir(dir_path):
    try:
        os.mkdir(dir_path)
    except FileExistsError as err:
        pass


def download(down_path, filename):
    try:
        os.mkdir(down_path)
    except FileExistsError as err:
        pass

    with open(f'{down_path}/{filename}', 'wb') as f:
        f.write(requests.get(file_link).content)
        cprint(f"Downloaded {filename}", 'green')

    return True


subjects = {
    "Physics": "Physics (9702)",
    "Chemistry": "Chemistry (9701)",
    "Computer": "Computer Science (for first examination in 2021) (9618)",
    "English": "English - Language AS and A Level  (9093)",
    "Mathematics": "Mathematics (9709)",
    "Biology": "Biology (9700)"
}
if args.subject == 'Computer':
    url = f"https://papers.gceguide.com/A%20Levels/{subjects[args.subject]}"
else:
    url = f"https://papers.gceguide.com/A%20Levels/{subjects[args.subject]}/{args.year}"

r = requests.get(url)
soup = bs(r.text, 'html.parser')

files = soup.select('li.file')

# Might be a bad practice to do it this way but here it goes.
user_path = os.path.expanduser('~/Documents')
makedir(f'{user_path}/PastPapers')
makedir(f'{user_path}/PastPapers/{args.subject}')
makedir(f'{user_path}/PastPapers/{args.subject}/{args.year}')

time_start = datetime.datetime.now()

download_files = 0
for file in files:

    link = file.find_all('a', href=True)[0]
    file_link = f"{url}/{link['href']}"

    file_type = link['href'].split("_")[2]
    if ".pdf" in file_type:
        file_type = file_type.strip(".pdf")

    if args.paper_type == '' or not args.paper_type:
        try:
            int(file_type)
            file_type = link['href'][-6:-4]
        except ValueError as err:
            pass
        path = f'{user_path}/PastPapers/{args.subject}/{args.year}/{file_type}'
        makedir(path)
        download(path, link['href'])
        download_files += 1

    elif file_type == args.paper_type:
        path = f'{user_path}/PastPapers/{args.subject}/{args.year}/{args.paper_type}'
        download(path, link['href'])
        download_files += 1

time_finish = datetime.datetime.now()
cprint("-----------------------\n Details:\n----------------------- ", 'magenta')
cprint(f"Start time:{time_start} \nFinished time: {time_finish}", 'yellow')
cprint(f"Total Time Taken: {time_finish - time_start}", 'yellow')
cprint(f"Total Downloads: {download_files} files.", 'yellow')
