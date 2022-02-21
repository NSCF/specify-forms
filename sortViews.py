#sorts the views and viewdefs in a views.xml file
#note this replaces the original file, so commit first...

fileName = 'bird//manager/bird.views.xml'

def getElemName(xmlStr):
  nameAttrStart = xmlStr.index('name')
  #now we need the closing quote
  nameStart = xmlStr.index('"', nameAttrStart) + 1
  nameEnd = xmlStr.index('"', nameStart)
  name = xmlStr[nameStart:nameEnd]
  return name

def sortxmlElems(xmlstr, section):

  openingtag = '<' + section + '>'
  closingtag = '</' + section + '>'

  xmlStart = xmlstr.index(openingtag)
  xmlEnd = xmlstr.index(closingtag) + len(closingtag)
  xmlString = xmlstr[xmlStart:xmlEnd]

  #split into individual views
  elements = []
  searchStart = len(openingtag) + 1
  elemOpeningTag = '<' + section[:-1]
  elemClosingTag = '</' + section[:-1] + '>'
  while searchStart < len(xmlString):
    try:
      elemStart = xmlString.index(elemOpeningTag, searchStart)
    except:
      break

    elemEnd = xmlString.index(elemClosingTag, searchStart) + len(elemClosingTag)
    elem = xmlString[elemStart:elemEnd]
    elements.append(elem)

    searchStart = elemEnd + 1
  
  elements.sort(key=getElemName)

  #strings are immutable so we have to do this
  firstxml = xmlstr[0:xmlStart]
  lastxml = xmlstr[xmlEnd:]
  print('sorting', len(elements), section)
  newxml = firstxml + openingtag + '\n\n\t\t' + '\n\n\t\t'.join(elements) + '\n\n\t' + closingtag + lastxml

  return newxml

###the actual script ###

with open(fileName, 'r') as f:
  xml = f.read()

sortedviewsxml = sortxmlElems(xml, 'views')
sortedviewdefsxml = sortxmlElems(sortedviewsxml, 'viewdefs')

with open(fileName, 'w') as f:
  f.write(sortedviewdefsxml)

print('all done')






