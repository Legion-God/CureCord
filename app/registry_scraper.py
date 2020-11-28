"""
TODO:use redis and task queue for Async processing.
"""
from urllib.parse import quote
import requests
import json


def spider(doc_name, doc_registration_number, doc_state_medical_council, doc_year_registration):
    """
    Returns the Doc's information from IMR in Python Dict
    :param doc_name: string
    :param doc_registration_number: string numb
    :param doc_state_medical_council: string numb
    :param doc_year_registration: string numb
    :return: Doc's information Dict.
    """
    doc_name = quote(doc_name)

    cookies = {}
    headers = {
        'Connection': 'keep-alive',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'DNT': '1',
        'X-Requested-With': 'XMLHttpRequest',
        # 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36 Edg/87.0.664.47',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://www.nmc.org.in/information-desk/indian-medical-register',
        'Accept-Language': 'en-US,en;q=0.9',
    }

    params = (
        ('service', 'getPaginatedDoctor'),
        ('draw', '1'),
        ('columns[0][data]', '0'),
        ('columns[0][name]', ''),
        ('columns[0][searchable]', 'true'),
        ('columns[0][orderable]', 'true'),
        ('columns[0][search][value]', ''),
        ('columns[0][search][regex]', 'false'),
        ('columns[1][data]', '1'),
        ('columns[1][name]', ''),
        ('columns[1][searchable]', 'true'),
        ('columns[1][orderable]', 'true'),
        ('columns[1][search][value]', ''),
        ('columns[1][search][regex]', 'false'),
        ('columns[2][data]', '2'),
        ('columns[2][name]', ''),
        ('columns[2][searchable]', 'true'),
        ('columns[2][orderable]', 'true'),
        ('columns[2][search][value]', ''),
        ('columns[2][search][regex]', 'false'),
        ('columns[3][data]', '3'),
        ('columns[3][name]', ''),
        ('columns[3][searchable]', 'true'),
        ('columns[3][orderable]', 'true'),
        ('columns[3][search][value]', ''),
        ('columns[3][search][regex]', 'false'),
        ('columns[4][data]', '4'),
        ('columns[4][name]', ''),
        ('columns[4][searchable]', 'true'),
        ('columns[4][orderable]', 'true'),
        ('columns[4][search][value]', ''),
        ('columns[4][search][regex]', 'false'),
        ('columns[5][data]', '5'),
        ('columns[5][name]', ''),
        ('columns[5][searchable]', 'true'),
        ('columns[5][orderable]', 'true'),
        ('columns[5][search][value]', ''),
        ('columns[5][search][regex]', 'false'),
        ('columns[6][data]', '6'),
        ('columns[6][name]', ''),
        ('columns[6][searchable]', 'true'),
        ('columns[6][orderable]', 'true'),
        ('columns[6][search][value]', ''),
        ('columns[6][search][regex]', 'false'),
        ('order[0][column]', '0'),
        ('order[0][dir]', 'asc'),
        ('start', '0'),
        ('length', '500'),
        ('search[value]', ''),
        ('search[regex]', 'false'),
        ('name', doc_name),
        ('registrationNo', doc_registration_number),
        ('smcId', doc_state_medical_council),
        ('year', doc_year_registration),
        ('_', '1606563996395'),
    )
    # smcID is state medical council Id, refer to registy to find the order, first value = 1

    response = requests.get('https://www.nmc.org.in/MCIRest/open/getPaginatedData',
                            headers=headers,
                            params=params,
                            cookies=cookies)

    dirty_resp = json.loads(response.text)
    # converts the response to JSON dict for cleaning.

    total_records = dirty_resp.get("recordsFiltered")
    if total_records == 0:
        raise ValueError("No records found, enter correct args.")
    elif total_records > 1:
        raise ValueError("Multiple records found, enter Doctor specific details.")

    dirty_list = dirty_resp.get("data")[0]
    # Stores the data about the Docs.

    # Create Doc's JSON from response list.
    doc_response = {}
    doc_response.update({'registrationNumber': dirty_list[2]})
    doc_response.update({'stateMedicalCouncil': dirty_list[3]})
    doc_response.update({'name': dirty_list[4]})

    # TODO:Comment out this line in production.
    print(json.dumps(doc_response, indent=4, sort_keys=True))

    return doc_response



# Test data, REMOVE this in production.
if __name__ == '__main__':
    spider(doc_name='Chandra Kailash',
           doc_registration_number='6053',
           doc_state_medical_council='',
           doc_year_registration='')
