def study_places(buildings):
    """Return a list of building names for study, excluding 'D Hall'.

    You MUST use a <b>while</b> loop! Use of count() is NOT allowed.

    Example: study_places(['King Hall', 'D Hall', 'ETMC']) returns ['King Hall', 'ETMC']. because

    Args:
        buildings (list): a list of building names.

    Returns:
        list: A list of building names except for 'D Hall'.
    """
    study = []
    i = 0
    while i < len(buildings):
        if buildings[i] != "D Hall":
            study.append(buildings[i])
        i += 1
    
    return study

rooms = ["King Hall", "D Hall", "ETMC"]
print(study_places(rooms))
            