import dateutil.parser

from General import Functions


class Follower:

    def __init__(self, **kwargs):

        self.followed_at = dateutil.parser.isoparse(kwargs.get("followed_at"))
        self.from_id = kwargs.get("from_id")
        self.from_name = kwargs.get("from_name")
        self.to_id = kwargs.get("to_id")
        self.to_name = kwargs.get("to_name")

    def __eq__(self, other):
        return self.from_id == other.from_id

    def __str__(self):
        return "Follower - name: {}  followed_at: {}".format(
            self.from_name,
            Functions.get_pretty_time(self.followed_at)
        )
