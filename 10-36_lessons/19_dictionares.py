# dictionary =    A changeable, unordered collection of unique key:value pairs
#                 Fast because the use hashing, allow us to access a value quickly

picks = {'Top':'Gnar',
         'Jungle':'Graves',
         'Mid':'Ryze',
         'AD':'Xayah',
         'Support':'Rakan'}

# print(picks.keys())
# print(picks.values())
# print(picks.items())
picks.update({'AD':'Kaisa'})
picks.update({'Supp':'Leona'})
picks.pop('Support')

for key,value in picks.items():
    print(f'{key} {value}')