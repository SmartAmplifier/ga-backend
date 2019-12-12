# ga-backend

Backend for Google Assistant Action to controlling `Smart Amplifier` by voice.

## Intents

### Pair new amplifier

Before you can control amplifier using Google Assistant. You must pair your amplifier to your Google Account. You can pair by by saying

    Pair new amplifier <id>

Response should looks like follow:

    You amplifier with id <id> was paired to your email

You can get your amplifier id by following [gateway tutorial](https://github.com/SmartAmplifier/gateway).

### Change your volume

You can change volume of your by saying

    Change volume to 30 %

Response should looks like:

    Volume was changed to 30 %

### Pair amplifier

You can check if your paired amplifier is what you expected by saying

    What is my paired amplifier

Response should looks like:

    Your paired amplifier id <id>