# AzureGPTChatbot
Flask-based Python chatbot application server optimised for use with Azure.

**Project Contents**

- templates/index.html - very basic front-end HTML
- requirements.txt - necessary for our deployment to Azure later
- training/index - necessary to give our script somewhere to store the trainings it generates
- docs/ - container for the training data prepared at Step 2 (I have a test file in there stating a random - probably untrue - fact about Martians).

**Summary**

As a quick summary, you can download this repository locally load training documents into the docs folder, insert your own API Key for OpenAI in app.py, and then run app.py locally using:

  *python app.py train*

in your terminal.

For a more detailed walkthrough including on training the model and deployment to a free public Azure server, please see the following Medium article:
