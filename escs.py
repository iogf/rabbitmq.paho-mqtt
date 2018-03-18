##############################################################################
tee >(stdbuf -o 0 python -i)
quit()
##############################################################################

import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

channel = connection.channel()

channel.queue_declare(queue='World')

channel.basic_publish(exchange='',
                      routing_key='World',
                      body='Good')

print(" [x] Sent 'Hello World!'")

connection.close()
##############################################################################
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='chat')

def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)

channel.basic_consume(callback,
                      queue='chat',
                      no_ack=False)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()

##############################################################################

import time
import sys

import stomp

class MyListener(stomp.ConnectionListener):
    def on_error(self, headers, message):
        print('received an error "%s"' % message)
    def on_message(self, headers, message):
        print('received a message "%s"' % message)

conn = stomp.Connection()
conn.set_listener('', MyListener())
conn.start()
conn.connect('guest', 'guest', wait=True)

conn.subscribe(destination='/queue/alpha', id=1, ack='auto')

# conn.send(body='some message.', destination='/queue/alpha')

time.sleep(2)
conn.disconnect()
##############################################################################
# paho example mqtt.

import paho.mqtt.client as mqtt

def on_connect(client, userdata, rc):
    print('connected')
    client.subscribe("beta")

def on_message(client, userdata, msg):
    print(msg)

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("127.0.0.1", 15675, 10)

client.loop_forever()

client.loop_start()


##############################################################################

import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe('beta')
    client.publish('beta', 111, 0, False)

def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("127.0.0.1", 15675, 60)

client.loop_forever()



