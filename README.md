
# RelyComply Social Media Activity API

## Overview

This Flask application provides an API endpoint to fetch live data on the activity levels of different social networks. It's designed to serve as an input for AI trading bots, offering a numeric indicator of the amount of content posted on each social network. The application fetches data asynchronously from predefined social media endpoints and handles unpredictable responses and potential errors gracefully.

## Features

- Asynchronous data fetching from multiple social media endpoints.
- Robust error handling to cope with unreliable external APIs.
- Returns a JSON response with the count of activities for each social media platform.

## Requirements

- Python 3
- Flask
- aiohttp

## Installation

1. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

1. To start the Flask server, run:
   ```bash
   flask run
   ```

2. By default, the server will start on `http://127.0.0.1:5000`.

## Testing the Endpoint

1. To check if the endpoint is running and functioning correctly, you can use a tool like `curl` or any API testing tool like Postman.

2. Use the following command or set up a request in your API tool:
   ```bash
   curl http://127.0.0.1:5000/social_network_activity
   ```

3. The endpoint should return a JSON response with the count of activities for each social media platform, such as:
   ```json
   {
     "twitter": 2,
     "facebook": 5,
     "instagram": 3
   }
   ```

   In case of an error while fetching data from any social media platform, the count will be `0`.

## Notes

- The application handles errors by returning `0` for a specific platform if there is an issue fetching data.
- The error handling can be observed by intentionally pointing to a non-existing or faulty endpoint.
