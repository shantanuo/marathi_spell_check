with open('mr_IN4.dic', 'w+') as d:
    with open('mr_IN3.dic') as f:
        for i in list(f)[:10000]:
            try:
                if i.rstrip('\n').endswith('णे'):
                    d.write(i+'\n')
                else:
                    d.write(i.rstrip('\n') + '/P' + '\n')
            except:
                pass
            
            
            
with open('nend3.dic', 'w+') as d:
    with open ('nend2.dic') as f:
        for i in list(f):
            x = i.rstrip('\n')
            if 'ु' in x[-8:]:
                d.write(x.replace('N', '')+'\n')
            else:
                d.write(x+'\n')
