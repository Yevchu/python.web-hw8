from models import Contact
import pika
import time
import json
import connect

credentials = pika.PlainCredentials('guest', 'guest')
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost', port=5672, credentials=credentials))
channel = connection.channel()

channel.queue_declare(queue='message_delivere', durable=True)
print(' [*] Waiting for messages. To exit press CTRL+C')    

def callback(ch, method, properties, body):
    message = json.loads(body.decode())
    contact = Contact.objects(id=message.get('id'))
    contact.update(delivered=True)
    print(f" [{message.get('id')}] Received: {message.get('message')}")
    time.sleep(0.1)
    print(f" [{message.get('id')}] Done: {method.delivery_tag}")
    ch.basic_ack(delivery_tag=method.delivery_tag)


channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue='message_delivere', on_message_callback=callback)


if __name__ == '__main__':
    channel.start_consuming()