import threading
import websocket
try:
    import thread
except ImportError:
    import _thread as thread
import time

def send_message_to_websocket(url, message, interval):
    """Fonction pour envoyer un message à un WebSocket en boucle."""
    ws = None
    try:
        # Utilisez create_connection pour établir la connexion WebSocket
        ws = websocket.create_connection(url)
        while True:
            ws.send(message)
            print(f"Message envoyé - " + str(threading.get_ident()))
            time.sleep(interval)
    except Exception as e:
        print(f"Erreur lors de l'envoi du message : {e}")
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
    NUMBER_OF_THREADS = 1
    WEBSOCKET_URL = "ws://localhost:8080/game"
    INTERVAL = 1000
    MESSAGE = """{"Type": "UpdateObject","ClientID": 0,
  "Metadata": {
    "objectData": {
      "transform": {
        "position": {
          "x": 165,
          "y": 100
        },
        "scale": {
          "x": 20,
          "y": 20
        },
        "rotation": 0
      },
      "name": "Lumi",
      "id": 3,
      "points": 0,
      "speed": 5,"clientID": 0,"Type": "player"}},"RoomID": -1}"""
    FIRST_MESSAGE = """{"Type":"SpawnObject","ClientID":0,"Metadata":{"objectData":{"transform":{"position":{"x":439.24161345001585,"y":169.02882205513788},"scale":{"x":10,"y":10},"rotation":134.76369761864186},"name":"fruit","id":-1,"SerializationTest":"","Type":"fruit"}},"RoomID":-1}"""

    create_threads(NUMBER_OF_THREADS, WEBSOCKET_URL, MESSAGE, INTERVAL)
