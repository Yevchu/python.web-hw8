from faker import Faker
from models import Contact
import connect
import pika
import json


fake = Faker()

for _ in range(1, 27):
    contact = Contact(name=fake.name(), email=fake.email()).save()

credentials = pika.PlainCredentials('guest', 'guest')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost', port=5672, credentials=credentials))
channel = connection.channel()

channel.exchange_declare(exchange='messages', exchange_type='direct')
channel.queue_declare(queue='message_delivere', durable=True)
channel.queue_bind(exchange='messages', queue='message_delivere')


def main():
    contact = Contact.objects().all()
    for el in contact:
        message = {
            'id': str(el.id),
            'message': 'Hello, you have a new message'
        }

        channel.basic_publish(
            exchange='messages',
            routing_key='message_delivere',
            body=json.dumps(message).encode(),
            properties=pika.BasicProperties(
            delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE
            ))
    connection.close()

if __name__ == "__main__":
    main()