from sortViews import formatFirstElement

xml = '''<viewdef name="BorrowAgent"
            type="form"
            class="edu.ku.brc.specify.datamodel.BorrowAgent"
            gettable="edu.ku.brc.af.ui.forms.DataGetterForObj"
            settable="edu.ku.brc.af.ui.forms.DataSetterForObj">
			<desc>
				<![CDATA[The Agent subform for the Borrow form.]]>
			</desc>
			<enableRules/>
			<columnDef>105px,2px,200px,5px,43px,2px,130px,345px,p:g</columnDef>
			<columnDef os="lnx">115px,2px,220px,5px,75px,2px,125px,373px,p:g</columnDef>
			<columnDef os="mac">130px,2px,245px,5px,80px,2px,165px,413px,p:g</columnDef>
			<columnDef os="exp">p,2px,p:g,5px:g,p,2px,p:g(2),p:g(4)</columnDef>
			<rowDef auto="true" cell="p" sep="2px"/>
			<rows>
				<row>
					<cell type="label" labelfor="1"/>
					<cell type="field" id="1" name="agent" uitype="querycbx" initialize="name=Agent;title=Agent"/>
					<cell type="label" labelfor="2"/>
					<cell type="field" id="2" name="role" uitype="combobox"/>
				</row>
				<row>
					<cell type="label" labelfor="3"/>
					<cell type="field" id="3" name="remarks" uitype="textareabrief" rows="2" colspan="6"/>
				</row>
				<!--<row><cell type="label" labelfor="9"/><cell type="field" id="9" name="createdByAgent" uitype="label" readonly="true"  uifieldformatter="Agent"/><cell type="label" labelfor="10"/><cell type="field" id="10" name="modifiedByAgent" uitype="label" readonly="true"  uifieldformatter="Agent"/></row><row><cell type="label" labelfor="11"/><cell type="field" id="11" name="timestampModified" uitype="label" readonly="true"/><cell type="label" labelfor="12"/><cell type="field" id="12" name="timestampCreated" uitype="label" readonly="true"/></row>-->
			</rows>
		</viewdef>'''

formattedxml = formatFirstElement(xml)
print(formattedxml)