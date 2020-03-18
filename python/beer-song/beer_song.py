def recite(start, take=1):
    lyrics = []

    while take > 0:
        if start == 0:
            lyrics += [
                "No more bottles of beer on the wall, no more bottles of beer.",
                "Go to the store and buy some more, 99 bottles of beer on the wall."]

            break

        bottles = get_bottles(start)
        lyrics += [
            f"{bottles} of beer on the wall, {bottles} of beer.",
            f"Take {'one' if start - 1 else 'it'} down and pass it around, {get_bottles(start - 1)} of beer on the wall."]

        take -= 1
        start -= 1

        if take > 0:
            lyrics.append("")

    return lyrics


def get_bottles(number):
    return f"{number or 'no more'} {'bottles' if number != 1 else 'bottle'}"
