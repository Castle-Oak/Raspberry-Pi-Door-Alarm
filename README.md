# Raspberry Pi Door Alarm

This is an example of a door alarm written in Python on Raspberry Pi. 

### Installation
- Copy alarm.py to the pi's home directory.
- Add your Pushover API creds to AWS SecretsManager. Replace TOKEN and USER_KEY with the token and user key from Pushover. Take note of the ARN. You'll need this to start the script. 
```aws secretsmanager create-secret --name api_key --secret-string "{\"token\": \"TOKEN\",\"user\": \"USER_KEY\"}"```
- Open crontab. 
```crontab -e```
- Add the following line to your crontab. Replace $SECRET_ARN with the name of the secret in AWS SecretsManager.
```@reboot sleep 120 && python3 /home/pi/alarm.py $SECRET_ARN >> /home/pi/alarm.log 2>&1```

### Software
- A Raspberry Pi with Rasbian Lite installed
- Network connectivity
- Python3
- The follwing Python modules: boto3, gpiozero
- AWS SecretsManager (To store Pushover API credentials)

### Hardware
- [Magnetic Reed Switch](https://www.amazon.com/Directed-Electronics-8601-Magnetic-Switch/dp/B0009SUF08/) 
- Raspberry Pi Zero, Raspberry Pi 2 or better
- Soldering Eequipment (Iron, Solder, thin guage wire)

Solder the the leads from the magnetic reed switch to GPIO2 and ground, polarity is not important.

<img src="https://raw.githubusercontent.com/pmgcrypto/Raspberry-Pi-Door-Alarm/master/3.png" width=50%>
