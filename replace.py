import re

with open('c:/Users/Admin/estmi/ESTMI_web/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace blue text with dark grey
html = html.replace('color:#1F4E9C', 'color:#151515')

# Replace blue hover with dark grey hover
html = html.replace('background:#1F4E9C', 'background:#151515')

# Replace rgba blue background
html = html.replace('rgba(31,78,156,0.92)', 'rgba(21,21,21,0.92)')

# Replace yellow background with neon green gradient
html = html.replace('background:#F5C518', 'background:linear-gradient(135deg, #b5ff00 0%, #10e826 100%)')

# Replace yellow text with neon green solid
html = html.replace('color:#F5C518', 'color:#52e000')

# Replace yellow border with neon green solid
html = html.replace('border-color:#F5C518', 'border-color:#52e000')

# Replace remaining blue/yellow hexes
html = html.replace('border-color:#1F4E9C', 'border-color:#52e000')
html = html.replace('#1F4E9C', '#151515')
html = html.replace('#F5C518', '#52e000')

with open('c:/Users/Admin/estmi/ESTMI_web/index.html', 'w', encoding='utf-8') as f:
    f.write(html)
