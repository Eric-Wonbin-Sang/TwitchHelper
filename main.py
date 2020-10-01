import time
import datetime

from Classes import Streamer
from lib import TwitchLib

from General import Functions, Constants


def main():

    credentials_dict = Functions.parse_json(Constants.credentials_file_path)

    oauth_dict = TwitchLib.get_oauth_dict(credentials_dict["client_id"], credentials_dict["secret"])

    streamer = Streamer.Streamer(
        credentials_dict=credentials_dict,
        oauth_dict=oauth_dict,
        **TwitchLib.get_streamer_dict(credentials_dict["client_id"], oauth_dict["access_token"])["data"][0]
    )

    print("Current followers as of {}:".format(Functions.get_pretty_time(datetime.datetime.now())))
    for follower in streamer.get_follower_list():
        print(
            "\t{} | name: {}  id: {}".format(
                Functions.get_pretty_time(follower.followed_at),
                Functions.str_to_length(follower.from_name, 18),
                follower.from_id
            )
        )
    print("-------------\n")
    prev_follower_list = streamer.get_follower_list()
    print("Listening for follower changes... (takes a bit to update in the API)")
    while True:
        curr_follower_list = streamer.get_follower_list()
        for prev_follower in prev_follower_list:
            if prev_follower not in curr_follower_list:
                print(
                    "\tLost follower! - {} | name: {}  id: {}".format(
                        Functions.get_pretty_time(prev_follower.followed_at),
                        Functions.str_to_length(prev_follower.from_name, 18),
                        prev_follower.from_id
                    )
                )
        for curr_follower in curr_follower_list:
            if curr_follower not in prev_follower_list:
                print(
                    "\tNew follower! - {}  | name: {}  id: {}".format(
                        Functions.get_pretty_time(curr_follower.followed_at),
                        Functions.str_to_length(curr_follower.from_name, 18),
                        curr_follower.from_id
                    )
                )
        prev_follower_list = curr_follower_list
        time.sleep(4)


main()
