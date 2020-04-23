#!/bin/sh

# Missing key usage extension:
# TLS Web client authentication

# SSL Client | Digital signature

# X509v3 extensions:
#     X509v3 Basic Constraints: critical
#         CA:TRUE
#     X509v3 Subject Key Identifier:
#         78:99:6B:80:27:DA:83:26:D4:D6:8C:40:F2:7B:BB:61:A4:34:E5:76
#     X509v3 Key Usage: critical
#         Certificate Sign, CRL Sign

# https://stackoverflow.com/questions/60691912/what-is-the-correct-certificate-purpose-for-ssl-client-in-python
#openssl x509 -in config/certificate.pem -text -noout
#openssl verify package/config/certificate.pem

find reports/behave -type f -name '*.json' -delete
find reports/behave -type f -name '*.html' -delete
find reports/log -type f -name '*.log' -delete
find reports/soap -type f -name '*.xml' -delete
find reports/screenshots -type f -name '*.png' -delete

# pip freeze > requirements.txt
# pip install -r requirements.txt

# python -m package.odatav4 $1


if ! [ -x "$(which npm)" ]; then
  if ! [ -z "$1" ]; then
    behave package/features
  else
    behave package/features --tags "$1"
  fi
else
  if ! [ -d "node_modules" ]; then
    npm install
  fi

  if ! [ -z "$1" ]; then
    behave -f json -f plain \
      -o reports/behave/report.json \
      package/features --tags "$1"
  else
    behave -f json \
      -o reports/behave/report.json \
      package/features
  fi

  if [ -f "reports/behave/report.json" ]; then
    python -m behave2cucumber \
      -i reports/behave/report.json \
      -o reports/behave/cucumber.json
    if [ -f "reports/behave/cucumber.json" ]; then
      node behave_reporter.js
    fi
  fi
fi
