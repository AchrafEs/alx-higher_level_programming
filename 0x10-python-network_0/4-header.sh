#!/bin/bash
# Send GET request to a URL with the X-School-User-Id header and display the response body
curl -s -H "X-School-User-Id: 98" "$1" ; echo ""
