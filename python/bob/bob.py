def response(hey_bob):
    phrase = hey_bob.strip()
    response = "Whatever."

    if phrase.isupper() and phrase.endswith("?"):
        response = "Calm down, I know what I'm doing!"

    elif phrase.isupper():
        response = "Whoa, chill out!"
    
    elif phrase.endswith("?"):
        response = "Sure."
    
    elif not phrase:
        response = "Fine. Be that way!"

    return response
