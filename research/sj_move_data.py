# A list of tuples - ie [(foo, bar), (foo2, bar2), (foo3, bar3)]
# Tuple format: (start_time [secs], movement, duration [secs]) ex1: (30, "LL->L", 5) ex2: (40, "L->C", 5)

# VIDEO #1 - STEVE JOBS iPhone 2007 Presentation
# v1 data starts @ 0:30 = 30 secs
v1 = [ (30, "LL->L", 5), (40, "L->C", 5), (52, "C->L", 6), (61, "L->LL", 10), (122, "LL->C", 4), (128, "C->LL", 5), (150, "LL->L", 9), (179, "L->LL", 6), (192, "LL->C", 6), (203, "L->C", 6), (220, "C->L", 5), (243, "L->C", 5), (248, "C->L", 5), (260, "L->LL", 4) ]
# v1 data stops @ 5:00 = 300 secs (so calculate over interval 30-300 secs, maybe subtract 30 from all times)

# VIDEO #2 - STEVE JOBS introduces iPhone 4 & Facetime - WWDC (2010)
# v1 data starts @ 41:34 but fuck it I'll probably start at 0
v2 = [ () ]
# v2 data stops @ 43:33 so end interval @ 43:33 - 41:34 = 1:59 => 119 secs 