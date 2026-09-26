import re

with open('c:/Users/Admin/estmi/ESTMI_web/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace email
html = html.replace('info@estmi.ee', 'estmiteenus@gmail.com')

# Replace phone link
html = html.replace('+37200000000', '+3725533178')

# Replace phone display text
html = html.replace('+372 000 0000', '+372 55 33 178')

# Replace address
html = html.replace('Kogu Eesti · kontor Harjumaal', 'Juure tee 2-2, Tiskre küla, Harku vald, 76916')

with open('c:/Users/Admin/estmi/ESTMI_web/index.html', 'w', encoding='utf-8') as f:
    f.write(html)
