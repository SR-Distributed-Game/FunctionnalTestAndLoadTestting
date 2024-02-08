import threading
import websocket
try:
    import thread
except ImportError:
    import _thread as thread
import time

def handle_message(ws):
    """Fonction pour écouter et traiter les messages reçus."""
    while True:
        message = ws.recv()
        pass


def send_message_to_websocket(url, message, interval):
    """Fonction pour envoyer un message à un WebSocket en boucle et écouter les messages reçus."""
    ws = None
    try:
        # Utilisez create_connection pour établir la connexion WebSocket
        ws = websocket.create_connection(url)

        # Créer un thread pour écouter les messages reçus
        listener_thread = threading.Thread(target=handle_message, args=(ws,))
        listener_thread.daemon = True  # Permet au thread d'être fermé lorsque le programme principal se termine
        listener_thread.start()

        while True:
            ws.send(message)
            time.sleep(interval)
    except Exception as e:
        print(f"Erreur lors de l'envoi ou de la réception du message {threading.get_ident()} : {e}")
    finally:
        if ws is not None:
            ws.close()

def create_threads(number_of_threads, url, message, interval):
    """Crée et démarre un nombre spécifié de threads pour envoyer des messages à un WebSocket."""
    threads = []
    for _ in range(number_of_threads):
        thread = threading.Thread(target=send_message_to_websocket, args=(url, message, interval))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    NUMBER_OF_THREADS = 100
    WEBSOCKET_URL = "ws://localhost:8080/game"
    INTERVAL = 1/60

    with open('./JSONMessage/Message.json', 'r') as file:
        MESSAGE = file.read()

    with open('./JSONMessage/FirstMessage.json', 'r') as file:
        FIRST_MESSAGE = file.read()

    create_threads(NUMBER_OF_THREADS, WEBSOCKET_URL, MESSAGE, INTERVAL)
