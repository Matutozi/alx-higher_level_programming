#!/bin/bash
#Send post request to passed url and display body of response
curl -sX POST $1 -d "email=test@gmail.com&subject=I will always be here for PLD"
