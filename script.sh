curl 'https://cps.opower.com/ei/edge/apis/DataBrowser-v1/cws/utilities/cps/utilityAccounts/GUID/reads?startDate=2021-01-29&endDate=2021-02-28&aggregateType=quarter_hour&includeEnhancedBilling=false&includeMultiRegisterData=false' \
  -H 'Connection: keep-alive' \
  -H 'DNT: 1' \
  -H 'x-requested-with: XMLHttpRequest' \
  -H 'accept-language: en-US' \
  -H 'User-Agent: Jaime waves at the web log parsers :)' \
  -H 'opower-selected-entities: ["urn:opower:customer:uuid:GUID"]' \
  -H 'Accept: */*' \
  -H 'Origin: https://secure.cpsenergy.com' \
  -H 'Sec-Fetch-Site: cross-site' \
  -H 'Sec-Fetch-Mode: cors' \
  -H 'Sec-Fetch-Dest: empty' \
  -H 'Referer: https://secure.cpsenergy.com/' \
  -H 'Cookie: cookie-check=true; JSESSIONID=GUID; __direct-domain-access-fix=applied' \
  --compressed >> power_usage.json

  cat  feb_power_usage.json | grep value | awk '{print $2}' |  sed 's/,*$//g' | paste -sd+  | bc



Compare python vs curl URLS:

https://cps.opower.com/ei/edge/apis/DataBrowser-v1/cws/utilities/cps/utilityAccounts/GUID/reads?startDate=2021-01-29&endDate=2021-02-28&aggregateType=&includeEnhancedBilling=false&includeMultiRegisterData=false
https://cps.opower.com/ei/edge/apis/DataBrowser-v1/cws/utilities/cps/utilityAccounts/GUID/reads?startDate=2021-01-29&endDate=2021-02-28&aggregateType=quarter_hour&includeEnhancedBilling=false&includeMultiRegisterData=false
