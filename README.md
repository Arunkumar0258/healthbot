# Healthbot - A medical diagnosis agent
This project aims to create an AI conversational agent to treat patients by giving them medical information and prescriptions when needed. It is built on top of the Rasa Stack and uses the Infermedica API to diagnose patients.

## Usage
To train the bot interactively, Run `train_core_interactive.py`

To make the Bot run on Facebook Messenger, follow the below steps.
* Go to Facebook Developers Page using this [link](https://developers.facebook.com/)
* Sign up and create a FB Messenger App Page.
* Configure the Messages Webhooks for your newly created app.
* Get the webhook verification name and store it in system variable as `FB_VERIFY`, Secret Key as `FB_BOT_SECRET`
and Page access token as `FB_PAGE_ACCESS_TOKEN`
* To run bot in Facebook, Just run `run_dialouge.py`

## Tasks to perform
* Interface better with Infermedica API to answer followup questions.
* Add more features to make chatbot interesting.
