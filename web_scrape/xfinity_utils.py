import requests 
import numpy as np
import time
import regex as re

def get_xfinity_offer_data(house_number: str, street_name: str, street_type:str, city: str, state: str, zip_code: str, lat: float, long: float):
    address = '{0} {1} {2}, {3}'.format(house_number, street_name, street_type, zip_code)
    headers = {
        'authority': 'www.xfinity.com',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9',
        'adrum': 'isAjax:true',
        'cache-control': 'no-cache',
        'pragma': 'no-cache',
        'referer': 'https://www.xfinity.com/planbuilder',
        'sec-ch-ua': '"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
    }

    with requests.Session() as s:

        # get a new set of cookies and a session id
        usercontext = s.get(
            'https://www.xfinity.com/sitecore/api/learn/neptune/persistencelayer/usercontext',
            #cookies=cookies,
            headers=headers,
        )

        # get the location id for the address of interests
        suggestions = s.get(
            f'https://www.xfinity.com/sitecore/api/learn/neptune/address-search/suggestions?show=false&search={address}',
            headers=headers,
        ).json()

        # now that we have cookies and the suggestions dict, we hit the localize API endpoint with the first suggestion to get the HK into the cookies
        json_data = {
            'AutoBuild': False,
            'AdditionalQueryParams': '',
            'Address': suggestions['Data'][0]['Address'],
            'RedirectURL': '/digital/offers/plan-builder',
            'RedirectionType': '',
            'OfferId': '',
            'OfferLobs': '',
            'XeppPromoId': '',
            'TenantInfo': {},
            'isACPOpted': False,
            'DisableRedirectUrl': False,
        }

        response = s.post(
            'https://www.xfinity.com/sitecore/api/learn/neptune/localize',
            headers=headers,
            json=json_data,
        )

        # and, at last, the offers API
        json_data = {
            'acpToggle': False,
        }

        response = s.post('https://digital.xfinity.com/offers/api/offerpackaging', headers=headers, json=json_data)

        offer = response.json()

        # get inernet plans
        # intialize plans
        internet_plan_info = []
        # store content
        content =  offer['CONTENT']
        for plan_id in content.keys():
            plan = content[plan_id]
            # only keep offers with certain keys that indicate they are an internet plan
            if 'InternetPlanID' in plan.keys() and 'Name' in plan.keys():
                # store key information about each plan
                internet_plan_info.append([plan['InternetPlanID'], plan['DownloadSpeed'], plan['UploadSpeed'], plan['EdpPrice']])    

        # get cheapest plan
        min_price = min([plan[3] for plan in internet_plan_info])
        cheapest_plan = [plan for plan in internet_plan_info if plan[3] == min_price]

        all_down_speeds = [eval(re.findall('[0-9]+', plan[1])[0]) for plan in internet_plan_info]
        ind = np.argmax(all_down_speeds)
        fastest_speed_down = all_down_speeds[ind]
        fastest_speed_price = [plan[3] for plan in internet_plan_info][ind]

        # ensure if there is more than 1 plan, that they have hte same information
        if len(cheapest_plan)>1:
            if cheapest_plan[0] != cheapest_plan[1]:
                raise Warning('Multiple cheapest plans with different plan information.')

        # take first cheapest plan
        cheapest_plan = cheapest_plan[0]

        package = cheapest_plan[0]
        price = cheapest_plan[3]

        # get download speed and units
        download_info = cheapest_plan[1].split(' ')
        speed_down = download_info[len(download_info)-2]
        speed_unit = download_info[len(download_info)-1]

        # get upload speed and units
        upload_info = cheapest_plan[2].split(' ')
        speed_up = upload_info[len(upload_info)-2]

        data_dict ={}
        data_dict['address_full'] = '{0}, {1} {2}, {3}, {4}, {5}'.format(house_number, street_name, street_type, city, state, zip_code)
        data_dict['incorporated_place'] = city
        data_dict['state'] = state
        data_dict['lat'] = lat
        data_dict['lon'] = long
        data_dict['collection_datetime'] = time.time()
        data_dict['provider'] = 'xfinity'
        data_dict['speed_down'] = speed_down
        data_dict['speed_up'] = speed_up
        data_dict['speed_unit'] = speed_unit
        data_dict['price'] = price
        data_dict['technology'] = 'Cable'
        data_dict['package'] = package
        data_dict['fastest_speed_down'] = fastest_speed_down
        data_dict['fastest_speed_price'] = fastest_speed_price

    return data_dict
