#!/bin/bash
# GET request to $1 with header X-School-User-Id: 98, prints response body
curl -s -X GET -H "X-School-User-Id: 98" "$1"
