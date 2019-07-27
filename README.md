# PyProtocolsCheck
An api in python to check if you e-mail connections is working correcly, if you dns rocords is right too.

# Important details

This api is in development an in *API-PRotocolTest.py* you can see it running in debug mode, in the same file if you don't pass the server by default the class will try in umbler.com server

In *blacklistLookup.py* the main function will get the blacklists domain inside a mysql server(need be change to mongodb), after you build image change the strinmg connection to you mysql.

To build your image RUN:
 1)docker build -t protocols .
 2)docker run --name protocolsTest -p 9080:80 --dns=8.8.8.8 -d protocols
 3) Simple test: curl -X GET \
  http://YOUR-IP:9080/dns/google.com.br/MX

Enjoy.
