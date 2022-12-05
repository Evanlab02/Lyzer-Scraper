"""
This module will be used to create and modify the flask web app.
"""
from flask import Flask, request

from src.file_parser import load_json_data
from src.scraper_helper import full_scrape

def create_web_app(home_directory: str):
    """
    This function will create the web app.
    """
    app = Flask(__name__)

    @app.route("/links", methods=["POST", "GET"])
    def links():
        """
        This function will handle the links endpoint.
        """
        if request.method == "POST":
            links = request.json
            codes = []
            for link in links:
                exit_code = full_scrape(["web-app", "--link", link], home_directory)
                codes.append(exit_code)
            return {"exit_codes": codes}

        if request.method == "GET":
            links = load_json_data(f"{home_directory}/.lyzer/links.json")
            return links

        return {"error": "Invalid Content-Type"}

    @app.route("/file/<file>", methods=["GET"])
    def file(file: str):
        """
        This function will handle the file endpoint.
        """
        file_name = f"{home_directory}/.lyzer/{file}.json"
        file_data = load_json_data(file_name)
        if file_data == {}:
            return {"error": f"file not found -> {file_name}"}
        return file_data

    return app
