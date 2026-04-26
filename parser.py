import requests
import fake_useragent
from bs4 import BeautifulSoup as BS
from datetime import datetime


def get_schedule():
    today = datetime.now()
    formatted_date = today.strftime("%d.%m.%Y")

    session = requests.Session()
    url = "https://e-rozklad.duikt.edu.ua/time-table/student?type=0"
    soup = BS(session.get(url).text, "lxml")
    csrf_token = soup.find('meta', attrs={'name': 'csrf-token'}).get('content')

    user = fake_useragent.UserAgent().random
    header = {'User-Agent': user}

    data = {
        "_csrf-frontend": csrf_token,
        "TimeTableForm[facultyId]": "1",
        "TimeTableForm[course]": "1",
        "TimeTableForm[groupId]": "1505",
        "TimeTableForm[studentId]": "47717"
    }

    response = session.post(url, headers=header, data=data).text
    soup = BS(response, "lxml")

    block = soup.find('div', class_='table-container')
    pairs = block.find_all('div', class_="lesson-1")

    list_pairs = {}
    for pair in pairs:
        info = pair.find('div', attrs={'data-toggle': 'popover'})
        if info:
            date_info = info.get('title')
            info_pair = info.get('data-content')
            clean_date = date_info.split()[0]
            timetablePair = date_info.split()[1]
            formattedInfo_pair = info_pair.replace('<br>', '\n')
            namePair = formattedInfo_pair.split('\n')[0]

            if clean_date == formatted_date:
                list_pairs[timetablePair] = namePair

    for i in range(1, 6):
        if str(i) not in list_pairs:
            list_pairs[str(i)] = None

    return dict(sorted(list_pairs.items()))