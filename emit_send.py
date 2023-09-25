# See Hello World! Example at
# https://www.rabbitmq.com/tutorials/tutorial-one-python.html

import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost"))
channel = connection.channel()

channel.queue_declare(queue="hello")

message = "Welcome to the gueue."

channel.basic_publish(exchange="", routing_key="hello", body="Hello World!")
print(" [x] Sent 'Welcome to the gueue.'")
connection.close()
