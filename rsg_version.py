__version__ = "6.0.0 Release"
version_hash_1 = "Deku Nut"
version_hash_2 = "Deku Nut"


class VersionError(Exception):
    def __init__(self, cause):
        message = f"Your {cause} is out of date. Please update it before continuing."
        with open('random_settings_generation.json', 'w') as fp:
            fp.write(message)
        super().__init__(message)
        

def check_rando_version():
    from version import __version__ as rsg_version
