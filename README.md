# NorthernLights
This python application uses a gmail robot to send an email reminder to subscribers when the northern lights reach Stockholm.

The target environment when I made this was my Raspberry pi 2 model B running raspbian 8.

# Why?
My ex gf heard that under some certain weather conditions it's possible to see the Northern Lights in Stockholm so I made her this app. For me personally, I will remember this system mostly because it was responsible for waking me up a number of times. It sent her emails at around 02:00 AM in the morning saying that the kp index was enough to reach us and she rushed out of bed to go outside and look up at the sky.

How to
------
Step 1. Create a gmail account and add the account info to the file "Settings.txt" (RobotGmailUsername and RobotGmailPassword). This account will send out email notifications.

Step 2. Add your own email in the file "Settings.txt" (AdminEmail)
    This email adress will receive potential error messages and such.
    
Step 3. Add one or more subscriber email adresses in the "Subscribers.txt" file.

Step 4. Run the script "InstallPythonDependencies.bash". Press "y" if prompted.

Step 5. Set up a cronjob or scheduled task that runs "RSSReminders.py".

___

Please send me a message if you have any questions or feedback :)
