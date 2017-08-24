from wikidataintegrator import wdi_core, wdi_login, wdi_property_store
import copy
import os


wdi_property_store.wd_properties['P3289'] = {
        'datatype': 'string',
        'name': 'Cellosaurus ID',
        'domain': ['cell lines'],
        'core_id': 'True'
    }

#References
refStatedIn = wdi_core.WDItemID(value="Q16626729", prop_nr='P248', is_reference=True)
refCellId = wdi_core.WDString("CVCL_1906", prop_nr='P3289', is_reference=True)
cellosaurus_reference = [refStatedIn,refCellId]

prep = dict()

prep["P1343"] = []
prep["P1343"].append(wdi_core.WDItemID("Q37854720", prop_nr="P1343", references=[copy.deepcopy(cellosaurus_reference)]))
prep["P1343"].append(wdi_core.WDItemID("Q37854696", prop_nr="P1343", references=[copy.deepcopy(cellosaurus_reference)]))
prep["P1343"].append(wdi_core.WDItemID("Q37854683", prop_nr="P1343", references=[copy.deepcopy(cellosaurus_reference)]))
prep["P1343"].append(wdi_core.WDItemID("Q37854660", prop_nr="P1343", references=[copy.deepcopy(cellosaurus_reference)]))
prep["P1343"].append(wdi_core.WDItemID("Q37854627", prop_nr="P1343", references=[copy.deepcopy(cellosaurus_reference)]))
prep["P1343"].append(wdi_core.WDItemID("Q37854604", prop_nr="P1343", references=[copy.deepcopy(cellosaurus_reference)]))
prep["P1343"].append(wdi_core.WDItemID("Q37854595", prop_nr="P1343", references=[copy.deepcopy(cellosaurus_reference)]))
prep["P1343"].append(wdi_core.WDItemID("Q16554737", prop_nr="P1343", references=[copy.deepcopy(cellosaurus_reference)]))
prep["P1343"].append(wdi_core.WDItemID("Q37854544", prop_nr="P1343", references=[copy.deepcopy(cellosaurus_reference)]))

data2add = []
for key in prep.keys():
    for statement in prep[key]:
        data2add.append(statement)
        print(statement.prop_nr, statement.value)

wdPage = wdi_core.WDItemEngine(wd_item_id="Q16554737", data=data2add, server="www.wikidata.org", domain="cell lines", global_ref_mode="STRICT_KEEP")
logincreds = wdi_login.WDLogin(user=os.environ["wd_user"], pwd=os.environ["pwd"])
wdPage.write(logincreds)