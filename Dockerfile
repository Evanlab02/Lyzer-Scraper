FROM ubuntu:latest

COPY . .

RUN apt update
RUN apt upgrade -y
RUN apt install -y make
RUN apt install -y wget
RUN wget -q https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
RUN apt install -y ./google-chrome-stable_current_amd64.deb
RUN apt install python3-pip -y
RUN apt install python-is-python3 -y
RUN pip install pipenv
RUN pipenv install
RUN pipenv run pytest testing --cov
RUN make build

EXPOSE 8080

CMD ["make", "run-ubuntu"]
