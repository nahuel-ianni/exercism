def recite(start, take=1):
    lyrics = []

    while take > 0:
        if start == 0:
            lyrics += [
                "No more bottles of beer on the wall, no more bottles of beer.",
                "Go to the store and buy some more, 99 bottles of beer on the wall."]

            break

        plural_1 = "bottles" if start != 1 else "bottle"
        plural_2 = "bottles" if start - 1 != 1 else "bottle"
        bottle_qty_1 = f"{start}" if start > 0 else "no more"
        bottle_qty_2 = f"{start - 1}" if start - 1 > 0 else "no more"
        bottle_prefix = "one" if start - 1 > 0 else "it"

        lyrics += [
            f"{bottle_qty_1} {plural_1} of beer on the wall, {bottle_qty_1} {plural_1} of beer.",
            f"Take {bottle_prefix} down and pass it around, {bottle_qty_2} {plural_2} of beer on the wall."]

        take -= 1
        start -= 1

        if take > 0:
            lyrics.append("")

    return lyrics
