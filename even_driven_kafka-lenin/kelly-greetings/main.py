import time
import random
from confluent_kafka import Producer

producer_config = {
    'bootstrap.servers': 'kafka-broker:9092',  
    'client.id': 'auth-service',  
}
producer = Producer(producer_config)
messages = [
    "Hola, soy Kelly :3",
    "Hello, i'm Kelly",
    "Cómo estás? --- Kelly",
    "How are you?  +++ kelly"
]

def send_random_message():
    try:
        while True:
            message = random.choice(messages)
            
            producer.produce('univalle-ideas', key=None, value=message)
            print(f"Enviado: {message}")
            
            producer.flush()
            
            # Espera 5 segundos antes de enviar el siguiente mensaje
            time.sleep(5)
    except KeyboardInterrupt:
        print("\nProceso detenido por el usuario.")
    except Exception as error:
        print(f"Error al enviar mensaje a Kafka: {error}")

send_random_message()
