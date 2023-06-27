#!/bin/bash
# This script takes a URL as the first argument, sends a DELETE request to that URL using curl,
# and displays the body of the response.

URL="$1"

# Send the DELETE request using curl with the -s (silent mode) and -X DELETE options
response=$(curl -s -X DELETE "$URL")

# Display the body of the response
echo "$response"
