### Work Queues aka Task Queues
Work queues allow us to take resource-intensive task, and schedule taks to be done later. Thig gives us asynchronous. Before we would have to wait for th task to complete.

Bundling the task as a message and send it to the queue.
The worker process will pop the tasks from the queue and execute the job.
####When you run many workers, the tasks will be shared between them.

This is useful for web applications

We will mock that we are busy by using the sleep function.

#### Round-robin dispatching

The task Queue allows us to parallelise work. If the backlog of work is building up, we can easily add more workers.

Open up three consoles, two will run worker.py scripts, these are the consumers
shell1

python worker.py

 `# => [*] Waiting for messages. To exit press CTRL+C
`

shell2

python worker.py

 `# => [*] Waiting for messages. To exit press CTRL+C
`
In the third shell, we will publish new tasks. 
`python new_task.py First message.`
`python new_task.py Second message..`
`python new_task.py Third message...`
`python new_task.py Fourth message....`
`python new_task.py Fifth message.....`

Looking back at shell 1 and 2 workers
shell1
`
`# => [*] Waiting for messages. To exit press CTRL+C
`# => [x] Received 'First message.'
`# => [x] Received 'Third message...'
`# => [x] Received 'Fifth message.....'
`
shell2
`
`# => [*] Waiting for messages. To exit press CTRL+C
`# => [x] Received 'Second message..'
`# => [x] Received 'Fourth message....'
`

#### WHen RMQ delivers message to aconsumer, it immediately marks it for deletion.
If a worker does/killed we will lose the message it was processing. 
Messages that were delivered to the worker but not completed are also lost

Message acknowledgmemnts solves this problem. A RMQ consumer will send an acknowledgment that the message had been
received, processed and that RabbitMQ can delete it.

If a consumer dies before sending an acknowledgement, RabbitMQ will know the message wasn't processed and will re-queue it.

#### Message Durability
Message acks mean that the message does not get lost, but if the server goes down, the messages will be lost
Marking both the queue and the messages as durable

* RabbitMQ doesn't allow you to redefine an existing queue. You must declare a new named queue

Mark queues durable and messages persistent. Then RabbitMQ can crash/reboot without losing messages