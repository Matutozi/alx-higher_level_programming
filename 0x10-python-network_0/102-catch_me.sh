#!/bin/bash
#Send PUT request to passed url, only for user_id=98
curl -sLX PUT 0.0.0.0:5000/catch_me -d "user_id=98" -H "Origin: HolbertonSchool"
