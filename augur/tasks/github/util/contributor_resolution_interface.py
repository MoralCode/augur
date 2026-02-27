
from .AugurForgeUser import AugurForgeUser 

class ContributorResolveable():
    """Interface class defining methods that all API endpoint classes must share in order to resolve contributors
    """

    def get_user_by_commit(self, owner:str, repo: str, commit_hash:str) -> AugurForgeUser:
        """Look up a user on this platform by a known commit they made
        This is the successor to the legacy get_login_with_commit_hash() method

        Args:
            owner (str): the name of the owner (user/org) account hosting the repo
            repo (str): the name of the repo
            commit_hash (str): the hash of the commit known to have been made by the intended user being looked up.

        Returns:
            AugurForgeUser: An augur internal forge user instance that can be passed around the application.
        """
        raise NotImplementedError("This is a method defined in an interface class that needs to be implemented")

    def get_user_by_info(self, name:str, email: str) -> AugurForgeUser:
        """Look up a user on this platform by their name and/or email
        This is the successor to the legacy get_login_with_supplemental_data() method

        Args:
            name (str): the users name to use in a search
            email (str): the users email address to use in a search

        Returns:
            AugurForgeUser: An augur internal forge user instance that can be passed around the application.
        """
        raise NotImplementedError("This is a method defined in an interface class that needs to be implemented")

    def get_user(self, username:str) -> AugurForgeUser:
        """Look up a user on this platform by their username

        Args:
            username (str): the username to look up

        Returns:
            AugurForgeUser: An augur internal forge user instance that can be passed around the application.
        """
        raise NotImplementedError("This is a method defined in an interface class that needs to be implemented")
