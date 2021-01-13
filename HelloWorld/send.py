#!/usr/bin/env python
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
# were connected now to a broker on the local machine(locahost)

# before sending, we need to make sure the recepient queue exists.
# sending a message toa  null destination; -rmq wil drop it

channel.queue_declare(queue='hello')

# We are now ready to send a message

#(Message can never go straight to queue, Always needs to go through an exchange first.)

#default exchange with an empty string

channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='Hello World!')
print(" [x] Sent 'Hello World!'")

#to ensure are messages were actually delivered, we can close the connection
connection.close()