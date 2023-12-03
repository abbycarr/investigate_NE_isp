import requests
import regex as re
from bs4 import BeautifulSoup
import time
import pandas as pd
import numpy as np

def get_fastest_speed_down_price(plans):
    names = []
    prices = []
    down_speeds = []

    for plan  in plans:

        name = plan.find(class_='plan-and-pricing-item__plan-data').text.strip()
        price = plan.find( class_='plan-and-pricing-item__monthly_price').text
        price = re.search('[0-9.]+', price).group()

        down_speed = plan.find('strong').text.split()[0]
        
        try:
            down_speed = eval(down_speed)
        except:
            down_speed = np.NaN
        
        prices.append(price)
        names.append(name)
        down_speeds.append(down_speed)
    
    ind = np.argmax([x for x in down_speeds if not pd.isna(x)])
    fastest_speed_down = down_speeds[ind]
    fastest_speed_price = prices[ind]
    
    return fastest_speed_down, fastest_speed_price

def get_hughes_offer_data(house_number: str, street_name: str, street_type:str, city: str, state: str, zip_code: str, lat: float, long: float):
    """
    Gets the response from https://www.hughesnet.com for searching for an offer at the given address
    in the United States.
    Parameters:
        house_number - str house number for the address
        street_name - str street name (i.e. Huntington)
        street_type - str type of street (i.e. Avenue, Boulevard, etc.)
        city - str name of city
        state - str state abberviation (i.e. MA)
        zip_code - str zip code
        lat - float latitude of the address
        long - float longitude for the address
    Return:
    json offer found for the given address
    """
    
    # replace the space with a "+" in the city name
    if ' ' in city:
        city = city.replace(' ', '+')
    # https://www.hughesnet.com
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/119.0',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'en-US,en;q=0.5',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'X-Requested-With': 'XMLHttpRequest',
        'Origin': 'https://www.hughesnet.com',
        'Connection': 'keep-alive',
        'Referer': 'https://www.hughesnet.com/get-started',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
    }
    params = {
        'ajax_form': '1',
        '_wrapper_format': 'drupal_ajax',
    }
    data = 'autocomplete={0}+{1}+{2}^%^2C+{3}^%^2C+{4}^%^2C+USA&street={0}&route={1}+{2}&city={3}&state={4}&zip={5}&country=United+States&lat={6}&lng={7}&administrative_area_level_3=&plan_type=Residential&epq_backup_street_address=&epq_backup_city=&epq_backup_state=&epq_backup_zip_code=&form_build_id=form-ZeKWKj-Yp0BAJ2jKqgybxmXAikOkANpiLHqPRGxS9Ug&form_id=epq_lookup_form&email=&_triggering_element_name=epq_lookup&_triggering_element_value=Find+Plans&_drupal_ajax=1&ajax_page_state^%^5Btheme^%^5D=hughes_na_theme&ajax_page_state^%^5Btheme_token^%^5D=&ajax_page_state^%^5Blibraries^%^5D=blazy^%^2Fload^%^2Cclassy^%^2Fbase^%^2Cclassy^%^2Fmessages^%^2Cclassy^%^2Fnode^%^2Ccore^%^2Finternal.jquery.form^%^2Ccore^%^2Fnormalize^%^2Cgeolocation_google_maps^%^2Fgoogle^%^2Chughes_form_epq^%^2Fepq-form-tfn^%^2Chughes_form_epq^%^2Fepq-lookup-library^%^2Chughes_na_theme^%^2Fglobal-css^%^2Chughes_na_theme^%^2Fglobal-js^%^2Chughes_utility^%^2Fhughes_utility.language^%^2Chughes_utility^%^2Fhughes_utility.tracking^%^2Chughesnet_na_base_theme^%^2Fcard-display-epq^%^2Chughesnet_na_base_theme^%^2Fcountry-selector^%^2Chughesnet_na_base_theme^%^2Fcountry_selector^%^2Chughesnet_na_base_theme^%^2Fcritical-general-css^%^2Chughesnet_na_base_theme^%^2Fepq-set-height^%^2Chughesnet_na_base_theme^%^2Fepq_lookup_block^%^2Chughesnet_na_base_theme^%^2Fexpandable-listing^%^2Chughesnet_na_base_theme^%^2Fform-label-animation^%^2Chughesnet_na_base_theme^%^2Fform-validation-message^%^2Chughesnet_na_base_theme^%^2Fglobal-offer-banner^%^2Chughesnet_na_base_theme^%^2Fhomepage-campaign-landing-common^%^2Chughesnet_na_base_theme^%^2Finit-tool-tip^%^2Chughesnet_na_base_theme^%^2Fload-current-date^%^2Chughesnet_na_base_theme^%^2Fmain-menu-pr-mx^%^2Chughesnet_na_base_theme^%^2Fmatch-height^%^2Chughesnet_na_base_theme^%^2Fmenu-footer-padding^%^2Chughesnet_na_base_theme^%^2Fmove-add-to-any^%^2Chughesnet_na_base_theme^%^2Fnodes^%^2Chughesnet_na_base_theme^%^2Fonecol_layout^%^2Chughesnet_na_base_theme^%^2Fparagraphs^%^2Chughesnet_na_base_theme^%^2Fpartial-css^%^2Chughesnet_na_base_theme^%^2Fplan-and-pricing-mobile-carousel^%^2Chughesnet_na_base_theme^%^2Fredirect-pr^%^2Chughesnet_na_base_theme^%^2Fshow-popup-content-link^%^2Chughesnet_na_base_theme^%^2Fsticky_cta_bar^%^2Chughesnet_na_base_theme^%^2Ftext^%^2Chughesnet_na_base_theme^%^2Ftoggle-whatsapp-hours^%^2Chughesnet_na_base_theme^%^2Ftwo-column-content^%^2Chughesnet_na_base_theme^%^2Futility_navigation^%^2Cparagraphs^%^2Fdrupal.paragraphs.unpublished^%^2Csmart_content_datalayer^%^2Fdatalayer_push^%^2Csystem^%^2Fbase'.format(house_number, street_name, street_type, city, state, zip_code, lat, long)
    response = requests.post('https://www.hughesnet.com/get-started', params=params, cookies={}, headers=headers, data=data)
    offer = response.json()
    
    upload_speed_dict = {'15 GB':3, '50 GB':3, 'Fusion 100GB':3, 'Fusion 200GB':5}
    fastest_down_speed ,fastest_speed_price = get_fastest_speed_down_price(BeautifulSoup(offer[12]['data']).find_all(class_='plan-and-pricing-item'))
    cheapest_plan = BeautifulSoup(offer[12]['data']).find(class_='plan-and-pricing-item')
    package = cheapest_plan.find(class_='plan-and-pricing-item__plan-data').text.strip()
    price = cheapest_plan.find( class_='plan-and-pricing-item__monthly_price').text
    price = re.search('[0-9.]+', price).group()
    download_details = cheapest_plan.find('strong').text.split()
    speed_down = download_details[0]
    speed_unit = download_details[1]
    speed_up = upload_speed_dict[package]

    data_dict ={}
    data_dict['address_full'] = '{0}, {1} {2}, {3}, {4}, {5}'.format(house_number, street_name, street_type, city, state, zip_code)
    data_dict['incorporated_place'] = city
    data_dict['state'] = state
    data_dict['lat'] = lat
    data_dict['lon'] = long
    data_dict['collection_datetime'] = time.time()
    data_dict['provider'] = 'hughes'
    data_dict['speed_down'] = speed_down
    data_dict['speed_up'] = speed_up
    data_dict['speed_unit'] = speed_unit
    data_dict['price'] = price
    data_dict['technology'] = 'Satellite'
    data_dict['package'] = package
    data_dict['fastest_speed_down'] = fastest_down_speed
    data_dict['fastest_speed_price'] = fastest_speed_price

    return data_dict
