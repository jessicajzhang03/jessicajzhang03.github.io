def makehtmlpage(poem): 
    poem_file = poem+'.txt'
    html_file = poem+'.html'
    f = open(poem_file,'r')
    title = f.readline().strip()
    author = f.readline().strip() 
    f.readline() 
    
    line = f.readline() 
    text = '<div class="stanza">'
    while line: 
        print(line.rstrip())
        rstripped = line.rstrip() 
        stripped = line.strip() 
        if rstripped: 
            if rstripped == stripped: 
                text += f'<p>{stripped}</p>'
            else: 
                indent = 0.3*(len(rstripped) - len(stripped))
                text += f'<p style="margin-left:{indent}em;">{stripped}</p>'
        else: 
            text += '</p></div> <div class="stanza">'
        line = f.readline() 
    text += '</div class="stanza">'
    f.close() 
    
    g = open(html_file,'w') 
    base = [
        '{% extends "poem-base.html" %}', 
        f'{{% block title %}}{title}{{% endblock %}}', 
        f'{{% block text %}}{text}{{% endblock %}}', 
        f'{{% block author %}}{author}{{% endblock %}}' 
    ]
    g.write('\n'.join(base)) 
    g.close() 

makehtmlpage(input().strip())