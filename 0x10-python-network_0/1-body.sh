#!/bin/bash
# This script takes a URL as an argument, sends a GET request to that URL using curl,
# and displays the body of the response for a 200 status code.

URL="$1"

# Send the GET request using curl with the -s (silent mode) and -w (write-out) options
response=$(curl -s -w "%{http_code}" "$URL")

# Check if the response status code is 200
if [[ $response == 200 ]]; then
    # Display the body of the response
    curl -s "$URL"
else
    echo "Error: Non-200 status code received: $response"
fi
