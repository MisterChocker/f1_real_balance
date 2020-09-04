import xml.etree.ElementTree as ET


def editor(ele):
    op = ele.get('op')
    if op or op != '=':
        value = ele.get('value')
        if value:
            if op == "*":
                ele.set('value', str(1 - (1 - float(value)) / 2))
            else:
                ele.set('value', str(float(value) / 2))

        else:
            value = ele.get('y')
            if value:
                ele.set('y', str(float(value) / 2))


files = [
    "ferrari",
    "force_india",
    "haas",
    "lotus",
    "mclaren",
    "myteam_ferrari",
    "myteam_honda",
    "myteam_mercedes",
    "myteam_renault",
    "redbull",
    "sauber",
    "toro_rosso",
    "williams"
]

for f in files:

    tree = ET.parse(f'{f}.vtf.xml')
    root = tree.getroot()

    for i in root.findall('Upgrade'):
        print(i.get('name'))
        for cat in list(i):
            # This layer has nothing to be edited

            for sub in list(cat):
                # check if we can edit something of interest
                if 'op' in sub.attrib:
                    editor(sub)
                # check for further children
                if list(sub):
                    for c in list(sub):
                        # check if we can edit something of interest
                        if 'op' in c.attrib:
                            editor(c)
                        if list(c):
                            for cc in list(c):
                                # check if we can edit something of interest
                                if 'op' in cc.attrib:
                                    editor(cc)

    tree.write(f'{f}.vtf.xml')

print('Done.')
