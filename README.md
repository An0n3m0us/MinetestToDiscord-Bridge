# MinetestToDiscord-Bridge

A bridge between a Minetest Server and Discord. Only works from Minetest to Discord.

![Img1](https://raw.githubusercontent.com/An0n3m0us/MinetestToDiscord-Bridge/master/image.png)

# Setting up - Linux only

Set up a [Discord Webhook](https://support.discordapp.com/hc/en-us/articles/228383668-Intro-to-Webhooks)

Download the `minetest-bridge.py` file.

Copy your webhook URL into the url variable in the Python file.

Run a minetest server then run the Python file.

# How it works

Every time the debug file updates, the script reads the new line and interprets it.
