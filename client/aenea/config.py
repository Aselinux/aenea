# Client-side config (Windows running Dragon sending commands)
HOST = "192.168.56.1"
PORT = 8240

# Whether to use proxy or native (not all modules support native.)
PLATFORM = "proxy"
#PLATFORM = "windows"

# Whether to use the server's multiple_actions RPC method.
USE_MULTIPLE_ACTIONS = True

SCREEN_RESOLUTION = (1920 * 2 + 2560), 1440

PROJECT_ROOT = "E:\\aenea"

# If this is enabled, reloading the configuration will not copy over the
# client-side configuration file at util/config.py (ie this file). this is useful
# if you wish to keep the master copy of your configuration files in the Natlink
# directory.
DONT_UPDATE_CONFIG = False
