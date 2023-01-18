FROM ubuntu:latest

COPY . .

RUN apt update
RUN apt install nala -y
RUN nala update
RUN nala upgrade -y
RUN nala install -y wget
RUN wget -q https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
RUN nala install -y ./google-chrome-stable_current_amd64.deb
RUN nala install python3-pip -y
RUN nala install python-is-python3 -y
RUN pip install pipenv
RUN pipenv install
RUN pipenv run pytest testing --cov
RUN pipenv run pyinstaller lyzer_scraper.py --name Lyzer-Scraper --add-data backup/:data/ -y

CMD ["make", "run-ubuntu"]
