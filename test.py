# here's a list of some people and their favourite youtube channels
fav_yt_channels = [
    ("andy", ["linus tech tips", "mkbhd"]),
    ("nathan", ["lowspecgamer", "linus tech tips", "electroboom"]),
    ("rebecca", ["electroboom", "minutephysics", "cgp grey", "veritasium"]),
    ("amir", ["techmoan", "lgr", "lowspecgamer", "technology connections", "eight bit guy"]),
    ("ben", ["mkbhd", "linus tech tips"]),
    ("chen", ["lgr", "techmoan", "eight bit guy", "lowspecgamer", "technology connections"]),
    ("john", ["mkbhd", "linus tech tips"])
]

# the expected output for the above test cases
fav_yt_channels_out = [["andy", "ben", "john"], ["nathan"], ["rebecca"], ["amir", "chen"]]


# here's a club of people where everyone likes only LTT and mkbhd
same_interests =[ 
    ("andy", ["linus tech tips", "mkbhd"]),
    ("nathan", ["linus tech tips", "mkbhd"]),
    ("rebecca", ["linus tech tips", "mkbhd"]),
    ("amir", ["linus tech tips", "mkbhd"]),
    ("ben", ["linus tech tips", "mkbhd"]),
    ("chen", ["linus tech tips", "mkbhd"])
]

# and here's the expected output
same_interests_out = [['amir', 'andy', 'ben', 'chen', 'nathan', 'rebecca']]


# if everyone has a different set of liked channels
different_interests = [  
    ("andy", ["linus tech tips", "mkbhd"]),
    ("nathan", ["lowspecgamer", "linus tech tips", "electroboom"]),
    ("rebecca", ["electroboom", "minutephysics", "cgp grey", "veritasium"]),
    ("amir", ["practical engineering", "wendover productions"]),
    ("ben", ["plainly difficult", "fascinating horror"]),
    ("chen", ["lgr", "techmoan", "eight bit guy", "lowspecgamer", "technology connections"])
]

# and the expected output
different_interests_out = [["andy"], ["nathan"], ["rebecca"], ["amir"], ["ben"], ["chen"]]


# here's an edge case: empty input!
empty_data = []
empty_data_out = []