# Studying Disparities in Internet Deals in the Northeast

This repository contains code to discovery disparities in internet packages offered in Boston, MA. The code and methods of the study are from the Mark Up team that wrote "[Dollars to Megabits: You May Be Paying 400 Times As Much As Your Neighbor for Internet](https://themarkup.org/still-loading/2022/10/19/dollars-to-megabits-you-may-be-paying-400-times-as-much-as-your-neighbor-for-internet-service)" in the series [Still Loading](https://themarkup.org/series/still-loading).

We describe our methodology in "[Studying Disparities in Internet Deals in the Northeast Report](https://github.com/abbycarr/investigate_NE_isp/blob/main/report.ipynb)".

Please read that document to understand the context for the code and data in this repository. 

## Data
This directory is where inputs, intermediaries, and outputs are saved.

### Input
In `data/input/`, we store all files taken as inputs to notebooks. `data/addresses/` contains all cities scraped.

In `data/census/`, we store all census data including data from the American Community Survey  in `data/census/acs5`.

In `data/fcc/`, we store data from the FCC's Form 477. 

In `data/intermediary/`, we story all offers scraped. We story the original offers scraped in batches in (`data/intermediary/scrape_offers_batches/`) and then combine all the data in one location in (`data/intermediary/offers/`).

In `data/open_address/`, we story all addresses for cities we plan to scrape. `data/open_address/original_data/` has the original unaltered data from open address. `data/open_address/processed/` has the sample of addresses chosen for each city, stored as csv's and geojson.gz files in `data/open_address/processed/csv/` and `data/open_address/processed/geojson/`.

In `data/output/`, we store the outputs of all reports and visualizations done on the scraped offers. We story figures in `data/output/figs/`, maps in `data/output/maps/`, and processed offers joined on census American Community Survey data in `data/output/speed_price_hughes.csv.gz` for each provider (the example being for Hughes Net). The speed_price files contain the following columns:

| column                      | description                                                                                                                                    |
|:----------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------|
| `address_full`                | The complete postal address of a household we searched.                                                                                        |
| `incorporated_place`          | The incorporated city that the address belongs to.                                                                                              |
| `major_city`                  | The city that the address is in.                                                                                                               |
| `state`                       | The state that the address is in.                                                                                                          |
| `lat`                         | The address’s latitude. From OpenAddresses or NYC Open Data.                                          |
| `lon`                         | The address’s longitude. From OpenAddresses or NYC Open Data.                                           |
| `block_group`                 | The Census block group of the address, as of 2019. From the Census Geocoder API based on `lat` and `lon`.                                                                                              |
| `collection_datetime`         | The Unix timestamp that the address was used to query the provider's website.                                                                   |
| `provider`                    | The internet service provider.                                                                                                                  |
| `speed_down`                  | Cheapest advertised download speed for the address.                                                                                            |
| `speed_up`                    | Cheapest advertised upload speed for the address.                                                                                              |
| `speed_unit`                  | The unit of speed. This is always in megabits per second (Mbps).                                                                                |
| `price`                       | The cost in USD of the cheapest advertised internet plan for the address.                                                                       |
| `technology`                  | The kind of technology (fiber or non-fiber) used to serve the cheapest internet plan.                                                           |
| `package`                     | The name of the cheapest internet plan.                                                                                                         |
| `fastest_speed_down`          | The advertised download speed of the fastest package. This is usually the same as the cheapest plan if the `speed_down` is less than 200 Mbps. |
| `fastest_speed_price`         | The advertised upload speed of the fastest internet package for the address.                                                                   |
| `fn`                          | The name of the file of API responses where this record was parsed from. To be used for trouble shooting. API responses are hosted externally in AWS s3.                                                                       |
| `redlining_grade`             | The redlining grade, merged from Mapping Inequality based on the `lat` and `lon` of the adddress.                                              |
| `race_perc_non_white`         | The percentage of people of color (not non-Hispanic White) in the addresse's Census block group expressed as a proportion. Sourced from the 2019 5-year American Community Survey.  |
| `median_household_income `    | The median household income in the addresses' Census block group. Sourced from the 2019 5-year American Community Survey                       |
| `income_lmi`                  | `median_household_income` divided by the city median household income (sourced from U.S. Census Bureau).                                                                         |
| `income_dollars_below_median` | City median household income minus the `median_household_income`.                                                                              |
| `ppl_per_sq_mile`             | People per square mile is used to determine population density. Sourced from 2019 TIGER shape files from the U.S. Census Bureau.               |
| `n_providers`                 | The number of other wired competitors in the addresses' Census block group. Sourced from FCC Form 477.                                              |
| `internet_perc_broadband`     | The percentage of the population that is already subscriped to broadband in an addresses' Census block group expressed as a proportion.                                  |

## Notebooks
The Python/Jupyter notebooks in this repository’s notebooks/ directory demonstrate the steps we took to process and analyze the data we collected. If you want a quick overview of the main methodology, you can skip directly to 3-statistical-tests-and-regression.ipynb.

### 0-get-address-pasring.ipynb
This notebook is to process addresses from open address and add census information to them inorder for offer scraping functions to properly work. 

### 1-process-offers.ipynb
This notebook parses and preprocesses offers collected from each ISP's service lookup tools.

### 2a-hughes-reports.ipynb / 2b-xfinity-reports.ipynb / 2c-viasat-reports.ipynb / 2d-compare_all.ipynb
An overview of offers by each ISP. This contains breakdowns for each city served by the ISP by income level, race/ethnicity, and historical redlining grades. 

### aggregators.py
This contains all functions needed to proccess offers and turn them into visualizations. 

### config.py
This contains all variables needed to proccess offers and turn them into visualizations. 

### parsers.py
This contains all functions needed to parse offers. 

## offer_scrape
The files here are dedicated to scraping internet package offers from the chosen ISPs: Hughes Net, Xfinity, and Viasat. 

### hughes_utils
This file contains all functions needs to collect offers from Hughes Net.

### xfinity_utils
This file contains all functions needs to collect offers from Xfinity.

### viasat_utils
This file contains all functions needs to collect offers from Viasat.

### scrape_all_isps.ipynb
This notebook uses all scarping functions to scrape offers from all ISP's for the processed addresses stored in `data/open_address/processed`

## analytic_files
The files here are used to run repoty.ipynb.

## report.ipynb
The final report as specified  for in the final project instructions.
