# Python-Scraper
This is a web-scraping tool that will alert subscribed users with stock updates on defined items.

# Scraping
Using Selenium, this bot will scrape multiple websites periodically, detecting whether or not the item is in stock or not.
## Supported Websites
- #### Adorama
- #### Amazon
- #### B&H Photo Video
- #### Best Buy
- #### Gamestop
- #### Sony Direct
- #### Walmart

# Human Verification
The bot will try and hide its presence on websites using many different methods.
Many websites still provide random human verification, regardless.
This is to stop botting for high-demand items that may possibly sell out quickly.
####### There are two different types of verification:
- ### Click And Hold
For this verification type, users are required to click and hold their mouse down at a specified location for a random period of time,
and must complete the process a random number of times.
These are often random, and can pop up many times when scraping the sites.

The bot handles these by detecting which website invoked the verification, and applying a brute-force method to passing it through.

###### More data will be collected, and the solution to this approach will become faster. A logarithmic approach is currently in the works.

- ### Captcha
For this verification type, users are required to click on a series of images that correspond with a given word.
Captchas are currently incapable of being solved by this bot. A solution is currently being researched.

####### These verifications happen very infrequently, if not only one time. The scraper allows the user to solve the Captcha in the beginning of the program.

# Notifications
Using the Twilio API, users are notified via text the instant the program finds that an item has just come in/gone out of stock.
Users must be subscribed to the notification system.
###### On Windows and Linux machines, if no Twilio client is stored, the message will instead print to the console and play a notification noise.

# Crontabs
This bot only sends text messages and scrapes websites at Crontabs specified times.
