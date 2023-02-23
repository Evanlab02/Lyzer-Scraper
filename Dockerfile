FROM ubuntu:22.04

COPY . .

RUN apt-get update
RUN apt-get install -y make
RUN apt-get install -y wget
RUN wget -q https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
RUN apt-get install -y ./google-chrome-stable_current_amd64.deb
RUN apt-get install python3-pip -y
RUN apt-get install python-is-python3 -y

RUN pip install --upgrade pip
RUN pipenv install
RUN pipenv run pytest -v testing
RUN pipenv check
RUN pipenv run pyinstaller --name Lyzer-Scraper --add-data backup/:data/ lyzer_scraper.py

EXPOSE 8000

CMD ["make", "run-bin"]
