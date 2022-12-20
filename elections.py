#xgv3cj
globaldic = {}
def add_state(name, votes):
    comparedvotes = 0
    comparedcand = ''
    for numvote in votes:
        if votes[numvote] > comparedvotes:
            comparedvotes = votes[numvote]
            comparedcand = numvote
    globaldic[name] = comparedcand
'''This function stores the election results in an 
empty dictionary globaldic'''
def winner(college):
    collegedic = {}
    total = 0
    global globaldic
    for evotes in college:
        if evotes in globaldic:
            total += college[evotes]
            if globaldic[evotes] in collegedic:
                collegedic[globaldic[evotes]] += college[evotes]
            else:
                collegedic[globaldic[evotes]] = college[evotes]
    for x in collegedic:
        if total != 0 and collegedic[x] / total > .5:
            return x
    return 'No Winner'
'''This function determines the outcome of an election
based on the given dictionary college, it will return
the winning candidate if they recieve more than 50% of the votes
and will return No Winner if they don't'''
def clear():
    global globaldic
    globaldic = {}
'''This function clears the dictionary globaldic'''