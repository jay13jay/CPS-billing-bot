#/usr/bin/env python3

import requests

startDate             = "2021-01-29"
endDate               = "2021-02-28"
timeframe             = "quarter_hour"
enhancedBilling       = "false"
includeRegisterData   = "false"
endpointURL           = 'https://cps.opower.com/ei/edge/apis/DataBrowser-v1/cws/utilities/cps/utilityAccounts/GUID/reads?'
urlOpts               = 'startDate=%s&endDate=%s&aggregateType=quarter_hour&includeEnhancedBilling=false&includeMultiRegisterData=false'


# print(endpointURL+"startDate="+startDate+"&endDate="+endDate+"&aggregateType="+"&includeEnhancedBilling="+enhancedBilling+"&includeMultiRegisterData="+includeRegisterData)
URL = endpointURL+"startDate="+startDate+"&endDate="+endDate+"&aggregateType="+"&includeEnhancedBilling="+enhancedBilling+"&includeMultiRegisterData="+includeRegisterData
# print(URL)



