import requests


def get_oauth_dict(client_id, client_secret):
    res = requests.post(
        "https://id.twitch.tv/oauth2/token?client_id={}&client_secret={}&grant_type=client_credentials".format(
            client_id,
            client_secret
        )
    )
    return res.json()


def get_streamer_dict(client_id, oauth_access_token):
    url = "https://api.twitch.tv/helix/search/channels?query=comfy_coder"
    res = requests.get(
        url,
        headers={
            "client-id": client_id,
            'Authorization': "Bearer " + oauth_access_token
        }
    )
    return res.json()


def get_follower_list(streamer_id, client_id, oauth_access_token):
    res = requests.get(
        url="https://api.twitch.tv/helix/users/follows?to_id={}".format(streamer_id),
        headers={
            "client-id": client_id,
            'Authorization': "Bearer " + oauth_access_token     # token_type
        }
    )
    return res.json()
