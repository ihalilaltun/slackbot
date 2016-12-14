#-*- coding: utf-8 -*-
import os
import time
from slackclient import SlackClient


# starterbot's ID as an environment variable
BOT_ID = 'U3FA0RB71'

# constants
AT_BOT = "<@" + BOT_ID + ">"
EXAMPLE_COMMAND = "do"

# instantiate Slack & Twilio clients
slack_client = SlackClient('YOUR ID HERE')


def handle_command(command, channel):
    """
        Receives commands directed at the bot and determines if they
        are valid commands. If so, then acts on the commands. If not,
        returns back what it needs for clarification.
    """
    response = "Not sure what you mean. Use the *" + EXAMPLE_COMMAND + \
               "* command with numbers, delimited by spaces."
    if command.startswith(EXAMPLE_COMMAND):
        response = "Sure...write some more code then I can do that!"
    slack_client.api_call("chat.postMessage", channel=channel,
                          text=response, as_user=True)

def handle_cmd(command, channel):
    print(command, channel)
    if "selam" in command:
        slack_client.api_call("chat.postMessage", channel=channel,text="ve aleyküm slm", as_user=True)
    elif "autoflowbot" in command:
        slack_client.api_call("chat.postMessage", channel=channel, text="Çooook yakında yeni cevaplarım ile aranızdayım", as_user=True)
    else:
        pass


def parse_slack_output(slack_rtm_output):
    """
        The Slack Real Time Messaging API is an events firehose.
        this parsing function returns None unless a message is
        directed at the Bot, based on its ID.
    """
    output_list = slack_rtm_output
    if output_list:
        for output in output_list:
            if output and 'text' in output:
                # return text after the @ mention, whitespace removed
                return output['text'], \
                       output['channel']
    return None, None


if __name__ == "__main__":
    READ_WEBSOCKET_DELAY = 1 # 1 second delay between reading from firehose
    if slack_client.rtm_connect():
        print("BOT connected and running!")
        while True:
            #print(slack_client.rtm_read())
            command, channel = parse_slack_output(slack_client.rtm_read())
            if command and channel:
                handle_cmd(command, channel)
            time.sleep(READ_WEBSOCKET_DELAY)
    else:
        print("Connection failed. Invalid Slack token or bot ID?")
