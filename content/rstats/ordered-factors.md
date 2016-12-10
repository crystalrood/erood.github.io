Title: Ordered Factors
Slug: ordered-factors
Summary: Ordered Factors
Date: 2016-05-01 12:00
Category: R Stats
Tags: Basics
Authors: Chris Albon




```R
# Generate some fake data about education in 1000 observations
education <- c("some high school", "high school", "college", "masters", "phd")
obs <- sample(education, 1000, replace = TRUE)
```


```R
obs
```




       [1] "college"          "college"          "college"         
       [4] "phd"              "high school"      "college"         
       [7] "phd"              "masters"          "high school"     
      [10] "some high school" "high school"      "masters"         
      [13] "high school"      "phd"              "some high school"
      [16] "masters"          "some high school" "high school"     
      [19] "phd"              "college"          "college"         
      [22] "phd"              "college"          "high school"     
      [25] "high school"      "college"          "high school"     
      [28] "college"          "college"          "high school"     
      [31] "high school"      "phd"              "some high school"
      [34] "some high school" "high school"      "high school"     
      [37] "phd"              "phd"              "college"         
      [40] "some high school" "masters"          "phd"             
      [43] "college"          "some high school" "phd"             
      [46] "phd"              "some high school" "high school"     
      [49] "high school"      "masters"          "some high school"
      [52] "masters"          "some high school" "masters"         
      [55] "high school"      "some high school" "some high school"
      [58] "masters"          "masters"          "masters"         
      [61] "phd"              "phd"              "some high school"
      [64] "masters"          "masters"          "high school"     
      [67] "college"          "college"          "phd"             
      [70] "some high school" "high school"      "college"         
      [73] "phd"              "phd"              "high school"     
      [76] "college"          "some high school" "phd"             
      [79] "college"          "phd"              "masters"         
      [82] "phd"              "masters"          "masters"         
      [85] "college"          "college"          "college"         
      [88] "high school"      "college"          "phd"             
      [91] "some high school" "high school"      "masters"         
      [94] "masters"          "phd"              "some high school"
      [97] "masters"          "phd"              "some high school"
     [100] "masters"          "some high school" "phd"             
     [103] "masters"          "masters"          "masters"         
     [106] "some high school" "high school"      "phd"             
     [109] "phd"              "some high school" "masters"         
     [112] "phd"              "phd"              "college"         
     [115] "masters"          "college"          "college"         
     [118] "college"          "college"          "some high school"
     [121] "phd"              "high school"      "high school"     
     [124] "high school"      "phd"              "phd"             
     [127] "college"          "high school"      "phd"             
     [130] "high school"      "phd"              "high school"     
     [133] "phd"              "phd"              "college"         
     [136] "high school"      "high school"      "high school"     
     [139] "masters"          "masters"          "phd"             
     [142] "masters"          "college"          "masters"         
     [145] "college"          "masters"          "phd"             
     [148] "high school"      "masters"          "phd"             
     [151] "masters"          "college"          "high school"     
     [154] "college"          "masters"          "some high school"
     [157] "college"          "college"          "phd"             
     [160] "high school"      "masters"          "phd"             
     [163] "masters"          "some high school" "college"         
     [166] "some high school" "high school"      "some high school"
     [169] "college"          "high school"      "phd"             
     [172] "masters"          "phd"              "some high school"
     [175] "some high school" "phd"              "phd"             
     [178] "masters"          "phd"              "college"         
     [181] "high school"      "some high school" "some high school"
     [184] "college"          "high school"      "high school"     
     [187] "phd"              "high school"      "masters"         
     [190] "some high school" "high school"      "masters"         
     [193] "high school"      "college"          "college"         
     [196] "masters"          "some high school" "masters"         
     [199] "some high school" "college"          "phd"             
     [202] "some high school" "college"          "high school"     
     [205] "phd"              "masters"          "phd"             
     [208] "college"          "some high school" "some high school"
     [211] "high school"      "some high school" "some high school"
     [214] "phd"              "masters"          "some high school"
     [217] "some high school" "college"          "masters"         
     [220] "college"          "masters"          "some high school"
     [223] "phd"              "phd"              "high school"     
     [226] "masters"          "college"          "some high school"
     [229] "phd"              "college"          "some high school"
     [232] "college"          "some high school" "phd"             
     [235] "high school"      "phd"              "masters"         
     [238] "high school"      "phd"              "masters"         
     [241] "high school"      "masters"          "masters"         
     [244] "masters"          "college"          "some high school"
     [247] "phd"              "masters"          "masters"         
     [250] "some high school" "phd"              "high school"     
     [253] "some high school" "some high school" "college"         
     [256] "some high school" "masters"          "high school"     
     [259] "high school"      "some high school" "high school"     
     [262] "high school"      "high school"      "phd"             
     [265] "masters"          "high school"      "college"         
     [268] "some high school" "masters"          "high school"     
     [271] "phd"              "some high school" "high school"     
     [274] "high school"      "masters"          "high school"     
     [277] "masters"          "phd"              "masters"         
     [280] "phd"              "phd"              "college"         
     [283] "masters"          "some high school" "masters"         
     [286] "phd"              "masters"          "college"         
     [289] "masters"          "high school"      "some high school"
     [292] "phd"              "phd"              "masters"         
     [295] "phd"              "high school"      "college"         
     [298] "masters"          "masters"          "masters"         
     [301] "phd"              "college"          "college"         
     [304] "phd"              "high school"      "masters"         
     [307] "high school"      "masters"          "some high school"
     [310] "college"          "phd"              "some high school"
     [313] "college"          "some high school" "college"         
     [316] "high school"      "masters"          "college"         
     [319] "masters"          "college"          "college"         
     [322] "college"          "masters"          "some high school"
     [325] "masters"          "masters"          "masters"         
     [328] "masters"          "masters"          "phd"             
     [331] "college"          "some high school" "some high school"
     [334] "masters"          "high school"      "high school"     
     [337] "some high school" "phd"              "masters"         
     [340] "some high school" "phd"              "some high school"
     [343] "masters"          "phd"              "college"         
     [346] "some high school" "phd"              "high school"     
     [349] "masters"          "college"          "college"         
     [352] "phd"              "masters"          "high school"     
     [355] "high school"      "high school"      "masters"         
     [358] "phd"              "phd"              "masters"         
     [361] "phd"              "masters"          "high school"     
     [364] "some high school" "college"          "high school"     
     [367] "some high school" "some high school" "phd"             
     [370] "some high school" "phd"              "phd"             
     [373] "some high school" "masters"          "high school"     
     [376] "college"          "masters"          "some high school"
     [379] "some high school" "some high school" "some high school"
     [382] "masters"          "phd"              "masters"         
     [385] "masters"          "high school"      "masters"         
     [388] "masters"          "college"          "phd"             
     [391] "high school"      "some high school" "masters"         
     [394] "masters"          "masters"          "masters"         
     [397] "college"          "phd"              "high school"     
     [400] "masters"          "high school"      "masters"         
     [403] "college"          "high school"      "some high school"
     [406] "phd"              "phd"              "masters"         
     [409] "phd"              "masters"          "masters"         
     [412] "phd"              "masters"          "high school"     
     [415] "college"          "masters"          "college"         
     [418] "masters"          "phd"              "phd"             
     [421] "college"          "college"          "some high school"
     [424] "masters"          "some high school" "phd"             
     [427] "college"          "masters"          "some high school"
     [430] "college"          "some high school" "college"         
     [433] "masters"          "masters"          "some high school"
     [436] "masters"          "high school"      "some high school"
     [439] "phd"              "phd"              "college"         
     [442] "phd"              "high school"      "some high school"
     [445] "some high school" "some high school" "phd"             
     [448] "high school"      "masters"          "masters"         
     [451] "some high school" "masters"          "some high school"
     [454] "college"          "masters"          "masters"         
     [457] "some high school" "phd"              "college"         
     [460] "masters"          "high school"      "some high school"
     [463] "some high school" "college"          "phd"             
     [466] "high school"      "masters"          "high school"     
     [469] "high school"      "some high school" "phd"             
     [472] "high school"      "some high school" "some high school"
     [475] "college"          "college"          "masters"         
     [478] "phd"              "masters"          "masters"         
     [481] "high school"      "high school"      "phd"             
     [484] "college"          "some high school" "phd"             
     [487] "masters"          "phd"              "some high school"
     [490] "high school"      "college"          "some high school"
     [493] "high school"      "phd"              "college"         
     [496] "phd"              "masters"          "phd"             
     [499] "some high school" "phd"              "high school"     
     [502] "phd"              "college"          "some high school"
     [505] "masters"          "phd"              "some high school"
     [508] "high school"      "phd"              "masters"         
     [511] "masters"          "some high school" "high school"     
     [514] "some high school" "masters"          "some high school"
     [517] "some high school" "phd"              "phd"             
     [520] "some high school" "phd"              "high school"     
     [523] "some high school" "masters"          "college"         
     [526] "high school"      "high school"      "phd"             
     [529] "high school"      "college"          "phd"             
     [532] "masters"          "high school"      "college"         
     [535] "masters"          "college"          "college"         
     [538] "college"          "some high school" "college"         
     [541] "phd"              "phd"              "college"         
     [544] "college"          "phd"              "college"         
     [547] "masters"          "college"          "masters"         
     [550] "phd"              "college"          "college"         
     [553] "college"          "some high school" "high school"     
     [556] "masters"          "phd"              "some high school"
     [559] "masters"          "masters"          "high school"     
     [562] "high school"      "phd"              "phd"             
     [565] "college"          "college"          "some high school"
     [568] "college"          "college"          "masters"         
     [571] "high school"      "phd"              "phd"             
     [574] "phd"              "masters"          "some high school"
     [577] "college"          "masters"          "college"         
     [580] "phd"              "masters"          "college"         
     [583] "college"          "phd"              "phd"             
     [586] "some high school" "phd"              "college"         
     [589] "high school"      "phd"              "some high school"
     [592] "masters"          "masters"          "masters"         
     [595] "college"          "masters"          "college"         
     [598] "college"          "college"          "high school"     
     [601] "masters"          "masters"          "phd"             
     [604] "phd"              "phd"              "college"         
     [607] "college"          "phd"              "phd"             
     [610] "phd"              "college"          "college"         
     [613] "masters"          "phd"              "masters"         
     [616] "high school"      "phd"              "college"         
     [619] "masters"          "high school"      "masters"         
     [622] "masters"          "masters"          "college"         
     [625] "phd"              "phd"              "masters"         
     [628] "some high school" "college"          "masters"         
     [631] "masters"          "college"          "high school"     
     [634] "some high school" "college"          "college"         
     [637] "college"          "phd"              "college"         
     [640] "masters"          "college"          "some high school"
     [643] "some high school" "phd"              "high school"     
     [646] "masters"          "college"          "high school"     
     [649] "high school"      "college"          "some high school"
     [652] "high school"      "phd"              "high school"     
     [655] "masters"          "masters"          "high school"     
     [658] "high school"      "some high school" "masters"         
     [661] "phd"              "high school"      "phd"             
     [664] "masters"          "masters"          "high school"     
     [667] "high school"      "masters"          "masters"         
     [670] "college"          "phd"              "some high school"
     [673] "masters"          "phd"              "some high school"
     [676] "high school"      "college"          "some high school"
     [679] "some high school" "high school"      "phd"             
     [682] "phd"              "college"          "phd"             
     [685] "some high school" "masters"          "high school"     
     [688] "college"          "masters"          "college"         
     [691] "college"          "masters"          "some high school"
     [694] "some high school" "college"          "some high school"
     [697] "high school"      "high school"      "phd"             
     [700] "some high school" "masters"          "phd"             
     [703] "high school"      "some high school" "college"         
     [706] "college"          "college"          "college"         
     [709] "some high school" "college"          "college"         
     [712] "some high school" "college"          "masters"         
     [715] "phd"              "college"          "phd"             
     [718] "high school"      "college"          "masters"         
     [721] "phd"              "some high school" "some high school"
     [724] "some high school" "masters"          "college"         
     [727] "college"          "some high school" "college"         
     [730] "masters"          "masters"          "high school"     
     [733] "phd"              "phd"              "college"         
     [736] "phd"              "college"          "college"         
     [739] "masters"          "some high school" "masters"         
     [742] "masters"          "high school"      "some high school"
     [745] "high school"      "phd"              "high school"     
     [748] "some high school" "masters"          "high school"     
     [751] "some high school" "phd"              "phd"             
     [754] "high school"      "college"          "high school"     
     [757] "college"          "college"          "masters"         
     [760] "phd"              "masters"          "phd"             
     [763] "high school"      "high school"      "high school"     
     [766] "college"          "masters"          "some high school"
     [769] "high school"      "phd"              "some high school"
     [772] "masters"          "some high school" "masters"         
     [775] "phd"              "some high school" "some high school"
     [778] "masters"          "high school"      "phd"             
     [781] "phd"              "some high school" "college"         
     [784] "some high school" "phd"              "some high school"
     [787] "masters"          "masters"          "masters"         
     [790] "college"          "high school"      "phd"             
     [793] "high school"      "college"          "some high school"
     [796] "high school"      "masters"          "phd"             
     [799] "college"          "some high school" "high school"     
     [802] "phd"              "college"          "high school"     
     [805] "masters"          "some high school" "college"         
     [808] "some high school" "high school"      "phd"             
     [811] "high school"      "high school"      "masters"         
     [814] "some high school" "some high school" "phd"             
     [817] "masters"          "college"          "high school"     
     [820] "masters"          "college"          "some high school"
     [823] "high school"      "high school"      "phd"             
     [826] "college"          "college"          "college"         
     [829] "college"          "masters"          "masters"         
     [832] "high school"      "some high school" "phd"             
     [835] "college"          "some high school" "some high school"
     [838] "high school"      "high school"      "college"         
     [841] "phd"              "high school"      "college"         
     [844] "phd"              "high school"      "college"         
     [847] "masters"          "college"          "college"         
     [850] "some high school" "some high school" "high school"     
     [853] "high school"      "high school"      "high school"     
     [856] "masters"          "high school"      "high school"     
     [859] "phd"              "some high school" "phd"             
     [862] "college"          "some high school" "college"         
     [865] "masters"          "phd"              "college"         
     [868] "phd"              "phd"              "some high school"
     [871] "high school"      "masters"          "some high school"
     [874] "masters"          "college"          "high school"     
     [877] "phd"              "high school"      "masters"         
     [880] "masters"          "some high school" "college"         
     [883] "some high school" "college"          "masters"         
     [886] "college"          "college"          "some high school"
     [889] "phd"              "phd"              "college"         
     [892] "phd"              "phd"              "masters"         
     [895] "college"          "phd"              "masters"         
     [898] "some high school" "high school"      "college"         
     [901] "high school"      "college"          "some high school"
     [904] "high school"      "masters"          "college"         
     [907] "masters"          "college"          "college"         
     [910] "some high school" "college"          "some high school"
     [913] "masters"          "phd"              "high school"     
     [916] "college"          "some high school" "phd"             
     [919] "high school"      "masters"          "some high school"
     [922] "phd"              "high school"      "some high school"
     [925] "phd"              "high school"      "phd"             
     [928] "high school"      "some high school" "some high school"
     [931] "high school"      "phd"              "masters"         
     [934] "some high school" "high school"      "some high school"
     [937] "phd"              "masters"          "high school"     
     [940] "college"          "some high school" "some high school"
     [943] "masters"          "some high school" "phd"             
     [946] "some high school" "phd"              "some high school"
     [949] "college"          "phd"              "phd"             
     [952] "masters"          "college"          "high school"     
     [955] "high school"      "masters"          "phd"             
     [958] "high school"      "phd"              "college"         
     [961] "masters"          "masters"          "phd"             
     [964] "college"          "masters"          "college"         
     [967] "college"          "some high school" "phd"             
     [970] "college"          "some high school" "some high school"
     [973] "high school"      "masters"          "some high school"
     [976] "phd"              "college"          "high school"     
     [979] "phd"              "high school"      "high school"     
     [982] "phd"              "masters"          "masters"         
     [985] "some high school" "high school"      "phd"             
     [988] "phd"              "college"          "phd"             
     [991] "college"          "high school"      "some high school"
     [994] "some high school" "college"          "some high school"
     [997] "high school"      "masters"          "masters"         
    [1000] "phd"             




