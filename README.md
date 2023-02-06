# slack-bot
Quick Easy Slack Chat Creator
The program we created, named "slack-bot.py," is a basic script that demonstrates how to use the Slack API to interact with a Slack workspace. Here's how it works:

The script starts by importing the necessary libraries, such as Flask, Requests, and Subprocess. These libraries are used to handle HTTP requests, sending API requests to Slack, and running shell commands, respectively.

Next, the script sets up a Flask application and creates a single endpoint "/". This endpoint will be the landing page for the form where the user can input the Jira number and tenant name.

The endpoint uses a simple HTML form that allows the user to input the Jira number and tenant name. The form is submitted using the POST method, and the data from the form is processed by the endpoint.

The script then uses the Subprocess library to run a shell command to check if all the necessary dependencies are installed. If any of the dependencies are missing, the script will ask the user if they would like to install them.

After the dependencies are installed, the script uses the Requests library to send an API request to the Slack API. The API request is used to create a Slack chat with the provided Jira number and tenant name.

The Slack API will process the request and return a response, which is processed by the script. If the API call was successful, the script will return a message to the user indicating that the chat was created successfully.
