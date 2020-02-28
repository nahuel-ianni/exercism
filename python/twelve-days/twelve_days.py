days = ["first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eighth", "ninth", "tenth", "eleventh", "twelfth"]

presents = [    
    "a Partridge in a Pear Tree",
    "two Turtle Doves",
    "three French Hens",
    "four Calling Birds",
    "five Gold Rings",
    "six Geese-a-Laying",
    "seven Swans-a-Swimming",
    "eight Maids-a-Milking",
    "nine Ladies Dancing",
    "ten Lords-a-Leaping",
    "eleven Pipers Piping",
    "twelve Drummers Drumming",
]


def recite(start_verse, end_verse):
    return [compose_lyrics(verse) for verse in range(start_verse, end_verse + 1)]


def compose_lyrics(verse):
    lyrics = [phrase for index, phrase in enumerate(presents) if index in range(0, verse)]
    if verse > 1: lyrics[0] = f"and {lyrics[0]}"
    
    return f'On the {days[verse - 1]} day of Christmas my true love gave to me: {", ".join(reversed(lyrics))}.'
