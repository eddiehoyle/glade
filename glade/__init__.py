import os

# TODO: Tidy this up
os.environ["GLADE_ROOT"] = os.path.abspath("%s/.." % os.path.dirname(os.path.abspath(__file__)))