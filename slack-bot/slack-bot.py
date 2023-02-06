import subprocess
import requests
from flask import Flask, request, render_template

dependencies = ['flask', 'requests']

for dependency in dependencies:
    try:
        __import__(dependency)
    except ImportError:
        user_input = input(f'{dependency} is not installed. Do you want to install it now? (y/n) ')
        if user_input.lower() == 'y':
            subprocess.run(['pip', 'install', dependency], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            print(f'{dependency} has been installed.')
        else:
            print(f'{dependency} is required. Please install it and try again.')

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        jira_number = request.form['jira_number']
        tenant_name = request.form['tenant_name']
        # Slack API
        url = 'https://slack.com/api/chat.postMessage'
        headers = {
            'Authorization': f'Bearer xapp-1-ANW860D0V-4750540874357-8022ff395a2e23e24bb9b325971dea8949f5ec23e0f897926a65ea185869692b',
            'Content-Type': 'application/json;charset=utf-8'
        }
        data = {
            'channel': '#nick-test-channel',
            'text': f'JIRA Number: {jira_number}\nTenant Name: {tenant_name}'
        }
        response = requests.post(url, headers=headers, json=data)
        if response.status_code == 200:
            return 'Slack chat created successfully!'
        else:
            return 'Failed to create Slack chat. Please try again later.'
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
