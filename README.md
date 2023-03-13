# Lyzer-Scraper

## 1. Running the web server
### 1.1 Linux - Releases

After downloading the latest release from the releases tab, and unzipping the folder. You can do the following to run the web server.

```
cd Lyzer-Scraper/
./Lyzer-Scraper
```

### 1.2 Linux - Source Code

After cloning the repo, you can run the web server with the source code by doing the following.

```
cd Lyzer-Scraper/
python3 lyzer_scraper.py
```

### 1.3 Windows

It is possible to run this project using windows, you can also create executable using PyInstaller, you can find a command for this in the Makefile under `build-windows:`.

## 2. Command Line Arguments
### 2.1 Clearing the backlog

```
./Lyzer-Scraper --clear-backlog
```
