#!/bin/bash
# Send POST request to a URL with email and subject variables and display the response body
curl -s -X POST "$1" -d "email=test@gmail.com" -d "subject=I will always be here for PLD"
