def recite(start, take=1):
    lyrics = []

    while take > 0:
        if start == 0:
            lyrics += [
                "No more bottles of beer on the wall, no more bottles of beer.",
                f"Go to the store and buy some more, 99 bottles of beer on the wall."]

            break

        lyrics += [
            f"{bottle_num(start)} {bottle_txt(start)} of beer on the wall, {bottle_num(start)} {bottle_txt(start)} of beer.",
            f"Take {bottle_qty(start - 1)} down and pass it around, {bottle_num(start - 1)} {bottle_txt(start - 1)} of beer on the wall."]

        take -= 1
        start -= 1

        if take > 0:
            lyrics.append("")

    return lyrics


def bottle_num(number):
    return f"{number}" if number > 0 else "no more"


def bottle_txt(number):
    return "bottles" if number != 1 else "bottle"


def bottle_qty(number):
    return "one" if number > 0 else "it"
