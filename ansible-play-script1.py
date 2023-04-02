import jinja2
import os

import jinja2
import os


from jinja2 import Environment, FileSystemLoader
import os

# Set up Jinja2 environment
env = Environment(loader=FileSystemLoader('.'))
template = env.get_template('playbook_template.j2')

# Define variables for the playbook
hosts = ['webserver1', 'webserver2']
username = 'myusername'
password = 'mypassword'
app_name = 'myapp'

# Render the template with the variables
playbook = template.render(hosts=hosts, username=username, password=password, app_name=app_name)

# Save the rendered playbook to a file
with open('myplaybook.yml', 'w') as f:
    f.write(playbook)

# Run the playbook using Ansible
os.system('ansible-playbook myplaybook.yml')
