import yaml
from pprint import pprint

with open('verify-apache.yml', 'r') as opened_file:
    verify_apache = yaml.safe_load(opened_file)

pprint(verify_apache)


with open('verify-apache.yml', 'w') as opened_file:
    yaml.dump(verify_apache, opened_file)


