#!/bin/bash
#script that displays allowed http methods
curl -sI $1 | grep Allow | cut -d " " -f 2-
