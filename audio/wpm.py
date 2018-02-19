import pickle

pk = 'stt_object.pkl'
pk = 'nonsense_object.pkl'
with open(pk, 'rb') as input:
    stt = pickle.load(input)

timestamps = []
simple = []
for phrase in stt['results']:
    for word in phrase['alternatives'][0]['timestamps']:
        simple.append([word[0], word[2]])

# wc / time

# interval of 5s
interval = 2
time_inc = 2
time_acc = time_inc #redundant^^
# total_time = 0
word_count = 0
last_time = 0
wpm = []
def calc_cum_wpm():
    wpm = []
    for word in simple:
        if(word[1]>=time_acc):
            if(last_time!=0):
                wpm.append([last_time, word_count/(last_time/60)])
            time_acc += time_inc
        word_count+=1
        last_time = word[1]
    wpm.append([last_time, word_count/(last_time/60)])
    return wpm

def calc_interval_wpm():
    global interval
    time_inc = interval
    time_acc = interval
    global word_count
    for word in simple:
        if(word[1]>=time_acc):
            wpm.append([time_acc, word_count/(interval/60)])
            time_acc+=time_inc
            word_count = 0
        word_count+=1
    if(word_count!=0):
        final_time = simple[-1][1]
        final_interval = final_time - (time_acc - time_inc)
        wpm.append([final_time, word_count/(final_interval/60)])


lpm = []
def calc_interval_lpm():
    global interval
    time_inc = interval
    time_acc = interval
    letter_count = 0
    for word in simple:
        if(word[1]>=time_acc):
            lpm.append([time_acc, letter_count/(interval/60)])
            time_acc+=time_inc
            letter_count = 0
        letter_count+=len(word[0])

    if(letter_count!=0):
        final_time = simple[-1][1]
        final_interval = final_time - (time_acc - time_inc)
        lpm.append([final_time, letter_count/(final_interval/60)])

calc_interval_lpm()
calc_interval_wpm()

lp = []
time = []
wp = []
for ll in lpm:
    lp.append(ll[1])

for wl in wpm:
    time.append(wl[0])
    wp.append(wl[1])
