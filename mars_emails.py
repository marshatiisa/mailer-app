import os
from random import choice

import requests
from sendgrid import SendGridAPIClient
from send.helpers.mail import Mail
#add the url
rover_url = ''

def send_mars_email(to_email, from_email, img_url):
    message = Mail(from_email = from_email,
                   to_email = to_email,
                   subject= 'Here is your mars rover photo',
                   html_content = '<br></br>'
                   )


def get_mars_photo(sol):
    params = {'sol': sol, 'api_key': os.environ.get('NASA_API_KEY')}
    resp = requests.get(rover_url, params).json()
    # use json method to convert to python dictionary
    img_url = choice(resp['photos'])['img_src']

    return img_url