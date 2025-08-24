from config import USERNAME, PASSWORD
from abu import Portal


portal = Portal(USERNAME, PASSWORD)

portal.print_examcard()
