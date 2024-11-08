import requests
import math


class AgentManager:

    def __init__(self, instance_name, access_token):
        self.instance_name = instance_name
        self.access_token = access_token
        self.agents = self.get_agents()

    def get_agents_count(self, plan="regular"):
        url = (
            "https://"
            + self.instance_name
            + f"-api.aswat.co/admin/agents/count?search&plan={plan}"
        )
        headers = {"access_token": self.access_token}
        response = requests.get(url, headers=headers)

        # print(response.json())
        return response.json()["content"]

    def get_agents(self, plan="regular"):
        """get all ahents with their assigned queues

        Args:
            plan (str, optional): _description_. Defaults to "regular".

        Returns:
            dict: agents
        """

        count = self.get_agents_count(plan)
        agents = []
        for skip in range(0, math.ceil(count / 50)):
            url = (
                "https://"
                + self.instance_name
                + f"-api.aswat.co/admin/agents/?limit=50&skip={skip * 50}&search&order&plan={plan}"
            )
            headers = {"access_token": self.access_token}
            response = requests.get(url, headers=headers)
            agents.extend(response.json()["content"])

        # print(agents)
        return agents

    def get_agent_by_username(self, username):
        # agents = self.get_agents()
        for agent in self.agents:
            if agent["username"] == username:
                return agent
        return None

    def create_agent(self, username, firstName, lastName, extra_fields={}):
        url = "https://" + self.instance_name + f"-api.aswat.co/admin/agents"
        payload = {
            "username": username,
            "firstName": firstName,
            "lastName": lastName,
        }
        payload.update(extra_fields)
        headers = {
            "access_token": self.access_token,
            "Content-Type": "application/json",
        }

        response = requests.post(url, headers=headers, json=payload)

        return response

    def update_agent(self, username, fields={}):
        agent = self.get_agent_by_username(username)
        url = (
            "https://"
            + self.instance_name
            + f"-api.aswat.co/admin/agents/{agent['id']}"
        )
        payload = fields
        headers = {
            "access_token": self.access_token,
            "Content-Type": "application/json",
        }
        response = requests.put(url, headers=headers, json=payload)
        return response


# instance_name = "tabby-ksa"
# instance_name = "allsop"
# access_token = "4be8e6f7-1c7a-4557-90d2-227dceaba7c6"
# access_token = "8de247f3-459f-4b87-88c5-71e66bba12b1"

# instance_name = "tabby-ksa"
# access_token = "d0a82436-e18c-47cc-9d16-77f7206d3b8b"

# agent = AgentManager(instance_name, access_token)

# agent.get_agents_count()
# print( agent.create_agent("marc.w@allsoppandallsopp.com", "Marc", "Walters", {"noAnswerTimeout": 10}) )

# agent.get_agents_count(plan="regular")
# agent.get_agents(plan="regular")
# agents = agent.get_agents()
# print(agents)

# agent_username = agent.get_agent_by_username(username="dina.zakaria@tabby.ai")
# print(agent_username)
# print(agent_username["id"])

# agent.create_agent(
#     "fatma.hgag@tabby.ai",
#     "Fatma",
#     "Hgag LB",
#     wrapUpTime=10,
#     noAnswerTimeout=12,
#     autoAnswer=True,
#     noAnswerDelayTime=7,
#     countryCode="IN",
#     languageCode="fr",
#     plan="regular",
#     pauseRecording=True,
# )

# extra = {
#     "wrapUpTime": 10,
#     "noAnswerTimeout": 12,
#     "autoAnswer": True,
#     "noAnswerDelayTime": 7,
#     "countryCode": "IN",
#     "languageCode": "fr",
#     "plan": "regular",
#     "pauseRecording": True}
