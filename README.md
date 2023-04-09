# EDU-Sentiment-API
# Sentiment Analysis Microservice

This repository contains a simple sentiment analysis microservice implemented in Python using the FastAPI web framework. The microservice accepts input text data and returns a JSON response containing sentiment analysis results.

## Prerequisites

Before running the microservice, you will need to ensure that the following prerequisites are met:

- Python 3.9 installed on your system
- venv module installed (can be installed via `python3 -m pip install venv`)

## Installation

To install the microservice, follow these steps:

1. Clone the repository to your local system.
   ```
   git clone https://github.com/averliz/EDU-Sentiment-API.git
   cd EDU-Sentiment-API
   ```
2. Create a new virtual environment in the cloned directory. 
   ```
   python3 -m venv env
   ```
3. Activate the virtual environment. 
   For macOS:
   ```
   source env/bin/activate
   ```
   For Windows (using Command Prompt):
   ```
   env\Scripts\activate
   ```

4. Install the required dependencies.
   ```
   pip install -r requirements.txt
   ```

## Usage

To start the FastAPI server, run the following command in your terminal while your virtual environment is activated:

``` 
uvicorn main:app --reload
```
This will start the FastAPI server at http://localhost:8000. You can send HTTP POST requests to http://localhost:8000/api/edu-sentiment-analysis-service with JSON input data to get sentiment analysis results.


