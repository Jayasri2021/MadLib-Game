def gen_madlibs():
    adj = input("Enter an adjective: ")
    n = input("Enter a noun: ")
    v = input("Enter a verb: ")
    adv = input("Enter an adverb: ")
    madlibs_story = f"The {adj} {n} {v} {adv}."
    return madlibs_story
