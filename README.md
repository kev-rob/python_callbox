# Callbox for Messaging Applications <a href="https://www.buymeacoffee.com/kevinrobert"> <img align="right" src="https://storage.googleapis.com/www-trabant-tech-com/BuyMeACoffee.png"></a>

A modern alternative to ringing a bell for service, this callbox application alerts **Slack** or **Google Chat** when a person presses a button for help.  

This Python application was originally written to run on a Raspberry Pi with an attached touchscreen to request support at an IT Help Desk. The following videos demonstrate this type of implementation, interacting with the respective messaging applications via iPad.

**Slack:** https://youtu.be/wFE2QAVsd6c

**Google:** https://youtu.be/0p94PBY21JU  

## 

![Screen](https://storage.googleapis.com/www-trabant-tech-com/Screen%20Shot%202022-05-06%20at%202.37.02%20PM.png)  

## Installation

Download **python_callbox** to the location you would like to run the application.  
  
```
git clone "https://github.com/kev-rob/python_callbox.git"
```

Navigate to the root of the **python_callbox** folder and install the requirements.  
  
   
```
cd python_callbox/  
pip3 install -r requirements.txt
``` 

To run the application, from  the root of the **python_callbox** folder execute the following command:
  
   
```
python3 main.py
``` 

## Configuration

To integrate **python_callbox** into your messaging application, you will first need to create a webhook and paste it into **weboook.py**. You can follow the tutorials provided by each vendor to create the webhook. Other applications that receive webhooks may also work with **python_callbox** but they have not been tested.

It is recommended to create a dedicated Channel (Slack) or Space (Google) for **python_callbox** to send its alerts.

### Slack  
Follow this tutorial from Slack to create your webhook:  

https://api.slack.com/messaging/webhooks

### Google  

The following information is available at https://developers.google.com/chat/how-tos/webhooks

> Define an incoming webhook
>
> From the chat space menu:
>
> 1. Select Manage webhooks. A dialog appears that lists any incoming webhooks already defined for the space.
> 2. If this is the space's first webhook, you are prompted to provide a webhook name and avatar URL. If the space already has webhooks, click Add another.
> 3. Fill in the name field and optionally the avatar URL field.  
> 4. Click SAVE.
>
> Copy and save the webhook URL
>
> From the Manage webhooks modal, find your webhook and click the copy icon to copy the webhook URL.
>
> Save this URL in your app's source code or configuration so that it can be used as a message destination.  

## Customization

### Images
Replace our **banner.png** and **logo.png** files with your own banner.png and logo.png files. Banner.png is the wordmark image in the upper left of the screen and logo.png is the icon/button in the center of the screen. Image sizes should be adjusted based on screen size. It is recommended to start with a banner.png of 100px height and a logo.png that is 50px x 50px.

### On-Screen Text  
The on-screen text can be customized in **main.py**. **help_text1** and **help_text2** are on screen when the callbox application is ready. **cancel_text** is on-screen after help has been requested until someone cancels the request for help.

### Message Text
The text sent to the messaging application via webhook is stored in the **data** section of **_request.py** for the help request message and **_cancel.py** for the help request cancel message.

## 

![Coffee](https://storage.googleapis.com/www-trabant-tech-com/BuyMeACoffee.png)
