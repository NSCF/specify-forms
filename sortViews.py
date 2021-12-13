
fileName = 'common/common.views.xml'
newFileName = 'common/common.views.sorted.xml'

def getViewName(viewStr):
  nameAttrStart = viewStr.index('name')
  #now we need the closing quote
  nameStart = viewStr.index('"', nameAttrStart) + 1
  nameEnd = viewStr.index('"', nameStart)
  name = viewStr[nameStart:nameEnd]
  return name

with open(fileName, 'r') as f:
    xml = f.read()

    viewsStart = xml.index('<views>')
    viewsEnd = xml.index('</views>') + len('</views>')
    viewsString = xml[viewsStart:viewsEnd]

    #split into individual views
    views = []
    searchStart = len('<views>') + 1
    while searchStart < len(viewsString):
      try:
        viewStart = viewsString.index('<view', searchStart)
      except:
        break

      viewEnd = viewsString.index('</view>', searchStart) + len('</view>')
      view = viewsString[viewStart:viewEnd]
      viewName = getViewName(view)
      views.append(view)
  
      searchStart = viewEnd + 1
    
views.sort(key=getViewName)

#strings are immutable so we have to do this
firstxml = xml[0:viewsStart]
lastxml = xml[viewsEnd:]
newxml = firstxml + '<views>\n\n\t\t' + '\n\n\t\t'.join(views) + '\n\n\t</views>' + lastxml

with open(newFileName, 'w') as f:
  f.write(newxml)

print('all done')






