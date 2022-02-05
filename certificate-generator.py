from PIL import Image, ImageFont, ImageDraw

Font = ImageFont.truetype(r'certificate-generator\font\AGENCYB.TTF',150)
Color = "#000000"

certificate_template = Image.open(r'certificate.png')
Height, Width = certificate_template.size

def generate_certificates(name):
    source =    Image.open(r'certificate.png')
    draw = ImageDraw.Draw(source)
    name_height, name_width = draw.textsize(name, font=Font)

    draw.text(((Width - name_width) / 2, (Height - name_height) / 2), name, fill=Color, font=Font)
    source.save("./output/"+name+".png")
    print("Successfully generated Certificate for",name)

names = ['Sparsh Singh', 'Shalini Pathak', 'Jayshree Patil', 'Aniket Kumar']
for name in names:
    generate_certificates(name)

print("Saved",len(names), "certificates successfully.")