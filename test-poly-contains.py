from shapely.geometry import Point
import shapely.wkt
import shapely.ops
a = "MULTIPOLYGON (((-69.91401960472092 -15.879619109234454, -69.91391985461757 -15.880370983833814, -69.91360385533363 -15.880857482886482, -69.91261647976671 -15.881291857233407, -69.91157260339287 -15.88188410666612, -69.91119635492782 -15.88220148281215, -69.91071948041963 -15.882389984310294, -69.90950573020524 -15.882605109338272, -69.90858785424604 -15.882625607585679, -69.90792872403136 -15.882769356120832, -69.90674710479499 -15.882184857944763, -69.90611235430168 -15.881699482145336, -69.90563160371549 -15.88169135677066, -69.90524185462783 -15.881834357069863, -69.90444810489606 -15.882544858358473, -69.90396510420618 -15.882787607861758, -69.90272597962024 -15.882943105140155, -69.90215672944946 -15.882941607768942, -69.90127734807112 -15.882835983293942, -69.90087135542865 -15.882860607630903, -69.90072647824434 -15.883006482163353, -69.90034697783072 -15.883782857892529, -69.89905935550479 -15.884653732583672, -69.89888484925636 -15.884714855006507, -69.89848922939439 -15.884619856920835, -69.89634598038265 -15.883607232887412, -69.89600810419063 -15.883387482646185, -69.89550223014379 -15.882899732636531, -69.89497598105663 -15.882553356951801, -69.89349872948276 -15.881897858199522, -69.89335998117815 -15.881885486226167, -69.89325310304821 -15.881964856792647, -69.89311310288736 -15.882477482949414, -69.89297572514954 -15.882604234297899, -69.89275085596717 -15.882528857620626, -69.89257147899053 -15.882197231716816, -69.89245785414658 -15.882116484288245, -69.89219847887665 -15.882101106780622, -69.89179710515225 -15.882220982812042, -69.89163973008942 -15.882333232592543, -69.89154672849867 -15.882534232868524, -69.89160285518756 -15.8832459824161, -69.89156222921349 -15.883827107235161, -69.89118672898434 -15.88437823336875, -69.88969635630178 -15.885129107921953, -69.8875251059988 -15.886824732875084, -69.88559660519911 -15.888085108440976, -69.88473110485654 -15.888520606940403, -69.88303685406754 -15.890195607741077, -69.88276785245438 -15.89056148252638, -69.88266048059666 -15.891004357265217, -69.88271822966254 -15.891517483445055, -69.88282498008874 -15.891802857216021, -69.88325397828844 -15.892320981827822, -69.88381973099575 -15.893485483368295, -69.88371223053497 -15.89374273264093, -69.88365297960127 -15.894148608371554, -69.88377397888597 -15.894388856860187, -69.88386997971577 -15.89479285840366, -69.88352260398494 -15.895412483199491, -69.883450730167 -15.896178732562419, -69.88350435494198 -15.89652510914641, -69.88341660449264 -15.896805607692613, -69.88323098082509 -15.896977609329154, -69.88328623067497 -15.897931108333921, -69.88310235349076 -15.898369108747316, -69.88318922889977 -15.898567858020158, -69.8834766036623 -15.898818107869317, -69.88370273099622 -15.899349358086338, -69.8840739783314 -15.900914358310956, -69.88437223039409 -15.901849483266972, -69.88441997809946 -15.902477731661918, -69.88418898003738 -15.903064731751897, -69.88324897895717 -15.904178106834138, -69.88265397939762 -15.905150857625925, -69.88252522975552 -15.90571560758917, -69.88229022881097 -15.905898857046564, -69.88152297940195 -15.906288233814905, -69.88106860593138 -15.906815607953886, -69.88079122983135 -15.907461733072465, -69.8805519768922 -15.907833608134467, -69.87950622812991 -15.908974357680393, -69.87884798104943 -15.909453234079422, -69.87772722702988 -15.909817857907795, -69.87732960257904 -15.910063982566667, -69.87713648036423 -15.910342356914212, -69.87707573026069 -15.910824858480396, -69.87710597715908 -15.91111410743008, -69.87731947711217 -15.911439858062975, -69.87729460366302 -15.911641858384995, -69.87716410483955 -15.91179723425489, -69.87663235370013 -15.912060982927981, -69.87546435559551 -15.912233232777453, -69.87476173056939 -15.912606482902845, -69.8744131047809 -15.913479482691912, -69.8739971035834 -15.913837857131341, -69.87335535546526 -15.913931609656004, -69.87278785357654 -15.91386798262124, -69.87260285223982 -15.913797609771846, -69.87212397943807 -15.913816482044977, -69.87123773083657 -15.91412760790274, -69.87087110421804 -15.914416982757528, -69.87029135446238 -15.915997482797536, -69.86999398103733 -15.916488982980125, -69.8696418514902 -15.916642729278463, -69.86929935368221 -15.916624482034194, -69.86902910291076 -15.916321483349746, -69.86873172948566 -15.915727982959993, -69.86862447813712 -15.91563598501267, -69.86837022900284 -15.915853234239306, -69.86826710374379 -15.916357357306138, -69.86828972978714 -15.917728483482675, -69.86814035329462 -15.918301357021958, -69.86784010563633 -15.918788232890563, -69.86743648000953 -15.919201233050444, -69.86722823029856 -15.919686107927474, -69.86708085389824 -15.920231357890826, -69.86686797807471 -15.92233198353415, -69.86601760612757 -15.924400606802521, -69.86595047983076 -15.925105857849017, -69.86590098024601 -15.92743435820904, -69.86579522896659 -15.927813982729049, -69.8656673561635 -15.928032857930019, -69.8652778525908 -15.928372483303404, -69.86497197877378 -15.928497607778354, -69.86427785234099 -15.928638733890407, -69.86368072948204 -15.928501107939724, -69.8629071038797 -15.928168732900643, -69.86270398120371 -15.928140733408098, -69.86251947989007 -15.928186607825637, -69.86241910205983 -15.928463733014837, -69.86244498005175 -15.928639357120575, -69.86274910558672 -15.929118107614556, -69.86351135386587 -15.929715982306673, -69.86352260618327 -15.930070859282692, -69.86330398009454 -15.930156232823833, -69.86236522727336 -15.930184859143878, -69.86179923084977 -15.930558859303858, -69.86110948051804 -15.931207982762144, -69.86105772813158 -15.931237357318137, -69.86098435514384 -15.932091858952104, -69.86104060503988 -15.933431482776655, -69.86151210609874 -15.934584107870252, -69.8626648543995 -15.935736607058741, -69.86434123116283 -15.937360733211223, -69.8645656057181 -15.93754935701719, -69.86656710538756 -15.939232483192482, -69.86723047680505 -15.939415982661444, -69.87121460566948 -15.938437729817338, -69.87387647841672 -15.938775356897166, -69.87963948067744 -15.93971835811567, -69.88309735415953 -15.941185358317567, -69.88653710270505 -15.94290823182939, -69.88948897803385 -15.945533857401529, -69.89111310238775 -15.947524608373953, -69.89619510292164 -15.948624857850861, -69.89865733876513 -15.949243274857224, -69.89958785289707 -15.949476982576641, -69.90258947782212 -15.951670608012082, -69.90686210470233 -15.953749107635188, -69.91125022971431 -15.956289481973954, -69.91127935425874 -15.956313358074967, -69.91387835540172 -15.95843110770943, -69.91436797959852 -15.958830107223603, -69.91944897738836 -15.962756232514096, -69.92291335386813 -15.966220608094543, -69.9278787303191 -15.970377734145075, -69.92909110547009 -15.971474609365657, -69.92911948087931 -15.971601608927072, -69.92955322749941 -15.973553359000277, -69.92959035601007 -15.973581234386414, -69.9304756018675 -15.974245109424203, -69.93093885524394 -15.974592609261435, -69.93153535397335 -15.97486798436995, -69.93694373016899 -15.977364110265455, -69.93971523117295 -15.980481984256128, -69.94191310590509 -15.983172984245755, -69.94306085217653 -15.984620234436248, -69.94306168854604 -15.984621143650827, -69.94444997828384 -15.98612998391161, -69.94478997957384 -15.986279983634288, -69.94534998021737 -15.986749983724735, -69.94577998116112 -15.986989983101182, -69.94625997721613 -15.987079980956308, -69.94674997732955 -15.987019983585355, -69.94709997998007 -15.986889983885588, -69.94824998085186 -15.986199984441669, -69.94889998024985 -15.985999985111164, -69.94933997805748 -15.98593998414293, -69.94978997812495 -15.985779983959047, -69.95007997980719 -15.985559983706251, -69.95067997869802 -15.98512998366175, -69.9515899810927 -15.984309983618799, -69.9524099811357 -15.983679984243848, -69.95342998050916 -15.982709983578841, -69.95435998022884 -15.982179985218124, -69.95529998130905 -15.981849984389214, -69.95558998029333 -15.981529984021504, -69.95594997890832 -15.980759983586324, -69.95610997999154 -15.980589983840614, -69.95720998035625 -15.980269984372226, -69.95763998130008 -15.980019983635314, -69.95783997703329 -15.979719984189899, -69.95790998116064 -15.979259983661278, -69.95763998130008 -15.978019984034972, -69.95768998000852 -15.977429983806642, -69.95804998132155 -15.97707998295482, -69.95820998420338 -15.977059985629806, -69.95925997956437 -15.977489982976294, -69.95982998066904 -15.977649984059495, -69.96070997628436 -15.977699984566584, -69.96177997976224 -15.977669984082468, -69.9630399812101 -15.977529983921556, -69.96399997691736 -15.97728998364579, -69.96483997608395 -15.977149980786919, -69.96568997571177 -15.977149985283575, -69.96636998098978 -15.976729983901578, -69.96665997817541 -15.976289984295306, -69.96670997688386 -15.975819984204863, -69.96686997796706 -15.975519983860124, -69.96709985277596 -15.975262233665092, -69.9671999778966 -15.97514998388459, -69.96769998026986 -15.974879983124652, -69.96784997909322 -15.974719983840146, -69.96785997775571 -15.974409984832901, -69.96756997877144 -15.973619984374748, -69.96792997828584 -15.972939983593335, -69.96801997883892 -15.972509984448152, -69.96782997996957 -15.971389984060464, -69.96784997909322 -15.971199983392466, -69.96809997803155 -15.970649984109457, -69.96799997791663 -15.970469983902605, -69.96794997920811 -15.970189982681516, -69.96802997930007 -15.969809983144158, -69.96789997960035 -15.968999983562354, -69.96791997962333 -15.968419983795172, -69.96801997883892 -15.96806998384261, -69.96828997690083 -15.967609984213368, -69.96854997989759 -15.967319984329775, -69.96903997821238 -15.966899983847158, -69.96927998028684 -15.966459984240828, -69.96932997899529 -15.965979982789916, -69.96917997837329 -15.965229984176402, -69.96916997971073 -15.96481998415487, -69.96975997993906 -15.963479982615068, -69.96962998023935 -15.962819982755947, -69.96970998123061 -15.962229983426937, -69.96938997906425 -15.96175998333649, -69.96930997987164 -15.96127998188558, -69.96938997906425 -15.959569983967526, -69.96946997915619 -15.959399983322497, -69.96981998000803 -15.959199983092674, -69.97044997848366 -15.959069983392965, -69.97084997804397 -15.958879982724964, -69.97088997988861 -15.958699983417432, -69.97083998118012 -15.957959981667784, -69.97096998087989 -15.957469983353006, -69.97095998041874 -15.95702998284736, -69.97088997988861 -15.956799983032738, -69.97069998101927 -15.95655998275697, -69.97003998026082 -15.956139983173612, -69.96974997947791 -15.955869983313049, -69.96971997809447 -15.95563998349837, -69.96978997772527 -15.955449982830373, -69.96983998093032 -15.954839981679752, -69.96891997717516 -15.95383998322859, -69.96825997911469 -15.95341998274597, -69.96808997936904 -15.953119983300553, -69.96778997812493 -15.952209982704517, -69.96756997877144 -15.951749983075217, -69.96703997771277 -15.95136998263854, -69.96591998092237 -15.949929982782407, -69.96548997997854 -15.949819982206348, -69.96528997974872 -15.949709983428933, -69.96455997935954 -15.948909983408953, -69.96359997825634 -15.948549982995244, -69.9634599780955 -15.94836998278845, -69.96354997864853 -15.947999981913595, -69.96353997998602 -15.947769982998295, -69.96312997906523 -15.947269982423675, -69.9629499797577 -15.947169983208086, -69.96245997964428 -15.947079981755733, -69.96217997932257 -15.946869981964028, -69.96195998086834 -15.94595998316663, -69.96216998066006 -15.945219983215623, -69.96218997798506 -15.944809983194148, -69.96212998061407 -15.944449982780439, -69.96123998094032 -15.94354998354487, -69.96074997812893 -15.943239982738987, -69.96068998075799 -15.943099982578076, -69.960709978083 -15.94266998343295, -69.96061998022788 -15.942499982787922, -69.96002997999953 -15.94218998288136, -69.95971997829433 -15.941699981868624, -69.95954997854864 -15.94107998385414, -69.95935997967928 -15.940839981779675, -69.95935997967928 -15.940599982403228, -69.9590499788734 -15.940189982381753, -69.95885998000404 -15.94000998307422, -69.95873997896683 -15.939709982729482, -69.95867997799854 -15.939349984114415, -69.95879997903573 -15.938989982801445, -69.95878998037324 -15.938629983287056, -69.95872997850569 -15.93820998280444, -69.95866998113468 -15.937909983359019, -69.95804998132155 -15.93725998396104, -69.95779998058458 -15.93677998251013, -69.95772998005452 -15.935999983412444, -69.95760997901726 -15.93545998279194, -69.95759997855612 -15.93480998249464, -69.9577899783248 -15.934509983049225, -69.95790998116064 -15.934089982566602, -69.95796998033029 -15.933849983190099, -69.95814997873849 -15.93348998277645, -69.95833998030582 -15.93306998229383, -69.95857997968227 -15.932769982848356, -69.95863997705328 -15.932349982365734, -69.95863997705328 -15.932169983058202, -69.95844997818392 -15.93180998264455, -69.95850998005146 -15.931389983061251, -69.95856997742248 -15.931029982647544, -69.95862998108873 -15.930309982719507, -69.95868998025833 -15.929959981867624, -69.95868998025833 -15.929539983183645, -69.95886997686789 -15.929119983600344, -69.95880998129559 -15.928639982149434, -69.95880998129559 -15.92839998277293, -69.95886997686789 -15.92797998318963, -69.95895998011895 -15.927459982592097, -69.95903998021089 -15.926999982063478, -69.95922797718934 -15.924817108023094, -69.95920697981825 -15.923481857601587, -69.95905023068354 -15.922034233293173, -69.95884598025776 -15.920148732677829, -69.95883747716776 -15.919925608180222, -69.95875810480265 -15.91783648306722, -69.95865622870195 -15.915156231774633, -69.95822997972977 -15.914771357911775, -69.957595605153 -15.914198732585419, -69.95673322905526 -15.914109483865559, -69.95535835630307 -15.91436848321888, -69.95380560484477 -15.914660983217743, -69.95291197820518 -15.914597232076572, -69.95192610810335 -15.914305109792963, -69.95100547752071 -15.914368108201586, -69.95021935583856 -15.914763982571683, -69.94880122839396 -15.915172986144341, -69.94827672848815 -15.915102982016945, -69.94782173088811 -15.915042482824274, -69.9476226030007 -15.914926231960008, -69.94740497875671 -15.914799358303695, -69.94649723006307 -15.91426973316163, -69.94543035712525 -15.91393860638152, -69.94443685537652 -15.914196108363683, -69.94230297909917 -15.915042482824274, -69.9402794802138 -15.916109232555016, -69.93836635332451 -15.91662435702841, -69.9368947279093 -15.916771353914783, -69.93560697877899 -15.916513982334378, -69.93350972829131 -15.915766482037498, -69.93193447759404 -15.915036233435387, -69.92941135584935 -15.914065857753087, -69.92876760494096 -15.913830106773956, -69.92862885303907 -15.913779485734608, -69.92862622791802 -15.913792105920889, -69.92399235416376 -15.912454733099423, -69.92261722870211 -15.912021482005741, -69.92107260441713 -15.911644731718923, -69.92033785380886 -15.911286858201889, -69.92020610312909 -15.911060733565932, -69.92014960591956 -15.910439106879208, -69.92013072825046 -15.908310607648387, -69.91999885256496 -15.904467856706162, -69.92009223097165 -15.90148885782446, -69.9204248542236 -15.897792983259535, -69.92070610460303 -15.895591607466656, -69.92166660572923 -15.891762483052103, -69.92310748062567 -15.887226108398123, -69.9236011059063 -15.883957357845757, -69.92355460466126 -15.883542357593683, -69.92347660466152 -15.882847607930728, -69.92308010526261 -15.882302732984668, -69.92239435421601 -15.881822814271404, -69.9210819807488 -15.880904359148813, -69.9202097282963 -15.87952810593731, -69.91946347985566 -15.879978482820661, -69.9189167298232 -15.88008285813737, -69.91835772832644 -15.880068358368021, -69.91780760313833 -15.879967484112058, -69.91710710321018 -15.879707483813261, -69.91577735574032 -15.879633358092974, -69.91547160602975 -15.879483983399039, -69.9151181041172 -15.879397858923994, -69.9142026041668 -15.879479232280687, -69.91401960472092 -15.879619109234454)))"
poly = shapely.wkt.loads(a)
latitud = -15.87970748
longitud = -69.921666

print(poly.contains(Point(longitud, latitud)))