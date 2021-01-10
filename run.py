import sys
import src.etl.get_anames as gn

args = args[1:]
fname = ""

if "scrape" in args:
    fname = gn.scrape()
    
if "retrieve" in args:
    if fname == "":
        artnames = gn.retrieve()
    else:
        artnames = gn.retrieve(fname)
