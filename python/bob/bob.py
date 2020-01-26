def response(hey_bob):
    phrase = hey_bob.strip()
    response = "Whatever."

    if not phrase:
        response = "Fine. Be that way!"

    elif phrase[-1] == "?":
        if _char_are_uppercase(phrase) and _sentence_has_chars(phrase):
            response =  "Calm down, I know what I'm doing!"
        
        else:
            response = "Sure."

    elif _char_are_uppercase(phrase) and _sentence_has_chars(phrase):
            response = "Whoa, chill out!"

    return response


def _sentence_has_chars(phrase):
    return any([c.isalpha() for c in phrase])


def _char_are_uppercase(phrase):
    phrase = "".join([c for c in phrase if c.isalpha()])
    
    return phrase == phrase.upper() 
