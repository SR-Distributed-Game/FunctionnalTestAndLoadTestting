import json

import websocket
import unittest

class TestWebSocketConnectionGame(unittest.TestCase):
    def test_1_game_websocketConnection(self):

        ws_url = "ws://localhost:8080/game"
        message = """{"Type":"ConnectSucces","ClientID":-1,"Metadata":{"playername":"OUAIIIIIIIS"},"RoomID":-1}"""
        ws = websocket.create_connection(ws_url)
        try:
            ws.send(message)
            response = ws.recv()

            response_data = json.loads(response)
            response_data["Metadata"]["clientID"] = "DYNAMIC"

            modified_response = json.dumps(response_data, sort_keys=True)

            print(modified_response)

            expected_response_data = json.loads("""{"Type":"ConnectSucces","Metadata":{"clientID": "DYNAMIC"},"ClientId":"-2","RoomId":"-1"}""")
            expected_response = json.dumps(expected_response_data, sort_keys=True)
            self.assertEqual(modified_response, expected_response)
        finally:
            ws.close()

    def test_2_game_websocketJoinRoom(self):

        ws_url = "ws://localhost:8080/game"
        message = """{"Type":"JoinRoom","ClientID":0,"Metadata":{"clientID":0},"RoomID":-1}"""
        ws = websocket.create_connection(ws_url)
        try:
            ws.send(message)
            response = ws.recv()

            response_data = json.loads(response)
            response_data["Metadata"]["players"] = "DYNAMIC"

            modified_response = json.dumps(response_data, sort_keys=True)

            expected_response_data = json.loads("""{"Type":"JoinRoom","Metadata":{"leaderboard":{"0":0},"players": "DYNAMIC"},"ClientId":"-2","RoomId":"-1"}""")
            expected_response = json.dumps(expected_response_data, sort_keys=True)

            print(response)
            self.assertEqual(modified_response, expected_response)
        finally:
            ws.close()


    def test_3_game_websocketMovePlayer(self):
        ws_url = "ws://localhost:8080/game"
        message = """{"Type":"UpdateObject","ClientID":0,"Metadata":{"objectData":{"transform":{"position":{"x":572.2338528885318,"y":783.5543260455736},"scale":{"x":20,"y":20},"rotation":0},"futurtransform":{"position":{"x":572.2338528885318,"y":783.5543260455736},"scale":{"x":20,"y":20},"rotation":0},"name":"Payll","id":107,"tag":"player","points":0,"speed":0.2,"hasBeenEaten":false,"clientID":0,"Type":"player"}},"RoomID":-1}"""
        ws = websocket.create_connection(ws_url)
        try:
            ws.send(message)
            response = ws.recv()
            print(response)
            # Analyser la réponse JSON
            response_data = json.loads(response)

            # Modifier les éléments dynamiques pour les standardiser avant la comparaison
            response_data["Metadata"]["objectData"]["id"] = "DYNAMIC"  # Standardiser l'ID
            # Pour la position, vous pouvez choisir de la standardiser si son exactitude n'est pas critique
            response_data["Metadata"]["objectData"]["transform"]["position"]["x"] = "DYNAMIC"
            response_data["Metadata"]["objectData"]["transform"]["position"]["y"] = "DYNAMIC"

            # Convertir à nouveau en chaîne JSON pour la comparaison
            modified_response = json.dumps(response_data, sort_keys=True)
            print(modified_response)
            expected_response_data = json.loads(
                """{"ClientId": "-2", "Metadata": {"objectData": {"SerializationTest": "TEST FOR SERIALIZATION", "Type": "fruit", "id": "DYNAMIC", "lifeTime": 1, "name": "fruit", "tag": "fruit", "transform": {"position": {"x": "DYNAMIC", "y": "DYNAMIC"}, "rotation": 0, "scale": {"x": 10, "y": 10}}}}, "RoomId": "-1", "Type": "SpawnObject"}""")
            expected_response = json.dumps(expected_response_data, sort_keys=True)

            self.assertEqual(modified_response, expected_response)
        finally:
            ws.close()
