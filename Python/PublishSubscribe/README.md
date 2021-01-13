Publish/subscribe pattern is delivering a message to multiple consumers.

Buidling a logging system. 1 program will transmit the message, and the second will receive and print the messages.
Every running copy of the receiver program will get the message.
* 1 receiver will direct the logs to disk
* 2nd receiver will print the logs to the screen.
 **Published log messages are going to be broadcast to all receivers.**

#### Exchanges
Before we used a queue, this tutorial will use the full rabbitmq message model.
* A producer is a user app that sends messages.
* A queue is a buffer that stores messages.
* A consumer is a user app that receives messages.

**Prodcer will never send any messages directly to a queue**. 
* In fact a producer doesn't know if amessage will be delvered to any queue at all.

Prodcuers instead send messages to the exchange. 
Exchange input is messages from producers, and output is different queues

Exchange does 1 of 3 things
* Append it to a singular queue
* Append it to many queues
* Discard message.
**rules defined by exchange type**

#### Four exchange types
1. Direct
2. Headers
3. Fanout (broadcast)
4. Topic

Fanout will broadcast all messages it receives to **all** the queues it knows
![alt text](https://github.com/jbollman7/rabbitmq-training/blob/master/Python/PublishSubscribe/PS0.png)
Creating an exchange called logs
`
channge.exchange_declare(exchange='logs', exchange_type='fanout')
`


1. When we connect to RabbitMQ we need a fresh, empty queue. Having the server choose a random queue name is best
`
result = channel.queue_declare(queue='')
`
result.method.queue cotains a random queue name
2. Once the consumer conenction is closed, the queue should be deleted. Use the exclusive flag
`
result = channel.queue_declare(queue'=', exclusive=True)
`

#### Bindings
We've already created a fanout exchange and a queue. Now we need to tell the exchange to send messages to our queue
The relationship between exchange and a queue is called a binding


#### Putting it all together
The most important chagne is that we publish messages to our logs exchange instead of the nameless one. We are required to supply a routing_key when sending
but its value is ignored for fanout exchanges
![alt-text](https://github.com/jbollman7/rabbitmq-training/blob/master/Python/PublishSubscribe/PS5.png)
`
channel.queue_bind(exchange='logs', queue=result.method.queue)
`
Our logs exchange will append messages to our queue

use `rabbitmqctl list_bindings` to verify that the code actually creates bindings and queues as we want.
