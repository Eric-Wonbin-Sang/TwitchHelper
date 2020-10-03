import datetime

from Classes import Streamer
from lib import TwitchLib

from General import Functions, Constants


def main():

    twitch_credentials_dict = Functions.parse_json(Constants.twitch_credentials_file_path)
    twitch_oauth_dict = TwitchLib.get_oauth_dict(twitch_credentials_dict["client_id"], twitch_credentials_dict["secret"])

    streamer = Streamer.Streamer(
        credentials_dict=twitch_credentials_dict,
        oauth_dict=twitch_oauth_dict,
        **TwitchLib.get_streamer_dict(twitch_credentials_dict["client_id"], twitch_oauth_dict["access_token"])["data"][0]
    )

    print("Current followers as of {}:".format(Functions.get_pretty_time(datetime.datetime.now())))
    print(Functions.tab_str("\n".join([str(x) for x in streamer.get_follower_list()]), 1))
    print("-------------\n")
    streamer.listen_for_followers()


main()
