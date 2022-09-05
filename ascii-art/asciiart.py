import requests
# attempted to use a different website for the art generation
# this request kinda works, but the returns a JSON with the ASCII art
# and a style, which would need to be further parsed to display
r = requests.get('http://api.textart.io/figlet.json?text=Awesomesauce')
print(r.text)