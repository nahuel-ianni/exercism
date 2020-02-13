def is_paired(input_string):
    brackets = "".join(c for c in input_string if c in "()[]{}")

    while "()" in brackets or "[]" in brackets or "{}" in brackets:
        brackets = brackets.replace("()", "").replace("[]", "").replace("{}", "")
    
    return len(brackets) == 0
