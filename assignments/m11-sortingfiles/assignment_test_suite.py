

# First and foremost, we need to actually move the files. 
    # Only call process_samples() once, in the first test function for process_samples()
try:
    process_samples(get_inbox_samples())
except NameError as e:
    print(jel_NameError("process_samples(get_inbox_samples())", e))



# What the dictionary should be

samples_4hrit76k45h8 = [
    {'filename':'lab06_negative_1451916068.jpg','type':'negative','method':'blood'},
    {'filename':'lab06_negative_1928932078.jpg','type':'negative','method':'blood'},
    {'filename':'lab06_negative_1946492728.jpg','type':'negative','method':'blood'},
    {'filename':'lab06_negative_2058607673.jpg','type':'negative','method':'buccal'},
    {'filename':'lab06_negative_2819489859.jpg','type':'negative','method':'buccal'},
    {'filename':'lab06_negative_3850039168.jpg','type':'negative','method':'blood'},
    {'filename':'lab06_negative_4672894958.jpg','type':'negative','method':'buccal'},
    {'filename':'lab06_negative_5330620049.jpg','type':'negative','method':'blood'},
    {'filename':'lab06_negative_5334163544.jpg','type':'negative','method':'blood'},
    {'filename':'lab06_negative_5408031502.jpg','type':'negative','method':'blood'},
    {'filename':'lab06_negative_5712828358.jpg','type':'negative','method':'blood'},
    {'filename':'lab06_negative_5797258442.jpg','type':'negative','method':'blood'},
    {'filename':'lab06_negative_5842598918.jpg','type':'negative','method':'blood'},
    {'filename':'lab06_negative_6494284429.jpg','type':'negative','method':'buccal'},
    {'filename':'lab06_negative_7015342541.jpg','type':'negative','method':'blood'},
    {'filename':'lab06_negative_7875356088.jpg','type':'negative','method':'blood'},
    {'filename':'lab06_negative_7922906177.jpg','type':'negative','method':'blood'},
    {'filename':'lab06_negative_8109938730.jpg','type':'negative','method':'buccal'},
    {'filename':'lab06_negative_8315662395.jpg','type':'negative','method':'buccal'},
    {'filename':'lab06_negative_8376447339.jpg','type':'negative','method':'buccal'},
    {'filename':'lab06_negative_8989442341.jpg','type':'negative','method':'buccal'},
    {'filename':'lab06_negative_9652371592.jpg','type':'negative','method':'blood'},
    {'filename':'lab06_negative_9803433669.jpg','type':'negative','method':'blood'},
    {'filename':'lab06_positive_1840042215.jpg','type':'positive','method':'blood'},
    {'filename':'lab06_positive_3168519771.jpg','type':'positive','method':'blood'},
    {'filename':'lab06_positive_3821890926.jpg','type':'positive','method':'blood'},
    {'filename':'lab06_positive_3845638867.jpg','type':'positive','method':'blood'},
    {'filename':'lab06_positive_4150941426.jpg','type':'positive','method':'buccal'},
    {'filename':'lab06_positive_4309829134.jpg','type':'positive','method':'buccal'},
    {'filename':'lab06_positive_4423347308.jpg','type':'positive','method':'buccal'},
    {'filename':'lab06_positive_5364475969.jpg','type':'positive','method':'blood'},
    {'filename':'lab06_positive_5706380941.jpg','type':'positive','method':'blood'},
    {'filename':'lab06_positive_5856810068.jpg','type':'positive','method':'blood'},
    {'filename':'lab06_positive_5989370345.jpg','type':'positive','method':'blood'},
    {'filename':'lab06_positive_6300032368.jpg','type':'positive','method':'buccal'},
    {'filename':'lab06_positive_7083327358.jpg','type':'positive','method':'blood'},
    {'filename':'lab06_positive_7167023391.jpg','type':'positive','method':'blood'},
    {'filename':'lab06_positive_7577872066.jpg','type':'positive','method':'blood'},
    {'filename':'lab06_positive_7971159980.jpg','type':'positive','method':'blood'},
    {'filename':'lab06_positive_8105371368.jpg','type':'positive','method':'buccal'},
    {'filename':'lab06_positive_8122083869.jpg','type':'positive','method':'buccal'},
    {'filename':'lab06_positive_8649087671.jpg','type':'positive','method':'buccal'},
    {'filename':'lab06_positive_9075477266.jpg','type':'positive','method':'blood'},
    {'filename':'lab06_positive_9090024040.jpg','type':'positive','method':'blood'},
    {'filename':'lab06_positive_9148027742.jpg','type':'positive','method':'blood'},
    {'filename':'lab06_positive_9171535697.jpg','type':'positive','method':'blood'},
    {'filename':'lab06_positive_9414842922.jpg','type':'positive','method':'blood'},
    {'filename':'lab06_positive_9858941703.jpg','type':'positive','method':'blood'},
    {'filename':'lab19_negative_1435909950.jpg','type':'negative','method':'blood'},
    {'filename':'lab19_negative_1763750956.jpg','type':'negative','method':'blood'},
    {'filename':'lab19_negative_2736829252.jpg','type':'negative','method':'buccal'},
    {'filename':'lab19_negative_2899746612.jpg','type':'negative','method':'buccal'},
    {'filename':'lab19_negative_2931358206.jpg','type':'negative','method':'buccal'},
    {'filename':'lab19_negative_3134828519.jpg','type':'negative','method':'blood'},
    {'filename':'lab19_negative_4221758489.jpg','type':'negative','method':'buccal'},
    {'filename':'lab19_negative_4573664790.jpg','type':'negative','method':'buccal'},
    {'filename':'lab19_negative_4742422988.jpg','type':'negative','method':'buccal'},
    {'filename':'lab19_negative_4772970393.jpg','type':'negative','method':'buccal'},
    {'filename':'lab19_negative_5529515030.jpg','type':'negative','method':'blood'},
    {'filename':'lab19_negative_5814300148.jpg','type':'negative','method':'blood'},
    {'filename':'lab19_negative_6273254319.jpg','type':'negative','method':'buccal'},
    {'filename':'lab19_negative_6286844691.jpg','type':'negative','method':'buccal'},
    {'filename':'lab19_negative_6522576617.jpg','type':'negative','method':'buccal'},
    {'filename':'lab19_negative_7569476542.jpg','type':'negative','method':'blood'},
    {'filename':'lab19_negative_7793852467.jpg','type':'negative','method':'blood'},
    {'filename':'lab19_negative_8115882609.jpg','type':'negative','method':'buccal'},
    {'filename':'lab19_negative_8269047223.jpg','type':'negative','method':'buccal'},
    {'filename':'lab19_negative_8794663153.jpg','type':'negative','method':'buccal'},
    {'filename':'lab19_negative_9143021793.jpg','type':'negative','method':'blood'},
    {'filename':'lab19_negative_9210790373.jpg','type':'negative','method':'blood'},
    {'filename':'lab19_negative_9869091968.jpg','type':'negative','method':'blood'},
    {'filename':'lab19_negative_9904274749.jpg','type':'negative','method':'blood'},
    {'filename':'lab19_positive_1652103953.jpg','type':'positive','method':'blood'},
    {'filename':'lab19_positive_1903286953.jpg','type':'positive','method':'blood'},
    {'filename':'lab19_positive_2683727205.jpg','type':'positive','method':'buccal'},
    {'filename':'lab19_positive_3077179522.jpg','type':'positive','method':'blood'},
    {'filename':'lab19_positive_3233536846.jpg','type':'positive','method':'blood'},
    {'filename':'lab19_positive_3988333505.jpg','type':'positive','method':'blood'},
    {'filename':'lab19_positive_4177994037.jpg','type':'positive','method':'buccal'},
    {'filename':'lab19_positive_4364819403.jpg','type':'positive','method':'buccal'},
    {'filename':'lab19_positive_4808437265.jpg','type':'positive','method':'buccal'},
    {'filename':'lab19_positive_5062504617.jpg','type':'positive','method':'blood'},
    {'filename':'lab19_positive_5808304651.jpg','type':'positive','method':'blood'},
    {'filename':'lab19_positive_6060392435.jpg','type':'positive','method':'buccal'},
    {'filename':'lab19_positive_6203778255.jpg','type':'positive','method':'buccal'},
    {'filename':'lab19_positive_6233702414.jpg','type':'positive','method':'buccal'},
    {'filename':'lab19_positive_6272234615.jpg','type':'positive','method':'buccal'},
    {'filename':'lab19_positive_6567122130.jpg','type':'positive','method':'buccal'},
    {'filename':'lab19_positive_8004474313.jpg','type':'positive','method':'buccal'},
    {'filename':'lab19_positive_8153972097.jpg','type':'positive','method':'buccal'},
    {'filename':'lab19_positive_8374325199.jpg','type':'positive','method':'buccal'},
    {'filename':'lab19_positive_8623873118.jpg','type':'positive','method':'buccal'},
    {'filename':'lab19_positive_8824924937.jpg','type':'positive','method':'buccal'},
    {'filename':'lab19_positive_9015333468.jpg','type':'positive','method':'blood'},
    {'filename':'lab19_positive_9194217786.jpg','type':'positive','method':'blood'},
    {'filename':'lab19_positive_9616746276.jpg','type':'positive','method':'blood'},
    {'filename':'lab33_negative_1377262389.jpg','type':'negative','method':'blood'},
    {'filename':'lab33_negative_1391755661.jpg','type':'negative','method':'blood'},
    {'filename':'lab33_negative_1593196264.jpg','type':'negative','method':'blood'},
    {'filename':'lab33_negative_1692464468.jpg','type':'negative','method':'blood'},
    {'filename':'lab33_negative_1782444661.jpg','type':'negative','method':'blood'},
    {'filename':'lab33_negative_2012581444.jpg','type':'negative','method':'buccal'},
    {'filename':'lab33_negative_2543327763.jpg','type':'negative','method':'buccal'},
    {'filename':'lab33_negative_2876435651.jpg','type':'negative','method':'buccal'},
    {'filename':'lab33_negative_2950486892.jpg','type':'negative','method':'buccal'},
    {'filename':'lab33_negative_3740041960.jpg','type':'negative','method':'blood'},
    {'filename':'lab33_negative_3969174537.jpg','type':'negative','method':'blood'},
    {'filename':'lab33_negative_4161714256.jpg','type':'negative','method':'buccal'},
    {'filename':'lab33_negative_4493710060.jpg','type':'negative','method':'buccal'},
    {'filename':'lab33_negative_4727590205.jpg','type':'negative','method':'buccal'},
    {'filename':'lab33_negative_5020827950.jpg','type':'negative','method':'blood'},
    {'filename':'lab33_negative_5357470978.jpg','type':'negative','method':'blood'},
    {'filename':'lab33_negative_5641711516.jpg','type':'negative','method':'blood'},
    {'filename':'lab33_negative_6200913542.jpg','type':'negative','method':'buccal'},
    {'filename':'lab33_negative_6286404699.jpg','type':'negative','method':'buccal'},
    {'filename':'lab33_negative_6402897413.jpg','type':'negative','method':'buccal'},
    {'filename':'lab33_negative_6531086505.jpg','type':'negative','method':'buccal'},
    {'filename':'lab33_negative_6586206972.jpg','type':'negative','method':'buccal'},
    {'filename':'lab33_negative_8469892544.jpg','type':'negative','method':'buccal'},
    {'filename':'lab33_negative_8478634240.jpg','type':'negative','method':'buccal'},
    {'filename':'lab33_negative_8761395738.jpg','type':'negative','method':'buccal'},
    {'filename':'lab33_negative_9464151482.jpg','type':'negative','method':'blood'},
    {'filename':'lab33_negative_9572053352.jpg','type':'negative','method':'blood'},
    {'filename':'lab33_negative_9732256399.jpg','type':'negative','method':'blood'},
    {'filename':'lab33_positive_1992782259.jpg','type':'positive','method':'blood'},
    {'filename':'lab33_positive_2238218141.jpg','type':'positive','method':'buccal'},
    {'filename':'lab33_positive_2257812764.jpg','type':'positive','method':'buccal'},
    {'filename':'lab33_positive_2654325255.jpg','type':'positive','method':'buccal'},
    {'filename':'lab33_positive_3621963862.jpg','type':'positive','method':'blood'},
    {'filename':'lab33_positive_3712427131.jpg','type':'positive','method':'blood'},
    {'filename':'lab33_positive_3996247001.jpg','type':'positive','method':'blood'},
    {'filename':'lab33_positive_4016259631.jpg','type':'positive','method':'buccal'},
    {'filename':'lab33_positive_5825270642.jpg','type':'positive','method':'blood'},
    {'filename':'lab33_positive_6012562232.jpg','type':'positive','method':'buccal'},
    {'filename':'lab33_positive_6918947663.jpg','type':'positive','method':'buccal'},
    {'filename':'lab33_positive_7120225203.jpg','type':'positive','method':'blood'},
    {'filename':'lab33_positive_7134677818.jpg','type':'positive','method':'blood'},
    {'filename':'lab33_positive_8371040179.jpg','type':'positive','method':'buccal'},
    {'filename':'lab33_positive_8955810602.jpg','type':'positive','method':'buccal'},
    {'filename':'lab33_positive_8958134544.jpg','type':'positive','method':'buccal'},
    {'filename':'lab33_positive_9153041229.jpg','type':'positive','method':'blood'},
    {'filename':'lab33_positive_9467650784.jpg','type':'positive','method':'blood'},
    {'filename':'lab33_positive_9520721045.jpg','type':'positive','method':'blood'},
    {'filename':'lab33_positive_9562075396.jpg','type':'positive','method':'blood'},
    {'filename':'lab34_negative_1432787153.jpg','type':'negative','method':'blood'},
    {'filename':'lab34_negative_1477257663.jpg','type':'negative','method':'blood'},
    {'filename':'lab34_negative_2003493804.jpg','type':'negative','method':'buccal'},
    {'filename':'lab34_negative_2328733093.jpg','type':'negative','method':'buccal'},
    {'filename':'lab34_negative_3130836804.jpg','type':'negative','method':'blood'},
    {'filename':'lab34_negative_4203241047.jpg','type':'negative','method':'buccal'},
    {'filename':'lab34_negative_4224336757.jpg','type':'negative','method':'buccal'},
    {'filename':'lab34_negative_5064576281.jpg','type':'negative','method':'blood'},
    {'filename':'lab34_negative_5144125132.jpg','type':'negative','method':'blood'},
    {'filename':'lab34_negative_5248598617.jpg','type':'negative','method':'blood'},
    {'filename':'lab34_negative_5354610310.jpg','type':'negative','method':'blood'},
    {'filename':'lab34_negative_5495137556.jpg','type':'negative','method':'blood'},
    {'filename':'lab34_negative_5900581964.jpg','type':'negative','method':'blood'},
    {'filename':'lab34_negative_6193879018.jpg','type':'negative','method':'buccal'},
    {'filename':'lab34_negative_6475977044.jpg','type':'negative','method':'buccal'},
    {'filename':'lab34_negative_7013860220.jpg','type':'negative','method':'blood'},
    {'filename':'lab34_negative_7311649751.jpg','type':'negative','method':'blood'},
    {'filename':'lab34_negative_7555867422.jpg','type':'negative','method':'blood'},
    {'filename':'lab34_negative_8179913503.jpg','type':'negative','method':'buccal'},
    {'filename':'lab34_negative_8735121715.jpg','type':'negative','method':'buccal'},
    {'filename':'lab34_negative_8956912934.jpg','type':'negative','method':'buccal'},
    {'filename':'lab34_negative_9099011125.jpg','type':'negative','method':'blood'},
    {'filename':'lab34_negative_9425368870.jpg','type':'negative','method':'blood'},
    {'filename':'lab34_negative_9900954182.jpg','type':'negative','method':'blood'},
    {'filename':'lab34_negative_9922171871.jpg','type':'negative','method':'blood'},
    {'filename':'lab34_positive_1742890137.jpg','type':'positive','method':'blood'},
    {'filename':'lab34_positive_1757143991.jpg','type':'positive','method':'blood'},
    {'filename':'lab34_positive_1955803621.jpg','type':'positive','method':'blood'},
    {'filename':'lab34_positive_2608899419.jpg','type':'positive','method':'buccal'},
    {'filename':'lab34_positive_2679026425.jpg','type':'positive','method':'buccal'},
    {'filename':'lab34_positive_2830108951.jpg','type':'positive','method':'buccal'},
    {'filename':'lab34_positive_2928409145.jpg','type':'positive','method':'buccal'},
    {'filename':'lab34_positive_4762931410.jpg','type':'positive','method':'buccal'},
    {'filename':'lab34_positive_4926209892.jpg','type':'positive','method':'buccal'},
    {'filename':'lab34_positive_5101796415.jpg','type':'positive','method':'blood'},
    {'filename':'lab34_positive_5353549054.jpg','type':'positive','method':'blood'},
    {'filename':'lab34_positive_5773046188.jpg','type':'positive','method':'blood'},
    {'filename':'lab34_positive_5996522969.jpg','type':'positive','method':'blood'},
    {'filename':'lab34_positive_6712433890.jpg','type':'positive','method':'buccal'},
    {'filename':'lab34_positive_6936599924.jpg','type':'positive','method':'buccal'},
    {'filename':'lab34_positive_7010749597.jpg','type':'positive','method':'blood'},
    {'filename':'lab34_positive_7285606198.jpg','type':'positive','method':'blood'},
    {'filename':'lab34_positive_7650573358.jpg','type':'positive','method':'blood'},
    {'filename':'lab34_positive_7803988494.jpg','type':'positive','method':'blood'},
    {'filename':'lab34_positive_8110728280.jpg','type':'positive','method':'buccal'},
    {'filename':'lab34_positive_9213413018.jpg','type':'positive','method':'blood'},
    {'filename':'lab34_positive_9442271255.jpg','type':'positive','method':'blood'},
    {'filename':'lab34_positive_9982717354.jpg','type':'positive','method':'blood'}
]


