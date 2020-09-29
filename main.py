import requests
import json
import pprint

from General import Functions, Constants


def get_oauth_dict(client_id, client_secret):
    oauth = requests.post(
        "https://id.twitch.tv/oauth2/token?client_id={}&client_secret={}&grant_type=client_credentials".format(
            client_id,
            client_secret
        )
    )
    return oauth.json()


def main():

    pp = pprint.PrettyPrinter(indent=4)

    credentials_dict = Functions.parse_json(Constants.credentials_file_path)

    oauth_dict = get_oauth_dict(credentials_dict["client_id"], credentials_dict["secret"])
    pp.pprint(oauth_dict)

    url = "https://api.twitch.tv/helix/search/channels?query=comfy_coder"
    res = requests.get(
        url,
        headers={
            "client-id": credentials_dict["client_id"],
            'Authorization': "Bearer " + oauth_dict["access_token"]
        }
    )
    pp.pprint(res.json())

    res = requests.get(
        url="https://api.twitch.tv/helix/users/follows?to_id={}".format(589965916),
        headers={
            "client-id": credentials_dict["client_id"],
            'Authorization': "Bearer " + oauth_dict["access_token"]
        }
    )
    pp.pprint(res.json())



main()
