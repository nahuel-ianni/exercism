presents = {
    1  : ("first"   , "a Partridge in a Pear Tree"),
    2  : ("second"  , "two Turtle Doves"),
    3  : ("third"   , "three French Hens"),
    4  : ("fourth"  , "four Calling Birds"),
    5  : ("fifth"   , "five Gold Rings"),
    6  : ("sixth"   , "six Geese-a-Laying"),
    7  : ("seventh" , "seven Swans-a-Swimming"),
    8  : ("eighth"  , "eight Maids-a-Milking"),
    9  : ("ninth"   , "nine Ladies Dancing"),
    10 : ("tenth"   , "ten Lords-a-Leaping"),
    11 : ("eleventh", "eleven Pipers Piping"),
    12 : ("twelfth" , "twelve Drummers Drumming"),
}


def recite(start_verse, end_verse):
    return [compose_lyrics(verse) for verse in range(start_verse, end_verse + 1)]


def compose_lyrics(verse):
    lyrics = f"On the {presents[verse][0]} day of Christmas my true love gave to me: "
    daily_phrase = [f"{phrase[1]}," for index, phrase in enumerate(presents.values()) if index in range(0, verse)]
    daily_phrase[0] = f"and {daily_phrase[0][:-1]}." if len(daily_phrase) > 1 else f"{daily_phrase[0][:-1]}."
    
    return lyrics + " ".join(reversed(daily_phrase))