# Problem 1
problem1_target = "get_inbox_samples()"

def test_get_inbox_samples():

    # Credit for the zip() and any() solution below: 
    # https://stackoverflow.com/a/9845430/2516576
    pairs = zip(get_inbox_samples(), samples_4hrit76k45h8)
    result = False if any(x != y for x, y in pairs) else True

    try:
        return jel_assert(
                problem1_target, 
                result,
                f"return a list with each element being a dictionary representing each file from the inbox"
            )
    except NameError as e:
        return jel_NameError(problem1_target, e)
    except TypeError as e:
        return jel_TypeError(problem1_target, e)

problem2_target = "process_samples()"

def test_process_samples_0():
    
    result = True

    # Get list of all files in /negative
    for r in os.scandir(os.curdir+"/negative"):
        if r.name[6:7] == 'p':
            result = False # So even one incorrectly moved file breaks the test

    try:
        return jel_assert(
                problem2_target, 
                result,
                f"move only 'negative' samples from /inbox to the /negative folder"
            )
    except NameError as e:
        return jel_NameError(problem2_target, e)
    except TypeError as e:
        return jel_TypeError(problem2_target, e)

def test_process_samples_1():
    # Make sure there are 100 negative samples

    num_files = 0
    
    for r in os.scandir(os.curdir+"/negative"):
        if r.is_file():
            num_files+=1

    try:
        return jel_assert(
                problem2_target, 
                num_files == 100,
                f"move a total of 100 samples from /inbox to the /negative folder"
            )
    except NameError as e:
        return jel_NameError(problem2_target, e)
    except TypeError as e:
        return jel_TypeError(problem2_target, e)


