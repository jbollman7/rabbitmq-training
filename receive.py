#!/usr/bin/env python
import pika, sys, os

def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    # were connected now to a broker on the local machine(locahost)

    # before sending, we need to make sure the recepient queue exists.
    # sending a message toa  null destination; -rmq wil drop it
    # we are making two queues. we COULD only need one, but only if we can ensure send.py runs first. By declaring two, we ensure that  a
    # queue will exist.
    channel.queue_declare(queue='hello')

    #callback funcion is necessary to receive mssages from a queue

    def callback(ch, method, properties, body):
        print(" [x] Received %r" % body)

    # next tell rmq that the function above, should receive messages from the hello queue

    channel.basic_consume(queue='hello', auto_ack=True, on_message_callback=callback)
    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)

