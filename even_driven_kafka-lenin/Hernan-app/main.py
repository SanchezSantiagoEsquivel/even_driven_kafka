import time
import random
from confluent_kafka import Producer

# Configuración del productor
producer_config = {
    'bootstrap.servers': 'kafka-broker:9092',
    'client.id': 'my-service',
}

producer = Producer(producer_config)

# Mensajes personalizados
messages = [
    "👋 ¡Hola, soy Hernan, estoy desde mi microservicio! 👋",
    "🎉 ¡Microservicio activo! 🎉",
    "🚀 Kafka es genial 🚀",
    "📡 Mensaje desde Kubernetes 📡",
    "🌟 ¿Listos para más mensajes? 🌟"
]

def send_random_message():
    try:
        while True:
            # Selecciona un mensaje aleatorio
            message = random.choice(messages)
            
            # Produce el mensaje en el tópico de Kafka
            producer.produce('univalle-ideas', key=None, value=message)
            print(f"Enviado: {message}")
            
            # Asegura que se haya enviado el mensaje
            producer.flush()
            
            # Espera 5 segundos antes del próximo mensaje
            time.sleep(5)
    except KeyboardInterrupt:
        print("\nProceso detenido por el usuario.")
    except Exception as error:
        print(f"Error al enviar mensaje a Kafka: {error}")

# Inicia el envío de mensajes
send_random_message()
