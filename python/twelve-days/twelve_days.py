presents = {
    1  : ("first"   , "a Partridge in a Pear Tree"),
    2  : ("second"  , "two Turtle Doves,"),
    3  : ("third"   , "three French Hens,"),
    4  : ("fourth"  , "four Calling Birds,"),
    5  : ("fifth"   , "five Gold Rings,"),
    6  : ("sixth"   , "six Geese-a-Laying,"),
    7  : ("seventh" , "seven Swans-a-Swimming,"),
    8  : ("eighth"  , "eight Maids-a-Milking,"),
    9  : ("ninth"   , "nine Ladies Dancing,"),
    10 : ("tenth"   , "ten Lords-a-Leaping,"),
    11 : ("eleventh", "eleven Pipers Piping,"),
    12 : ("twelfth" ,  "twelve Drummers Drumming,"),
}

def recite(start_verse, end_verse):
    if start_verse == end_verse:
        start_verse = 1

    intro = f"On the {presents[end_verse][0]} day of Christmas my true love gave to me: "
    print(intro)
    
    # days  = [phrase for index, phrase in enumerate(presents.values()) if index in range(0, end_verse)]

    return None
