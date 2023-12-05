from flask import Flask, request
from mars_emails import get_mars_photo, send_mars_email

app = Flask(__name__)

@app.route('/email', methods=['POST'])
def email_respponse():
    to_email = request.form['to']
    from_email = request.form['from']
    text = request.form['text']

    sol = str.split(text)[0]

    #error checking
    if sol.isdigit():
        img_url = get_mars_photo(sol)
    else:
        img_url = get_mars_photo(1000)
    
    send_mars_email(from_email, to_email, sol)