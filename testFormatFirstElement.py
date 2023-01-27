from sortViews import formatFirstElement

xml = '''<viewdef
            type="formtable"
            name="Address Table"
            class="edu.ku.brc.specify.datamodel.Address"
            gettable="edu.ku.brc.af.ui.forms.DataGetterForObj"
            settable="edu.ku.brc.af.ui.forms.DataSetterForObj">
            <desc><![CDATA[Address grid view.]]></desc>
            <definition>Address</definition>
         </viewdef>'''

formattedxml = formatFirstElement(xml)
print(formattedxml)