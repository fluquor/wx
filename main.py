import xml.etree.ElementTree as ET

def main():
    tree=ET.parse('ele.xml')
    to=tree.find('CreateTime')
    print(to.text)

if __name__ == '__main__':
    main()
    