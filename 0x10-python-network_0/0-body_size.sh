#!/bin/bash
# This script takes a URL as an argument, sends a request to that URL using curl,
# and displays the size of the response body in bytes.

URL="$1"

# Send the request using curl with the -s (silent mode) and -o (output to /dev/null) options
# to suppress any progress or output
response=$(curl -s -o /dev/null -w '%{size_download}' "$URL")

echo "Response body size: $response bytes"
