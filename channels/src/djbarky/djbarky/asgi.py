"""
ASGI config for djbarky project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""
#add redis in windows
# 1. https://learn.microsoft.com/en-us/windows/wsl/install    wsl --install     default Ubuntu
# 2. open ubuntu      https://learn.microsoft.com/en-us/windows/wsl/setup/environment#set-up-your-linux-username-and-password
# 3. windows powershell:  
#     i. ubuntu

#     ii. https://redis.io/docs/latest/operate/oss_and_stack/install/install-redis/install-redis-on-linux/#install-on-ubuntu-debian

#     curl -fsSL https://packages.redis.io/gpg | sudo gpg --dearmor -o /usr/share/keyrings/redis-archive-keyring.gpg
#     echo "deb [signed-by=/usr/share/keyrings/redis-archive-keyring.gpg] https://packages.redis.io/deb $(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/redis.list
#     sudo apt-get update
#     sudo apt-get install redis

#     iii. start server:  sudo service redis-server start
# ? didn't work...hmmmm
#     iv. add docker? first...? -> then windows powershell then run redist stack in docker and connect to redis cli


#     https://redis.io/docs/latest/operate/oss_and_stack/install/install-stack/docker/

#     docker run -d --name redis-stack -p 6379:6379 -p 8001:8001 redis/redis-stack:latest
#     needs docker?  docker, podman, or docker.io?  -> trying sudo snap install docker
#     docker run -d --name redis-stack -p 6379:6379 -p 8001:8001 redis/redis-stack:latest
# does not work ...permission denied


# # try this again:  sudo service redis-server start....not sure?


# https://www.youtube.com/watch?v=_nFwPTHOMIY&t=683s  -> this did not work, doesn't recognize sudo...ughhahahah

# ?turn windows feature on/off
# check.... window subsystem for linux
# ...already have ubuntu    20.04lts -chosen...? i don't know what version i have
# ls -al

# sudo apt-add-repository ppa:/redislabs/redis

# sudo apt-get update
# sudo apt-get upgrade

# sudo apt-get install redis-server
# redis-server --version
# redis-server

# open ubuntu:  ping
#     lolwut


# to run in bakground sudo service redis-server start...? 
# sudo service redis-server stop


# powershell -> ubuntu -> sudo service redis server start -> test ping -> open vsc 2 bash ->  source venv/Scripts/activate  for both

#left test 
#right worker ->  cd channels/src/djbarky        $ ./manage.py runworker
#error no module daphne  -> install..but why..what didn't i do before...
#https://channels.readthedocs.io/en/latest/installation.html
#https://pypi.org/project/channels-redis/
# $ ./manage.py runworker bookmarks-add

#./manage.py test  barkyarch.tests.TestCommands


#tried to restart this...redis: unrecognized service...resdis server version present...

import os

from channels.routing import ChannelNameRouter, ProtocolTypeRouter
from django.core.asgi import get_asgi_application

from barkyapi import consumers
#add to read all settings
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djbarky.settings")

barky_asgi_app = get_asgi_application()

# for channels support   
#notification pub/sub 
application = ProtocolTypeRouter(
    {
        "http": barky_asgi_app, #any name
        "channel": ChannelNameRouter(
            {
                "bookmarks-add": consumers.SimpleBookmarkConsumer.as_asgi(),
                "bookmarks-edit": consumers.SimpleBookmarkConsumer.as_asgi(),
            }    #channel name : consumer type   #? can you keep adding these?
        ),
    }
)

#external message bus 
