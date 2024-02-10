import websocket
import unittest


class TestWebSocketConnectionEcho(unittest.TestCase):
    def test_echo_websocket(self):
        ws_url = "ws://localhost:8080/echo"  # URL du serveur de test WebSocket
        message = "Hello, WebSocket!"  # Message à envoyer
        expected_response = message  # Réponse attendue du serveur

        # Créer une connexion WebSocket au serveur de test
        ws = websocket.create_connection(ws_url)
        try:
            # Envoyer le message au serveur
            ws.send(message)

            # Recevoir la réponse du serveur
            response = ws.recv()

            # Vérifier que la réponse reçue est égale au message envoyé
            self.assertEqual(response, expected_response)
        finally:
            # Fermer la connexion WebSocket
            ws.close()


if __name__ == '__main__':
    unittest.main()
