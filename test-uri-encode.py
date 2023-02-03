from urllib.parse import quote
from urllib.parse import unquote
q = 'params={"params":[{"svc":"events/update_units","params":{"mode":"add","units":[{"id":22833343,"detect":{"sensors,lls,ignition":0}},{"id":22786556,"detect":{"sensors,lls,ignition":0}}]}}],"flags":0}&sid='
u = 'params=%7B%22params%22%3A%5B%7B%22svc%22%3A%22core%2Fupdate_data_flags%22%2C%22params%22%3A%7B%22spec%22%3A%5B%7B%22type%22%3A%22col%22%2C%22data%22%3A%5B%2222511245%22%2C%2222511315%22%2C%2222511352%22%2C%2222511371%22%2C%2222511395%22%2C%2222511549%22%2C%2222512400%22%2C%2222512686%22%2C%2222517564%22%2C%2222518416%22%2C%2222518584%22%2C%2222519288%22%2C%2222528628%22%2C%2222528908%22%2C%2222529061%22%2C%2222529499%22%2C%2222530185%22%2C%2222530462%22%2C%2222533870%22%2C%2222533999%22%2C%2222534544%22%2C%2222534711%22%2C%2222534874%22%2C%2222535021%22%2C%2222537666%22%2C%2222537984%22%2C%2222538007%22%2C%2222538163%22%2C%2222538412%22%2C%2222538534%22%2C%2222538541%22%2C%2222543728%22%2C%2222544657%22%2C%2222544666%22%2C%2222545166%22%2C%2222545392%22%2C%2222545432%22%2C%2222545444%22%2C%2222545550%22%2C%2222545598%22%2C%2222545777%22%2C%2222545869%22%2C%2222546051%22%2C%2222551671%22%2C%2222552581%22%2C%2222552598%22%2C%2222552604%22%2C%2222552609%22%2C%2222552612%22%2C%2222552621%22%2C%2222552627%22%2C%2222553704%22%2C%2222559267%22%2C%2222559403%22%2C%2222559617%22%2C%2222559636%22%2C%2222559741%22%2C%2222559827%22%2C%2222560261%22%2C%2222560690%22%2C%2222560899%22%2C%2222560920%22%2C%2222561222%22%2C%2222561656%22%2C%2222561671%22%2C%2222561680%22%2C%2222561691%22%2C%2222561705%22%2C%2222561715%22%2C%2222566567%22%2C%2222566916%22%2C%2222567272%22%2C%2222567883%22%2C%2222568192%22%2C%2222568228%22%2C%2222568263%22%2C%2222568318%22%2C%2222569022%22%2C%2222569029%22%2C%2222569036%22%2C%2222569042%22%2C%2222569050%22%2C%2222569055%22%2C%2222569060%22%2C%2222569065%22%2C%2222569071%22%2C%2222569078%22%2C%2222569086%22%2C%2222569093%22%2C%2222569097%22%2C%2222569104%22%2C%2222569109%22%2C%2222574357%22%2C%2222574375%22%2C%2222590292%22%2C%2222590471%22%2C%2222590668%22%2C%2222591312%22%2C%2222591910%22%2C%2222592061%22%2C%2222597908%22%2C%2222597970%22%2C%2222598459%22%2C%2222598708%22%2C%2222598714%22%2C%2222613344%22%2C%2222613822%22%2C%2222629202%22%2C%2222629288%22%2C%2222637038%22%2C%2222637054%22%2C%2222637084%22%2C%2222651943%22%2C%2222682935%22%2C%2222779722%22%2C%2222786556%22%2C%2222786828%22%2C%2222787000%22%2C%2222787116%22%2C%2222787410%22%2C%2222793225%22%2C%2222802698%22%2C%2222811077%22%2C%2222811089%22%2C%2222811094%22%2C%2222811504%22%2C%2222812553%22%2C%2222818708%22%2C%2222821039%22%2C%2222821235%22%2C%2222821842%22%2C%2222826896%22%2C%2222826925%22%2C%2222827027%22%2C%2222827734%22%2C%2222827762%22%2C%2222828105%22%2C%2222828307%22%2C%2222829196%22%2C%2222829325%22%2C%2222829344%22%2C%2222833035%22%2C%2222833343%22%2C%2222835981%22%2C%2222836008%22%2C%2222840018%22%2C%2222840397%22%2C%2222840717%22%2C%2222851627%22%2C%2222857130%22%2C%2222857846%22%2C%2222858029%22%2C%2222858610%22%2C%2222858782%22%2C%2222874978%22%2C%2222874993%22%2C%2222883957%22%2C%2222892351%22%2C%2222892383%22%2C%2222892444%22%2C%2222892850%22%2C%2222893688%22%2C%2222914063%22%2C%2222914110%22%2C%2222990603%22%2C%2222991857%22%2C%2223032364%22%2C%2223032538%22%2C%2223040851%22%2C%2223133579%22%2C%2223151123%22%2C%2223774991%22%2C%2223775008%22%2C%2223775181%22%2C%2223775256%22%2C%2223775383%22%2C%2223775433%22%2C%2223775475%22%2C%2223775522%22%2C%2223775559%22%2C%2223775578%22%2C%2223775599%22%2C%2223775657%22%2C%2223775682%22%2C%2223775701%22%2C%2223775716%22%2C%2223775732%22%2C%2223775761%22%2C%2224353758%22%2C%2224834421%22%2C%2225087107%22%2C%2225649729%22%2C%2225649772%22%2C%2225649790%22%2C%2225649796%22%2C%2225657118%22%2C%2225676298%22%2C%2226025413%22%2C%2226026953%22%2C%2226026958%22%2C%2226026968%22%2C%2226026970%22%2C%2226026974%22%2C%2226026978%22%2C%2226026983%22%2C%2226035977%22%2C%2226037572%22%2C%2226037577%22%2C%2226037586%22%2C%2226037594%22%2C%2226037600%22%2C%2226037603%22%2C%2226037608%22%2C%2226037620%22%2C%2226037623%22%2C%2226037627%22%2C%2226037641%22%2C%2226122723%22%2C%2226122766%22%2C%2226122802%22%2C%2226122808%22%2C%2226122892%22%2C%2226122960%22%2C%2226123014%22%2C%2226123183%22%2C%2226123306%22%2C%2226123528%22%2C%2226134421%22%2C%2226134424%22%2C%2226134428%22%2C%2226134461%22%2C%2226135082%22%2C%2226135095%22%2C%2226135106%22%2C%2226135110%22%2C%2226135155%22%2C%2226144747%22%2C%2226144749%22%2C%2226264424%22%2C%2226264426%22%2C%2226264427%22%2C%2226268894%22%2C%2226268908%22%2C%2226268910%22%2C%2226364776%22%2C%2226364792%22%2C%2226364804%22%2C%2226393648%22%2C%2226459649%22%5D%2C%22flags%22%3A4294967295%2C%22mode%22%3A1%7D%5D%7D%7D%2C%7B%22svc%22%3A%22core%2Fupdate_data_flags%22%2C%22params%22%3A%7B%22spec%22%3A%5B%7B%22type%22%3A%22id%22%2C%22data%22%3A22630230%2C%22flags%22%3A513%2C%22mode%22%3A1%7D%5D%7D%7D%2C%7B%22svc%22%3A%22core%2Fupdate_data_flags%22%2C%22params%22%3A%7B%22spec%22%3A%5B%7B%22type%22%3A%22type%22%2C%22data%22%3A%22avl_unit%22%2C%22flags%22%3A8397079%2C%22mode%22%3A1%7D%5D%7D%7D%2C%7B%22svc%22%3A%22item%2Fupdate_custom_property%22%2C%22params%22%3A%7B%22itemId%22%3A22630230%2C%22name%22%3A%22inf_map%22%2C%22value%22%3A%22%22%7D%7D%2C%7B%22svc%22%3A%22render%2Fset_locale%22%2C%22params%22%3A%7B%22tzOffset%22%3A-134170192%2C%22language%22%3A%22en%22%2C%22flags%22%3A259%2C%22formatDate%22%3A%22%25Y-%25m-%25E%20%25H%3A%25M%3A%25S%22%7D%7D%2C%7B%22svc%22%3A%22core%2Fupdate_data_flags%22%2C%22params%22%3A%7B%22spec%22%3A%5B%7B%22type%22%3A%22type%22%2C%22data%22%3A%22avl_resource%22%2C%22flags%22%3A4097%2C%22mode%22%3A1%7D%5D%7D%7D%2C%7B%22svc%22%3A%22core%2Fupdate_data_flags%22%2C%22params%22%3A%7B%22spec%22%3A%5B%7B%22type%22%3A%22type%22%2C%22data%22%3A%22avl_resource%22%2C%22flags%22%3A1048577%2C%22mode%22%3A1%7D%5D%7D%7D%2C%7B%22svc%22%3A%22core%2Fupdate_data_flags%22%2C%22params%22%3A%7B%22spec%22%3A%5B%7B%22type%22%3A%22type%22%2C%22data%22%3A%22avl_resource%22%2C%22flags%22%3A519%2C%22mode%22%3A1%7D%5D%7D%7D%2C%7B%22svc%22%3A%22core%2Fupdate_data_flags%22%2C%22params%22%3A%7B%22spec%22%3A%5B%7B%22type%22%3A%22type%22%2C%22data%22%3A%22avl_resource%22%2C%22flags%22%3A1031%2C%22mode%22%3A1%7D%5D%7D%7D%2C%7B%22svc%22%3A%22core%2Fupdate_data_flags%22%2C%22params%22%3A%7B%22spec%22%3A%5B%7B%22type%22%3A%22type%22%2C%22data%22%3A%22avl_unit_group%22%2C%22flags%22%3A21%2C%22mode%22%3A1%7D%5D%7D%7D%2C%7B%22svc%22%3A%22core%2Fupdate_data_flags%22%2C%22params%22%3A%7B%22spec%22%3A%5B%7B%22type%22%3A%22type%22%2C%22data%22%3A%22avl_resource%22%2C%22flags%22%3A313%2C%22mode%22%3A1%7D%5D%7D%7D%2C%7B%22svc%22%3A%22core%2Fupdate_data_flags%22%2C%22params%22%3A%7B%22spec%22%3A%5B%7B%22type%22%3A%22type%22%2C%22data%22%3A%22avl_unit%22%2C%22flags%22%3A1%2C%22mode%22%3A1%7D%5D%7D%7D%2C%7B%22svc%22%3A%22core%2Fupdate_data_flags%22%2C%22params%22%3A%7B%22spec%22%3A%5B%7B%22type%22%3A%22type%22%2C%22data%22%3A%22avl_unit_group%22%2C%22flags%22%3A1%2C%22mode%22%3A1%7D%5D%7D%7D%2C%7B%22svc%22%3A%22core%2Fupdate_data_flags%22%2C%22params%22%3A%7B%22spec%22%3A%5B%7B%22type%22%3A%22type%22%2C%22data%22%3A%22user%22%2C%22flags%22%3A1%2C%22mode%22%3A1%7D%5D%7D%7D%2C%7B%22svc%22%3A%22core%2Fupdate_data_flags%22%2C%22params%22%3A%7B%22spec%22%3A%5B%7B%22type%22%3A%22type%22%2C%22data%22%3A%22avl_resource%22%2C%22flags%22%3A769%2C%22mode%22%3A1%7D%5D%7D%7D%2C%7B%22svc%22%3A%22core%2Fupdate_data_flags%22%2C%22params%22%3A%7B%22spec%22%3A%5B%7B%22type%22%3A%22type%22%2C%22data%22%3A%22avl_resource%22%2C%22flags%22%3A66049%2C%22mode%22%3A1%7D%5D%7D%7D%2C%7B%22svc%22%3A%22core%2Fsearch_items%22%2C%22params%22%3A%7B%22spec%22%3A%7B%22itemsType%22%3A%22avl_resource%22%2C%22propName%22%3A%22*%22%2C%22propValueMask%22%3A%22*%22%2C%22sortType%22%3A%22%22%7D%2C%22force%22%3A1%2C%22flags%22%3A1%2C%22from%22%3A0%2C%22to%22%3A4294967295%7D%7D%2C%7B%22svc%22%3A%22core%2Fupdate_data_flags%22%2C%22params%22%3A%7B%22spec%22%3A%5B%7B%22type%22%3A%22type%22%2C%22data%22%3A%22avl_resource%22%2C%22flags%22%3A1%2C%22mode%22%3A1%7D%5D%7D%7D%2C%7B%22svc%22%3A%22core%2Fsearch_items%22%2C%22params%22%3A%7B%22spec%22%3A%7B%22itemsType%22%3A%22avl_retranslator%22%2C%22propName%22%3A%22*%22%2C%22propValueMask%22%3A%22*%22%2C%22sortType%22%3A%22%22%7D%2C%22force%22%3A1%2C%22flags%22%3A1%2C%22from%22%3A0%2C%22to%22%3A4294967295%7D%7D%2C%7B%22svc%22%3A%22core%2Fupdate_data_flags%22%2C%22params%22%3A%7B%22spec%22%3A%5B%7B%22type%22%3A%22type%22%2C%22data%22%3A%22avl_retranslator%22%2C%22flags%22%3A1%2C%22mode%22%3A1%7D%5D%7D%7D%2C%7B%22svc%22%3A%22core%2Fsearch_items%22%2C%22params%22%3A%7B%22spec%22%3A%7B%22itemsType%22%3A%22avl_route%22%2C%22propName%22%3A%22*%22%2C%22propValueMask%22%3A%22*%22%2C%22sortType%22%3A%22%22%7D%2C%22force%22%3A1%2C%22flags%22%3A1%2C%22from%22%3A0%2C%22to%22%3A4294967295%7D%7D%2C%7B%22svc%22%3A%22core%2Fupdate_data_flags%22%2C%22params%22%3A%7B%22spec%22%3A%5B%7B%22type%22%3A%22type%22%2C%22data%22%3A%22avl_route%22%2C%22flags%22%3A1%2C%22mode%22%3A1%7D%5D%7D%7D%2C%7B%22svc%22%3A%22core%2Fupdate_data_flags%22%2C%22params%22%3A%7B%22spec%22%3A%5B%7B%22type%22%3A%22type%22%2C%22data%22%3A%22avl_resource%22%2C%22flags%22%3A33281%2C%22mode%22%3A1%7D%5D%7D%7D%2C%7B%22svc%22%3A%22core%2Fupdate_data_flags%22%2C%22params%22%3A%7B%22spec%22%3A%5B%7B%22type%22%3A%22type%22%2C%22data%22%3A%22avl_resource%22%2C%22flags%22%3A131585%2C%22mode%22%3A1%7D%5D%7D%7D%2C%7B%22svc%22%3A%22core%2Fupdate_data_flags%22%2C%22params%22%3A%7B%22spec%22%3A%5B%7B%22type%22%3A%22type%22%2C%22data%22%3A%22avl_resource%22%2C%22flags%22%3A2097665%2C%22mode%22%3A1%7D%5D%7D%7D%2C%7B%22svc%22%3A%22core%2Fupdate_data_flags%22%2C%22params%22%3A%7B%22spec%22%3A%5B%7B%22type%22%3A%22type%22%2C%22data%22%3A%22avl_resource%22%2C%22flags%22%3A8389121%2C%22mode%22%3A1%7D%5D%7D%7D%2C%7B%22svc%22%3A%22core%2Fupdate_data_flags%22%2C%22params%22%3A%7B%22spec%22%3A%5B%7B%22type%22%3A%22type%22%2C%22data%22%3A%22avl_resource%22%2C%22flags%22%3A8197%2C%22mode%22%3A1%7D%5D%7D%7D%2C%7B%22svc%22%3A%22core%2Fupdate_data_flags%22%2C%22params%22%3A%7B%22spec%22%3A%5B%7B%22type%22%3A%22type%22%2C%22data%22%3A%22user%22%2C%22flags%22%3A2053%2C%22mode%22%3A1%7D%5D%7D%7D%2C%7B%22svc%22%3A%22core%2Fupdate_data_flags%22%2C%22params%22%3A%7B%22spec%22%3A%5B%7B%22type%22%3A%22type%22%2C%22data%22%3A%22avl_resource%22%2C%22flags%22%3A49439%2C%22mode%22%3A1%7D%5D%7D%7D%2C%7B%22svc%22%3A%22core%2Fupdate_data_flags%22%2C%22params%22%3A%7B%22spec%22%3A%5B%7B%22type%22%3A%22type%22%2C%22data%22%3A%22avl_resource%22%2C%22flags%22%3A1%2C%22mode%22%3A1%7D%5D%7D%7D%2C%7B%22svc%22%3A%22core%2Fupdate_data_flags%22%2C%22params%22%3A%7B%22spec%22%3A%5B%7B%22type%22%3A%22type%22%2C%22data%22%3A%22avl_resource%22%2C%22flags%22%3A32769%2C%22mode%22%3A1%7D%5D%7D%7D%2C%7B%22svc%22%3A%22core%2Fupdate_data_flags%22%2C%22params%22%3A%7B%22spec%22%3A%5B%7B%22type%22%3A%22type%22%2C%22data%22%3A%22avl_resource%22%2C%22flags%22%3A458783%2C%22mode%22%3A1%7D%5D%7D%7D%2C%7B%22svc%22%3A%22core%2Fupdate_data_flags%22%2C%22params%22%3A%7B%22spec%22%3A%5B%7B%22type%22%3A%22type%22%2C%22data%22%3A%22avl_resource%22%2C%22flags%22%3A131073%2C%22mode%22%3A1%7D%5D%7D%7D%2C%7B%22svc%22%3A%22core%2Fupdate_data_flags%22%2C%22params%22%3A%7B%22spec%22%3A%5B%7B%22type%22%3A%22type%22%2C%22data%22%3A%22avl_resource%22%2C%22flags%22%3A14680095%2C%22mode%22%3A1%7D%5D%7D%7D%2C%7B%22svc%22%3A%22core%2Fupdate_data_flags%22%2C%22params%22%3A%7B%22spec%22%3A%5B%7B%22type%22%3A%22type%22%2C%22data%22%3A%22avl_resource%22%2C%22flags%22%3A6291487%2C%22mode%22%3A1%7D%5D%7D%7D%2C%7B%22svc%22%3A%22core%2Fget_hw_types%22%2C%22params%22%3A%7B%22includeType%22%3Atrue%7D%7D%5D%2C%22flags%22%3A0%7D&sid=05c6a8472e9f4320d66e2367c25d71ec'
#print(quote(q, safe="=&"))
print(unquote(u))