def build_successors_table(tokens):
    """Return a dictionary: keys are words; values are lists of successors."""

    table = {}
    prev = '.'
    for word in tokens:
        if prev not in table:

            table[prev] = [word]
        else:
            table[prev].append(word)
        prev = word
    return table

text = ['We', 'came', 'to', 'investigate', ',', 'catch', 'bad', 'guys', 'and', 'to', 'eat', 'pie', '.']
table = build_successors_table(text)
sorted(table)
table['to']
table['pie']
table['.']
