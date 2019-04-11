import pika

credentials = pika.PlainCredentials('guest', 'guest')
connection  = pika.BlockingConnection( pika.ConnectionParameters('rabbit', 5672, '/', credentials, socket_timeout=300) )

channel = connection.channel()

channel.queue_declare( queue='sample_test', durable=True )

def callback(channel, method, properties, body):
    print( ' [x] Received %r ' % body )

channel.basic_consume( 'sample_test', callback, True)

print( ' [*] Waiting for messages. To exit press CTRL+C ' )
channel.start_consuming()
