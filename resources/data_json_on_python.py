import json
# Пока не разобрался как поместить это в class

with open('/Users/antongrunt/Desktop/project/symphony-solutions.eu_contact_form/resources/data.json', 'r') as f:
    secret_variables = json.load(f)

NAME_ADMIN = secret_variables['name']
PASSWORD_ADMIN = secret_variables['password']
URL_CONTACT_US = secret_variables['endpoint']
URL_QUICK_APPLY = secret_variables['endpoint_quick_apply']


