FROM ubuntu:22.04

COPY . .

RUN apt-get update
RUN apt-get install -y make
RUN apt-get install -y wget
RUN wget -q https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
RUN apt-get install -y ./google-chrome-stable_current_amd64.deb
RUN apt-get install python3-pip -y
RUN apt-get install python-is-python3 -y
RUN pip install pipenv
RUN pipenv install
RUN pipenv run pytest testing --cov
RUN make build

EXPOSE 8080

CMD ["make", "run-ubuntu"]
