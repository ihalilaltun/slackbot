#-*- coding: utf-8 -*-
#!/usr/bin/env python
import os
import time
import random

from slackclient import SlackClient
import difflib

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

# starterbot's ID as an environment variable
BOT_ID = 'BOT_ID_HERE'

# constants
AT_BOT = "<@" + BOT_ID + ">"
EXAMPLE_COMMAND = "do"

# instantiate Slack & Twilio clients
slack_client = SlackClient('BOT_TOKEN_HERE')

# bot data
atar_input=['bot musun','are you','nesin','kimsin','what']
atar_output=['adam var, adam var','ben botum','sen kimsin', 'hayır sen kimsin?', 'bu köyden degilsem ne olacak', 'sen kimi tanıyon?', 'what are you?', 'are you kola?', 'bu insansa ben neyim','bot musun?','e what are you?','kardeş sen nerelisin','azını yüzüne kırarım','bana haydarı verin']

hehe_input=['hehe','he','ya he','komik',':D',';)',':)','ahahahha',':smile:']
hehe_output=['yav he', 'he tamam', 'tamam en komik sensin', 'acaip komiksiniz', 'hep böylemisiniz ya', 'hehe','he','ya he','çok komik',':D',';)',':)','ahahahha',':smile:','inş cnm ya','ne gülüyon']

cahil_input=['bilmiyorum','bilmek','bil','bileme','yapama','yapamadı','olmadı','olmuyor','zor','çok zor','sıkıldım','offfff']
cahil_output=['aç oku aç','RTFM','cahillik','yine cahillik','sana bakınca boşluk görüyorum', 'are you kola?','o kadar cahilsin ki ağlamak istiyorum','salak ya yemin ederim gerizakalı bu çocuk','aklı yok fikri var']

at_input=['ata bindin mi','at var at', 'at var','at yiyelim','at ye','at varmış']
at_output=['at olmasa gel','bidaha bin','at var at','at yiyin','|         AT          ATATATATA\n|       ATAT               AT\n|     AT     AT            AT\n|   ATAATTAT         AT\n| AT             AT        AT']

bug_input=['patladı','patlak','bug']
bug_output=['yine patlatmışınız','aç abi bi bug daha aç','buga doyduk','buga bindin mi hehehe']

lan_input=['lan']
lan_output=['lan mı?','ulan!','ayıp ayıp','lan değildir o']

baybay_input=['görüşürüz','ben çıktım','eyv','bay','siyu','see you','c ya','ben kaçtım','kaçtım','kaçıyorum']
baybay_output=['görüşürüz cnm','ben çıktım','eyv','bay','siyu','see you','c ya','siiiiyuuu canninballl','gidin ya tamam','see you on the other side brother','daha karpuz kesecektik','gitmeyin :(','çıkıyonuz mu?','sen git','ya sen git','yürü git','abi gidin ya','ne kadar güzel bir gün']

selam_input=['ordamısın','nerdesin','where are you','bot nerde','bot ayakta mı','bot online','bot açık mı','geldim','ben geldim']
selam_output=['burdayım','welcome bro','hoşgeldin hacı naptın','ooo kimler gelmiş','kardeş nerdesin','neyse','geldin mi la']

nasilsin_input=['nasılsın','nassın','naptın','nasıl gidiyor','nabyon','naber']
nasilsin_output=['naabak karşim','iyi napak','sen naptın','canım sıkkın','sürünüyoz','akıyor ;)','aşırı iyi','çoh iyi','yaaani','nabim sen naaabyon', 'sen nasılsınız inşallah']

neden_input=['neden','sebep','niye','niye ki']
neden_output=['öyle ya','hayat','sence?','ne bilim','kısmet','çünküüüü','çok düşünmemek lazım :D','bi nedeni yok']

star_wars_input=['force','obi wan kenobi','anakin','yoda','rogue one','jedi','padawan','sith','order','star wars','r2d2','bb8','k2so','han solo','princes leia','wader','it is a trap']
star_wars_output=['feel the force luke','force is strong with this one','you were my brother','I hate you!','you were supposed to bring balance','come to the dark side','When 900 years old, you reach… Look as good, you will not.','I sense great fear in you, Skywalker. You have hate… you have anger… but you don’t use them.','It\'s a trap!','These aren\'t the droids you\'re looking for...','Fear is the path to the dark side.','You were the chosen one! It was said that you would destroy the Sith, not join them.','I find your lack of faith disturbing.','Help me Obi-Wan Kenobi, you\'re my only hope.','Do or do not, there is no try']