def test_process_samples_2():
    
    result = True

    # Get list of all files in /positive/blood
    for r in os.scandir(os.curdir+"/positive/blood"):
        if r.name[15:16] in ['2', '4', '6', '8', '0']:
            result = False # So even one incorrectly moved file breaks the test

    # Get list of all files in /positive/buccal

    # Get list of all files in /inbox (should be zero)

    try:
        return jel_assert(
                problem2_target, 
                result,
                f"move only 'positive' blood samples from /inbox to the /positive/blood folder"
            )
    except NameError as e:
        return jel_NameError(problem2_target, e)
    except TypeError as e:
        return jel_TypeError(problem2_target, e)

def test_process_samples_3():
    

    num_files = 0
    
    for r in os.scandir(os.curdir+"/positive/buccal"):
        if r.is_file():
            num_files+=1

    try:
        return jel_assert(
                problem2_target, 
                num_files == 39,
                f"move a total of 39 buccal samples from /inbox to the /positive/buccal folder"
            )
    except NameError as e:
        return jel_NameError(problem2_target, e)
    except TypeError as e:
        return jel_TypeError(problem2_target, e)

def test_process_samples_4():
    

    num_files = 0
    
    for r in os.scandir(os.curdir+"/positive/blood"):
        if r.is_file():
            num_files+=1

    try:
        return jel_assert(
                problem2_target, 
                num_files == 53,
                f"move a total of 53 samples from /inbox to the /positive/blood folder"
            )
    except NameError as e:
        return jel_NameError(problem2_target, e)
    except TypeError as e:
        return jel_TypeError(problem2_target, e)

