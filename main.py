import csv

import requests
from bs4 import BeautifulSoup

date = input("Enter the date (YYYY-MM-DD):\n")
filename = input("Enter the filename to save the data in ['filename.csv']:\n")
page = requests.get(f"https://www.yallakora.com/match-center/?date={date}")

src = page.content
soup = BeautifulSoup(src, "html.parser")
match_list = []


def write_to_csv(match_list):
    with open(filename, "w", newline="", encoding="utf-8-sig") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=[
                "Championship",
                "Home",
                "Score",
                "Away",
                "Status",
                "Time",
                "Date",
            ],
        )
        writer.writeheader()
        writer.writerows(match_list)


def get_match_data():
    championships = soup.find_all("div", {"class": "matchCard"})
    for championship in championships:
        championshipTitle = (
            championship.find("div", {"class": "title"})
            .find("h2")
            .text.strip()
            .replace("..", "")
        )
        matches = championship.find("div", {"class": "ul"}).find_all(
            "div", {"class": "item"}
        )

        for match in matches:
            matchStatus = (
                match.find("a")
                .find("div", {"class": "matchStatus"})
                .find("span")
                .text.strip()
            )
            home_team = (
                match.find("a").find("div", {"class": "teamA"}).find("p").text.strip()
            )
            away_team = (
                match.find("a").find("div", {"class": "teamB"}).find("p").text.strip()
            )
            home_score = (
                match.find("a")
                .find("div", {"class": "MResult"})
                .find_all("span", {"class": "score"})[0]
                .text.strip()
            )
            away_score = (
                match.find("a")
                .find("div", {"class": "MResult"})
                .find_all("span", {"class": "score"})[1]
                .text.strip()
            )
            time = (
                match.find("a")
                .find("div", {"class": "MResult"})
                .find("span", {"class": "time"})
                .text.strip()
            )
            match_list.append(
                {
                    "Championship": championshipTitle,
                    "Home": home_team,
                    "Score": f"{home_score}-{away_score}",
                    "Away": away_team,
                    "Status": matchStatus,
                    "Time": f"{date} - {time}",
                    "Date": date,
                }
            )


get_match_data()
write_to_csv(match_list)