vizontele_input=['görevin var','halkına sorumluluk','sosyal faşistler','sen delisin']
vizontele_output=['eee ona bakarsan sen de hıyarsın','cahit abe giller mi?','koccaamaan bir F düşün','görevin var','halkına sorumluluk','sosyal faşistler','sen delisin']

gunaydin_input=['günaydın']
gunaydin_output=['günaydın janım','en tatlı sabahlar çokokremle başlar','gün mü aydın']

# TODO
one_to_one_input=[{'zira':'zira mı? zira nedir?'}]

# TODO
organize_isler_input=['araba nerde','para nerde','zira']
organize_isler_output=['müşteride','yarın vericekler','zira mı? zira nedir?']

ne_kadar_input=['ne kadar','pahalı','fazla']
ne_kadar_output=['ne kadarsa o kadar','holoska + 20bin lira','senin paran yetmez','çok fazla','aşırı','azdan az çoktan çok gider','fakirlik','havan kime yabancı']

random_output=['güldürmedi','sean connery?','zira?','şimdi onlar düşünsün','bırakın gidin ya','eeee daha napyonuz']

# all data list for iterating
data = [
  {
    "name":"atar",
    "input":atar_input,
    "output":atar_output
  },
  {
    "name":"hehe",
    "input":hehe_input,
    "output":hehe_output
  },
  {
    "name":"cahil",
    "input":cahil_input,
    "output":cahil_output
  },
  {
    "name":"at",
    "input":at_input,
    "output":at_output
  },
  {
    "name":"lan",
    "input":lan_input,
    "output":lan_output
  },
  {
    "name":"baybay",
    "input":baybay_input,
    "output":baybay_output
  },
  {
    "name":"starwars",
    "input":star_wars_input,
    "output":star_wars_output
  },
  {
    "name":"selam",
    "input":selam_input,
    "output":selam_output
  },
  {
    "name":"nasilsin",
    "input":nasilsin_input,
    "output":nasilsin_output
  },
  {
    "name":"neden",
    "input":neden_input,
    "output":neden_output
  },
  {
    "name":"vizontele",
    "input":vizontele_input,
    "output":vizontele_output
  },
  {
    "name":"organize",
    "input":organize_isler_input,
    "output":organize_isler_output
  },
  {
    "name":"gunaydin",
    "input":gunaydin_input,
    "output":gunaydin_output
  },
  {
    "name":"ne_kadar",
    "input":ne_kadar_input,
    "output":ne_kadar_output
  }
]

ratioLevel=40

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

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
    #print(command, channel)
    start_time = time.time()
    if "selam" in command:
        slack_client.api_call("chat.postMessage", channel=channel,text="ve aleyküm slm", as_user=True)
    else:
        reply=getReply(command,ratioLevel,data)
        if(reply):
            slack_client.api_call("chat.postMessage", channel=channel,text=reply, as_user=True)
    #print("reply time %s seconds" % (time.time() - start_time))
	


def parse_slack_output(slack_rtm_output):
    """
        The Slack Real Time Messaging API is an events firehose.
        this parsing function returns None unless a message is
        directed at the Bot, based on its ID.
    """
    output_list = slack_rtm_output
    #print output_list
    if output_list:
        for output in output_list:
            if output and 'text' in output and not output.get("user")=='BOT_ID_HERE':
                # return text after the @ mention, whitespace removed
                return output['text'], output['channel']
    return None, None


def getReply(input,ratioLevel,data):
    biggestRatio=0
    reply=None
    for item in data:
        for elm in item["input"]:
    	    newRatio=difflib.SequenceMatcher(a=input.lower(),b=elm.lower()).ratio()*100
    	    if(newRatio>biggestRatio):
    	        biggestRatio=newRatio
    	        matchName = item["name"] + ' - ' + elm
    	        reply=random.choice(item["output"])
    #print biggestRatio
    
    if biggestRatio >= ratioLevel:
        #print "Matched with : " + matchName + " with ratio " + str(biggestRatio) + " - reply : " + reply
    	return reply
    else:
        #print "Not matched"
    	return False

if __name__ == "__main__":
    READ_WEBSOCKET_DELAY = 0.5 # 1 second delay between reading from firehose
    if slack_client.rtm_connect():
        print("BOT connected and running!")
	#slack_client.api_call("chat.postMessage", channel='C4PDQCX0U',text="I AM ALIVEEEEEE", as_user=True)
        while True:
            #print(slack_client.rtm_read())
            command, channel = parse_slack_output(slack_client.rtm_read())
            if command and channel:
		#print command , channel
                handle_cmd(command, channel)
            time.sleep(READ_WEBSOCKET_DELAY)
    else:
        print("Connection failed. Invalid Slack token or bot ID?")

