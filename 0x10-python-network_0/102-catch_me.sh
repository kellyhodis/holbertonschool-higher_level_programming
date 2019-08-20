#!/bin/bash
# Make request to 0.0.0.0:5000/catch_me that makes server respond "You got me!".
curl -Lbs -H "Origin:HolbertonSchool" -X PUT -d "user_id=98" 0.0.0.0:5000/catch_me
