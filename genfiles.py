a = '''Queequeg was a native of Rokovoko, an island far away to the West and South. It is not down in any map; true places never are.
When a new-hatched savage running wild about his native woodlands in a grass clout, followed by the nibbling goats, as if he were a green sapling; even then, in Queequegs ambitious soul, lurked a strong desire to see something more of Christendom than a specimen whaler or two. His father was a High Chief, a King; his uncle a High Priest; and on the maternal side he boasted aunts who were the wives of unconquerable warriors. There was excellent blood in his veins—royal stuff; though sadly vitiated, I fear, by the cannibal propensity he nourished in his untutored youth'''

word = []
file_names = []
for i in a:
    if i.isalpha():
        word.append(i)
    elif word:
        file_names.append(''.join(word))
        word = []
file_names = list(dict.fromkeys(file_names))
for name in file_names:
    with open(f'./input/{name}','w') as file:
        for i in range(1,100):
            file.write(f'{i}\n')
        file.write('50')
            
