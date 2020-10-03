import time

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

    def listen_for_followers(self):
        prev_follower_list = self.get_follower_list()
        print("Listening for follower changes... (takes a bit to update in the API)")
        while True:
            curr_follower_list = self.get_follower_list()
            for prev_follower in prev_follower_list:
                if prev_follower not in curr_follower_list:
                    print("\tLost follower! - " + str(prev_follower))
            for curr_follower in curr_follower_list:
                if curr_follower not in prev_follower_list:
                    print("\tNew follower!  - " + str(curr_follower))
            prev_follower_list = curr_follower_list
            time.sleep(4)

    def __str__(self):
        return "Streamer - name: {}  id: {}".format(
            self.display_name,
            self.id
        )
