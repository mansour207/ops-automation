import requests


class AuthManager:

    def __init__(self, instance_name, username, password):
        self.instance_name = instance_name
        self.username = username
        self.password = password

    def login(self):
        """get access token

        Args:
            instance_name (string): instance name
            username (string): username as email
            password (string): password

        Returns:
            string: access token
        """

        url = "https://" + self.instance_name + "-api.aswat.co/auth/login"
        # Data to be sent in the request
        data = {
            "username": self.username,
            "password": self.password,
            "remember": "true",
        }
        # Make the POST request
        response = requests.post(url, data=data)

        # Print the response
        return response.json()


# Testing

# conf of the endpoint
# instance_name = "ivr-test-poc"
# username = "ziwo@aswat-telecom.com"
# password = "eZpZ107*FDTfY=S0dTeEw-JE^*Z0QCWd^re#JhOilhLMOm0I8ZeUG82fr*Y8xiDz"
#########
# instance_name = "tabby-ksa"
# username = "ziwo@aswat-telecom.com"
# password = "pYW3k^M1Bn5!!%dsySbj0IVIDdQ93Z@osbmGJ3jdFL=-ms=8oeA2Ew3CmorLmiMS"
########
# instance_name = "allsop"
# username = "ziwo@aswat-telecom.com"
# password = "&B33bYdt&npT7#^C@a#In5laoQgBVOcn*4xWNCb$6!SfjExW2sDJz4e3N2jAEeB&"

# auth = AuthManager(instance_name, username, password)
# result = auth.login()

# print("access_token :", result["content"]["access_token"])
