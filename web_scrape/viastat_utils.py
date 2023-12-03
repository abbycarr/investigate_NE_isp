import requests
import time


def get_viastat_offer_data(unit: str, street: str, city: str, state: str, zip_code: str, lat: float, lon: float):
    """
    Takes in the address and returns the data of the offer provided by Verisat.
    
    Parameters:
    unit : str - The unit of your apartment / building. (eg. 530)
    street : str - The address line containing the name of your street and building number. (eg. 220 Huntington Ave)
    city : str - The city that the street belongs to. (eg. Boston)
    state : str - The state abbreviation where the street and address is in. (eg. MA, CA, IA)
    zip_code : str - The zipcode of the address. (eg. 02120)
    
    Returns:
    dataDict : dictionary - The dictionary that contains all of the data.
    """
    headers = {
    'authority': 'buy.viasat.com',
    'accept': '*/*',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmbG93SWQiOiJiODFjMDE1ZS0wOTBhLTQxYTMtYWRiZC0zZjJjY2I4NDBhOTciLCJsYW5ndWFnZSI6ImVuIiwiY291bnRyeSI6IlVTIiwiZW52IjoicHJvZCIsImN1c3RvbWVyVHlwZSI6InJlc2lkZW50aWFsIiwiaWF0IjoxNzAxNDUxMjc0LCJleHAiOjE3MDE0NTQ4NzR9.KvGB1e1EFAosfDOQBRNJe9iDg4jqs1Jv_FPjXSePZf4',
    'content-type': 'application/json',
    # 'cookie': 'at_check=true; AMCVS_370765E45DE4FF8F0A495C94%40AdobeOrg=1; _gcl_au=1.1.2099547810.1701233050; _ga=GA1.1.1094327119.1701233050; _mkto_trk=id:396-AYU-154&token:_mch-viasat.com-1701233050435-70913; _biz_uid=8f5a94fea33b48b39d9618b9c37166a9; _biz_flagsA=%7B%22Version%22%3A1%2C%22Mkto%22%3A%221%22%2C%22Ecid%22%3A%221058641575%22%2C%22ViewThrough%22%3A%221%22%2C%22XDomain%22%3A%221%22%7D; _fbp=fb.1.1701233050850.767218924; s_cc=true; LDKEY=6c86328a-5c64-45ed-8dc3-8dfc02131025; tn-pixel-ref=Direct; tn-pixel-userId=55ea6878-9d6b-4e20-9a24-599e7b6f0c1b; AMCV_370765E45DE4FF8F0A495C94%40AdobeOrg=179643557%7CMCIDTS%7C19693%7CMCMID%7C46443462322129800141863332175276479611%7CMCAAMLH-1702056069%7C7%7CMCAAMB-1702056069%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1701458469s%7CNONE%7CvVersion%7C5.5.0; OptanonConsent=isGpcEnabled=0&datestamp=Fri+Dec+01+2023+12%3A21%3A11+GMT-0500+(Eastern+Standard+Time)&version=202306.2.0&browserGpcFlag=0&isIABGlobal=false&hosts=&landingPath=NotLandingPage&groups=C0001%3A1%2CBG43%3A1%2CC0003%3A1%2CC0002%3A1%2CSPD_BG%3A1%2CC0004%3A1&AwaitingReconsent=false; _biz_nA=6; _biz_pendingA=%5B%5D; _ce.irv=new; cebs=1; _ce.clock_event=1; _ce.clock_data=-48%2C155.33.132.18%2C1%2Ceede85db4b43e095858cc613d9c48e11; _clck=drn4ec%7C2%7Cfh6%7C0%7C1428; mbox=PC#3491480bc556452fa4757e807f6d560b.34_0#1764696075|session#4bc8a3a7a0b94fe99761bdb7955d74b2#1701453135; s_nr30=1701451274507-Repeat; adcloud={%22_les_v%22:%22y%2Cviasat.com%2C1701453074%22}; _uetsid=06734280906e11eea767a14e4670a1a6; _uetvid=f0bcb5e08e7111eea3cb9bc7650e53e2; _clsk=1mgyo50%7C1701451275220%7C2%7C1%7Cr.clarity.ms%2Fcollect; invoca_session=%7B%22ttl%22%3A%222023-12-31T17%3A21%3A16.887Z%22%2C%22session%22%3A%7B%22invoca_id%22%3A%22i-6e1ec818-3f81-4b31-a96a-1520f617865d%22%7D%2C%22config%22%3A%7B%22ce%22%3Atrue%2C%22fv%22%3Afalse%2C%22rn%22%3Afalse%7D%7D; connect.sid=s%3A23641bc9-077a-41c1-96b0-5c712c8cee39.H%2BZADcjHG5SxAlfoj4ANCLMNCtFN%2BJyDeFz00vkTn8I; cebsp_=3; _ce.s=v~12700f90237be4ead49aeec23116fd17d69f3410~lcw~1701451320096~lva~1701451272360~vpv~0~v11.cs~327010~v11.s~068f21f0-906e-11ee-8e16-5392db608757~v11.sla~1701451320180~lcw~1701451320181; _ga_SXSN1L2638=GS1.1.1701451271.2.1.1701451320.11.0.0; s_sq=%5B%5BB%5D%5D',
    'origin': 'https://buy.viasat.com',
    'referer': 'https://buy.viasat.com/en-US/r/pln',
    'sec-ch-ua': '"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
    }

    json_data = {
        'operationName': 'getAvailableProducts',
        'variables': {
            'input': {
                'location': {
                    'address': {
                        'addressLines': [
                            street,
                            unit,
                        ],
                        'municipality': city,
                        'region': state,
                        'postalCode': zip_code,
                        'countryCode': 'US',
                    },
                    'coordinates': {
                        'longitude': lon,
                        'latitude': lat,
                    },
                },
                'salesAgreementId': '3f9e0dd5-612a-49f6-9e22-15bebfbeb175',
                'productSegment': 'RESIDENTIAL',
            },
        },
        'query': 'query getAvailableProducts($input: GetAvailableProductsInputR0) {\n  getAvailableProducts(input: $input) {\n    id\n    name\n    characteristics {\n      dataCap\n      dataCapUnits\n      uploadSpeed\n      uploadUnits\n      downloadSpeed\n      downloadUnits\n      displayOrder\n      freeZone\n      resolution\n      productFamily\n      dataAllowanceText\n      textGeneral\n      textGeneral01\n      inflectionPointText\n      bannerColor\n      routerText\n      shortName\n      benefits\n      attribute1\n      attribute2\n      titleAddOns\n      serviceType\n      tag\n      imageOneUrl\n      isRegulated\n      contractTerm\n      contractTermUnit\n      feeText\n      downloadRange\n      uploadSpeedText\n      typicalDownloadSpeed\n      __typename\n    }\n    offerId\n    price\n    extensionTypes\n    promo {\n      price\n      duration\n      __typename\n    }\n    bestFor\n    isCafII\n    totalDiscount {\n      price\n      duration\n      __typename\n    }\n    digitalServices {\n      iconUrl\n      __typename\n    }\n    __typename\n  }\n}\n',
    }

    response = requests.post('https://buy.viasat.com/graphql', cookies={}, headers=headers, json=json_data)

    data = response.json()

    dataDict = {}
    dataDict['address_full'] = f'{unit}, {street}, {city}, {state}, {zip_code}'
    dataDict['incorporated_place'] = city
    dataDict['state'] = state
    dataDict['lat'] = lat
    dataDict['lon'] = lon
    dataDict['collection_datetime'] = time.time()
    dataDict['provider'] = 'Viasat'
    
    plan_name = data['data']['getAvailableProducts'][0]['name'].split()
    slow_down_speed = plan_name[1]
    
    fast_down_speed = data['data']['getAvailableProducts'][4]['name'].split()[1]
    
    dataDict['speed_down'] = slow_down_speed
    dataDict['speed_up'] = 'Not specified'
    dataDict['speed_unit'] = 'Mbps'
    dataDict['price'] = data['data']['getAvailableProducts'][0]['price']
    dataDict['technology'] = 'Satellite'
    dataDict['package'] = data['data']['getAvailableProducts'][0]['name']
    dataDict['fastest_speed_down'] = fast_down_speed
    dataDict['fastest_speed_price'] = data['data']['getAvailableProducts'][4]['price']

    return dataDict