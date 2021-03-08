import requests

cpsUID                = "REPLACEWITHUSERID"
startDate             = "2021-01-29"
endDate               = "2021-02-28"
timeframe             = "quarter_hour"
enhancedBilling       = "false"
includeRegisterData   = "false"
userAgent             = "Checking my usage, bro, don't taze me"
language              = "en-US"
oPowerEntities        = ["urn:opower:customer:uuid:"+cpsUID]

cookies = {
    'cookie-check': 'true',
    'JSESSIONID': cpsUID,
    '__direct-domain-access-fix': 'applied',
}

headers = {
    'Connection': 'keep-alive',
    'DNT': '1',
    'x-requested-with': 'XMLHttpRequest',
    'accept-language': language,
    'User-Agent': userAgent,
    'opower-selected-entities': oPowerEntities,
    'Accept': '*/*',
    'Origin': 'https://secure.cpsenergy.com',
    'Sec-Fetch-Site': 'cross-site',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://secure.cpsenergy.com/',
}

params = (
    ('startDate', startDate),
    ('endDate', endDate),
    ('aggregateType', timeframe),
    ('includeEnhancedBilling', enhancedBilling),
    ('includeMultiRegisterData', 'false'),
)
print("cookies:\n",params)

# response = requests.get('https://cps.opower.com/ei/edge/apis/DataBrowser-v1/cws/utilities/cps/utilityAccounts/GUID/reads', headers=headers, params=params, cookies=cookies)
# response = requests.get('https://cps.opower.com/ei/edge/apis/DataBrowser-v1/cws/utilities/cps/utilityAccounts/GUID/reads?startDate=2021-01-29&endDate=2021-02-28&aggregateType=quarter_hour&includeEnhancedBilling=false&includeMultiRegisterData=false', headers=headers, cookies=cookies)
