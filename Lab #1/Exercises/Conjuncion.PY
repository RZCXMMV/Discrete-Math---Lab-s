def CreateTables(Values):
    Option = len(Values)
    Table = []

    if Option == 2:
        P, Q = Values
        Table.append([P, Q,P and Q])

    if Option == 3:
        P, Q, R = Values
        Table.append([P, Q, R, (P and Q), (P and Q and R)])

    if Option == 4:
        P, Q, R, S = Values
        Table.append([P, Q, R, S, (P and Q), (P and Q and R), (P and Q and R and S)])

    return Table