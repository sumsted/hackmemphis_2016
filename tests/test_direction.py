from unittest import TestCase

import requests


class TestDirection(TestCase):
    URL = "http://localhost:8085/alexa/event"

    def test_east(self):
        request = {
            "session": {
                "user": {
                    "userId": "amzn1.ask.account.AEEJPMHKHF2DINXCST2H3GAKEG5H5V2JCO6WH5PULVUYQ7PHPDNC2I6VORS4FG2YJ3TJDUOCCFWZYVBDIRHAINSQG2MRVZKJMA7GY3SKGPUHR6ZRQAFGXD5FMOKBFVJWHF4YSYBJBPIWUP76LLSW47AC6JUVPO4Q3QDMYBGRUXWNHUID73T4L54HUHPYEJESTNKP24XHXYUQVVY"
                },
                "application": {
                    "applicationId": "amzn1.ask.skill.ceccea0b-f170-4541-b01c-a054a9a5676b"
                },
                "sessionId": "amzn1.echo-api.session.77430aad-380e-4b0c-aae7-184850c32e1d",
                "new": False
            },
            "context": {
                "AudioPlayer": {
                    "playerActivity": "IDLE"
                },
                "System": {
                    "user": {
                        "userId": "amzn1.ask.account.AEEJPMHKHF2DINXCST2H3GAKEG5H5V2JCO6WH5PULVUYQ7PHPDNC2I6VORS4FG2YJ3TJDUOCCFWZYVBDIRHAINSQG2MRVZKJMA7GY3SKGPUHR6ZRQAFGXD5FMOKBFVJWHF4YSYBJBPIWUP76LLSW47AC6JUVPO4Q3QDMYBGRUXWNHUID73T4L54HUHPYEJESTNKP24XHXYUQVVY"
                    },
                    "application": {
                        "applicationId": "amzn1.ask.skill.ceccea0b-f170-4541-b01c-a054a9a5676b"
                    },
                    "device": {
                        "supportedInterfaces": {
                            "AudioPlayer": {}
                        }
                    }
                }
            },
            "version": "1.0",
            "request": {
                "locale": "en-US",
                "timestamp": "2016-09-25T00:47:14Z",
                "intent": {
                    "slots": {
                        "direction": {
                            "value": "east",
                            "name": "direction"
                        }
                    },
                    "name": "navigateIntent"
                },
                "requestId": "amzn1.echo-api.request.ef7a5205-f274-4c64-acca-8328ae3e94ff",
                "type": "IntentRequest"
            }
        }

        response = requests.post(self.URL, json=request)

        print('east: %s' % str(response.json()))
        self.assertTrue('outputSpeech' in response.json()['response'])
        self.assertTrue('card' in response.json()['response'])
