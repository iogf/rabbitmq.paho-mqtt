##############################################################################
cd /home/tau/projects/rabbitmq.ws.example-code/
# clean up all .pyc files. 
find . -name "*.pyc" -exec rm -f {} \;
##############################################################################
cd /home/tau/projects/rabbitmq.paho-mqtt-code
git status
git add *
git commit -a
git push 

# enable the plugin.
sudo rabbitmq-plugins enable rabbitmq_stomp
##############################################################################