```R
# Turn the same into a ordered factor
obs.ordered <- ordered(obs)
```


```R
obs.ordered
```




       [1] college          college          college          phd             
       [5] high school      college          phd              masters         
       [9] high school      some high school high school      masters         
      [13] high school      phd              some high school masters         
      [17] some high school high school      phd              college         
      [21] college          phd              college          high school     
      [25] high school      college          high school      college         
      [29] college          high school      high school      phd             
      [33] some high school some high school high school      high school     
      [37] phd              phd              college          some high school
      [41] masters          phd              college          some high school
      [45] phd              phd              some high school high school     
      [49] high school      masters          some high school masters         
      [53] some high school masters          high school      some high school
      [57] some high school masters          masters          masters         
      [61] phd              phd              some high school masters         
      [65] masters          high school      college          college         
      [69] phd              some high school high school      college         
      [73] phd              phd              high school      college         
      [77] some high school phd              college          phd             
      [81] masters          phd              masters          masters         
      [85] college          college          college          high school     
      [89] college          phd              some high school high school     
      [93] masters          masters          phd              some high school
      [97] masters          phd              some high school masters         
     [101] some high school phd              masters          masters         
     [105] masters          some high school high school      phd             
     [109] phd              some high school masters          phd             
     [113] phd              college          masters          college         
     [117] college          college          college          some high school
     [121] phd              high school      high school      high school     
     [125] phd              phd              college          high school     
     [129] phd              high school      phd              high school     
     [133] phd              phd              college          high school     
     [137] high school      high school      masters          masters         
     [141] phd              masters          college          masters         
     [145] college          masters          phd              high school     
     [149] masters          phd              masters          college         
     [153] high school      college          masters          some high school
     [157] college          college          phd              high school     
     [161] masters          phd              masters          some high school
     [165] college          some high school high school      some high school
     [169] college          high school      phd              masters         
     [173] phd              some high school some high school phd             
     [177] phd              masters          phd              college         
     [181] high school      some high school some high school college         
     [185] high school      high school      phd              high school     
     [189] masters          some high school high school      masters         
     [193] high school      college          college          masters         
     [197] some high school masters          some high school college         
     [201] phd              some high school college          high school     
     [205] phd              masters          phd              college         
     [209] some high school some high school high school      some high school
     [213] some high school phd              masters          some high school
     [217] some high school college          masters          college         
     [221] masters          some high school phd              phd             
     [225] high school      masters          college          some high school
     [229] phd              college          some high school college         
     [233] some high school phd              high school      phd             
     [237] masters          high school      phd              masters         
     [241] high school      masters          masters          masters         
     [245] college          some high school phd              masters         
     [249] masters          some high school phd              high school     
     [253] some high school some high school college          some high school
     [257] masters          high school      high school      some high school
     [261] high school      high school      high school      phd             
     [265] masters          high school      college          some high school
     [269] masters          high school      phd              some high school
     [273] high school      high school      masters          high school     
     [277] masters          phd              masters          phd             
     [281] phd              college          masters          some high school
     [285] masters          phd              masters          college         
     [289] masters          high school      some high school phd             
     [293] phd              masters          phd              high school     
     [297] college          masters          masters          masters         
     [301] phd              college          college          phd             
     [305] high school      masters          high school      masters         
     [309] some high school college          phd              some high school
     [313] college          some high school college          high school     
     [317] masters          college          masters          college         
     [321] college          college          masters          some high school
     [325] masters          masters          masters          masters         
     [329] masters          phd              college          some high school
     [333] some high school masters          high school      high school     
     [337] some high school phd              masters          some high school
     [341] phd              some high school masters          phd             
     [345] college          some high school phd              high school     
     [349] masters          college          college          phd             
     [353] masters          high school      high school      high school     
     [357] masters          phd              phd              masters         
     [361] phd              masters          high school      some high school
     [365] college          high school      some high school some high school
     [369] phd              some high school phd              phd             
     [373] some high school masters          high school      college         
     [377] masters          some high school some high school some high school
     [381] some high school masters          phd              masters         
     [385] masters          high school      masters          masters         
     [389] college          phd              high school      some high school
     [393] masters          masters          masters          masters         
     [397] college          phd              high school      masters         
     [401] high school      masters          college          high school     
     [405] some high school phd              phd              masters         
     [409] phd              masters          masters          phd             
     [413] masters          high school      college          masters         
     [417] college          masters          phd              phd             
     [421] college          college          some high school masters         
     [425] some high school phd              college          masters         
     [429] some high school college          some high school college         
     [433] masters          masters          some high school masters         
     [437] high school      some high school phd              phd             
     [441] college          phd              high school      some high school
     [445] some high school some high school phd              high school     
     [449] masters          masters          some high school masters         
     [453] some high school college          masters          masters         
     [457] some high school phd              college          masters         
     [461] high school      some high school some high school college         
     [465] phd              high school      masters          high school     
     [469] high school      some high school phd              high school     
     [473] some high school some high school college          college         
     [477] masters          phd              masters          masters         
     [481] high school      high school      phd              college         
     [485] some high school phd              masters          phd             
     [489] some high school high school      college          some high school
     [493] high school      phd              college          phd             
     [497] masters          phd              some high school phd             
     [501] high school      phd              college          some high school
     [505] masters          phd              some high school high school     
     [509] phd              masters          masters          some high school
     [513] high school      some high school masters          some high school
     [517] some high school phd              phd              some high school
     [521] phd              high school      some high school masters         
     [525] college          high school      high school      phd             
     [529] high school      college          phd              masters         
     [533] high school      college          masters          college         
     [537] college          college          some high school college         
     [541] phd              phd              college          college         
     [545] phd              college          masters          college         
     [549] masters          phd              college          college         
     [553] college          some high school high school      masters         
     [557] phd              some high school masters          masters         
     [561] high school      high school      phd              phd             
     [565] college          college          some high school college         
     [569] college          masters          high school      phd             
     [573] phd              phd              masters          some high school
     [577] college          masters          college          phd             
     [581] masters          college          college          phd             
     [585] phd              some high school phd              college         
     [589] high school      phd              some high school masters         
     [593] masters          masters          college          masters         
     [597] college          college          college          high school     
     [601] masters          masters          phd              phd             
     [605] phd              college          college          phd             
     [609] phd              phd              college          college         
     [613] masters          phd              masters          high school     
     [617] phd              college          masters          high school     
     [621] masters          masters          masters          college         
     [625] phd              phd              masters          some high school
     [629] college          masters          masters          college         
     [633] high school      some high school college          college         
     [637] college          phd              college          masters         
     [641] college          some high school some high school phd             
     [645] high school      masters          college          high school     
     [649] high school      college          some high school high school     
     [653] phd              high school      masters          masters         
     [657] high school      high school      some high school masters         
     [661] phd              high school      phd              masters         
     [665] masters          high school      high school      masters         
     [669] masters          college          phd              some high school
     [673] masters          phd              some high school high school     
     [677] college          some high school some high school high school     
     [681] phd              phd              college          phd             
     [685] some high school masters          high school      college         
     [689] masters          college          college          masters         
     [693] some high school some high school college          some high school
     [697] high school      high school      phd              some high school
     [701] masters          phd              high school      some high school
     [705] college          college          college          college         
     [709] some high school college          college          some high school
     [713] college          masters          phd              college         
     [717] phd              high school      college          masters         
     [721] phd              some high school some high school some high school
     [725] masters          college          college          some high school
     [729] college          masters          masters          high school     
     [733] phd              phd              college          phd             
     [737] college          college          masters          some high school
     [741] masters          masters          high school      some high school
     [745] high school      phd              high school      some high school
     [749] masters          high school      some high school phd             
     [753] phd              high school      college          high school     
     [757] college          college          masters          phd             
     [761] masters          phd              high school      high school     
     [765] high school      college          masters          some high school
     [769] high school      phd              some high school masters         
     [773] some high school masters          phd              some high school
     [777] some high school masters          high school      phd             
     [781] phd              some high school college          some high school
     [785] phd              some high school masters          masters         
     [789] masters          college          high school      phd             
     [793] high school      college          some high school high school     
     [797] masters          phd              college          some high school
     [801] high school      phd              college          high school     
     [805] masters          some high school college          some high school
     [809] high school      phd              high school      high school     
     [813] masters          some high school some high school phd             
     [817] masters          college          high school      masters         
     [821] college          some high school high school      high school     
     [825] phd              college          college          college         
     [829] college          masters          masters          high school     
     [833] some high school phd              college          some high school
     [837] some high school high school      high school      college         
     [841] phd              high school      college          phd             
     [845] high school      college          masters          college         
     [849] college          some high school some high school high school     
     [853] high school      high school      high school      masters         
     [857] high school      high school      phd              some high school
     [861] phd              college          some high school college         
     [865] masters          phd              college          phd             
     [869] phd              some high school high school      masters         
     [873] some high school masters          college          high school     
     [877] phd              high school      masters          masters         
     [881] some high school college          some high school college         
     [885] masters          college          college          some high school
     [889] phd              phd              college          phd             
     [893] phd              masters          college          phd             
     [897] masters          some high school high school      college         
     [901] high school      college          some high school high school     
     [905] masters          college          masters          college         
     [909] college          some high school college          some high school
     [913] masters          phd              high school      college         
     [917] some high school phd              high school      masters         
     [921] some high school phd              high school      some high school
     [925] phd              high school      phd              high school     
     [929] some high school some high school high school      phd             
     [933] masters          some high school high school      some high school
     [937] phd              masters          high school      college         
     [941] some high school some high school masters          some high school
     [945] phd              some high school phd              some high school
     [949] college          phd              phd              masters         
     [953] college          high school      high school      masters         
     [957] phd              high school      phd              college         
     [961] masters          masters          phd              college         
     [965] masters          college          college          some high school
     [969] phd              college          some high school some high school
     [973] high school      masters          some high school phd             
     [977] college          high school      phd              high school     
     [981] high school      phd              masters          masters         
     [985] some high school high school      phd              phd             
     [989] college          phd              college          high school     
     [993] some high school some high school college          some high school
     [997] high school      masters          masters          phd             
    Levels: college < high school < masters < phd < some high school
