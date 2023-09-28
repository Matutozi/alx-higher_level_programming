#!/bin/bash
#script that sends request to url and displays size of the response body
curl -s $1 -w "%{size_download}\n" -o /dev/null
