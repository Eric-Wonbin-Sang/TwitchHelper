from Classes import Follower
from lib import TwitchLib


class Streamer:

    def __init__(self, credentials_dict, oauth_dict, **kwargs):

        self.credentials_dict = credentials_dict
        self.oauth_dict = oauth_dict

        self.broadcaster_language = kwargs.get("broadcaster_language")
        self.display_name = kwargs.get("display_name")
        self.game_id = kwargs.get("game_id")
        self.id = kwargs.get("id")
        self.is_live = kwargs.get("is_live")
        self.started_at = kwargs.get("started_at")
        self.tag_ids = kwargs.get("tag_ids")
        self.thumbnail_url = kwargs.get("thumbnail_url")
        self.title = kwargs.get("title")

    def get_follower_list(self):
        response_dict = TwitchLib.get_follower_list(
            streamer_id=self.id,
            client_id=self.credentials_dict["client_id"],
            oauth_access_token=self.oauth_dict["access_token"]
        )
        follower_list = []
        for data_dict in response_dict["data"]:
            follower_list.append(Follower.Follower(**data_dict))
        return follower_list

    def __str__(self):
        return "Streamer - name: {}  id: {}".format(
            self.display_name,
            self.id
        )
