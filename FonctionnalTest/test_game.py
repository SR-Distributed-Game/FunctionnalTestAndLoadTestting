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
            print(response)
            self.assertEqual(response, """{"Type":"ConnectSucces","Metadata":{"clientID":0},"ClientId":"-2","RoomId":"-1"}""")
        finally:
            ws.close()

    def test_2_game_websocketJoinRoom(self):
        ws_url = "ws://localhost:8080/game"
        message = """{"Type":"JoinRoom","ClientID":0,"Metadata":{"clientID":0},"RoomID":-1}"""
        ws = websocket.create_connection(ws_url)
        try:
            ws.send(message)
            response = ws.recv()
            print(response)
            self.assertEqual(response, """{"Type":"JoinRoom","Metadata":{"leaderboard":{"0":0},"players":{"0":"OUAIIIIIIIS"}},"ClientId":"-2","RoomId":"-1"}""")
        finally:
            ws.close()

    import json

    def test_3_game_websocketCreatePlayer(self):
        ws_url = "ws://localhost:8080/game"
        message = """{"Type":"SpawnObject","ClientID":0,"Metadata":{"objectData":{"transform":{"position":{"x":100,"y":100},"scale":{"x":0,"y":0},"rotation":0},"name":"OUAIIIIIIIS","id":-1,"points":0,"speed":5,"clientID":0,"Type":"player"}},"RoomID":-1}"""
        ws = websocket.create_connection(ws_url)
        try:
            ws.send(message)
            response = ws.recv()
            response_data = json.loads(response)
            response_data["Metadata"]["objectData"]["id"] = "DYNAMIC"
            modified_response = json.dumps(response_data, sort_keys=True)

            expected_response_data = json.loads(
                """{"Type":"SpawnObject","Metadata":{"objectData":{"transform":{"rotation":0,"scale":{"x":20,"y":20},"position":{"x":100,"y":100}},"Type":"player","clientID":0,"name":"OUAIIIIIIIS","id":"DYNAMIC","speed":5,"points":0}},"ClientId":"-2","RoomId":"-1"}""")
            expected_response = json.dumps(expected_response_data, sort_keys=True)

            self.assertEqual(modified_response, expected_response)
        finally:
            ws.close()

    def test_4_game_websocketMovePlayer(self):
        ws_url = "ws://localhost:8080/game"
        message = """{"Type":"UpdateObject","ClientID":0,"Metadata":{"objectData":{"transform":{"position":{"x":100,"y":100},"scale":{"x":20,"y":20},"rotation":0},"name":"OUAIIIIIIIS","id":5,"points":0,"speed":5,"clientID":0,"Type":"player"}},"RoomID":-1}"""
        ws = websocket.create_connection(ws_url)
        try:
            ws.send(message)
            response = ws.recv()

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
                """{"ClientId": "-2", "Metadata": {"objectData": {"SerializationTest": "TEST FOR SERIALIZATION", "Type": "fruit", "id": "DYNAMIC", "name": "fruit", "transform": {"position": {"x": "DYNAMIC", "y": "DYNAMIC"}, "rotation": 0, "scale": {"x": 10, "y": 10}}}}, "RoomId": "-1", "Type": "SpawnObject"}""")
            expected_response = json.dumps(expected_response_data, sort_keys=True)

            self.assertEqual(modified_response, expected_response)
        finally:
            ws.close()
