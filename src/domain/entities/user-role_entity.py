class UserRole:
    """Represents a relationship between a user and a role."""

    def __init__(self, uid: int, rid: int):
        self.uid: int = uid
        """The ID of the user.
        """
        self.rid: int = rid
        """The ID of the role.
        """
