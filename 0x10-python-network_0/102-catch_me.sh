#!/bin/bash
# catch me if you can
(curl -s -o /dev/null -w "You got me!" "http://0.0.0.0:5000/catch_me" && true) || false
