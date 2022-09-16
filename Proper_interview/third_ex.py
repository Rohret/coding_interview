

def change_time(orignal_seconds):
    hours = 0
    min = 0
    seconds = 0
    hours = int(orignal_seconds/3600)
    min = int((orignal_seconds-(hours*3600))/60)
    seconds = int((orignal_seconds-(hours*3600)-(min*60)))
    print(orignal_seconds,"sekunder är lika med " , hours , " h " , min , " min och " , seconds ," sekunder.")
    print(f'{orignal_seconds} sekunder är lika med {hours} h {min}  min och {seconds} sekunder')
change_time(4990)
