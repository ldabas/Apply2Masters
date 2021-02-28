import pandas as pd
import requests
import logging
logging.basicConfig(level = logging.INFO)

pd.set_option('display.expand_frame_repr', False)


"""


def make_request(form_id, token):
    url = 'https://api.typeform.com/forms/{}/responses'.format(form_id)
    return requests.get(url,
                       headers = {'Authorization': 'bearer {}'.format(token)})

def get_responses(form_id):
    token = '55hntDubVXhPAQEua2bBVivwfJypUa7a5KKBpApSbyvv'
    res = make_request(form_id, token)

    return res
answer = get_responses('Dd3tYlRv')
print(answer.json())


import requests
import json
a = json.loads(answer.text)


from pandas import json_normalize

df = json_normalize(a, 'items')


def get_typeform_responses(form_id):
    responses = get_responses(form_id)
    responses = [r for r in responses]
    df = pd.DataFrame([r for r in responses if r])
    return df

what = get_typeform_responses('Dd3tYlRv')
what.to_csv(r'here.csv',index=False)
"""

import re

txt = "dsfdbgfflag{Is {.*}t=This}"
newstr = re.escape(txt)
print(newstr)

x = re.search("flag\{.*\}$", txt)
print(x.group())
