import requests        

def api_call():
    headers = {'User-Agent': 'abc'}
    response = requests.get('https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode=400064&date=30-06-2021', headers=headers)
    response.raise_for_status()
    return response.json()
reply = api_call()
centers = reply.get('centers')
#print (centers)
for center in centers:
    center_id = center.get('center_id')
    center_name = center.get('name')
    sessions = center.get('sessions')
    #available_slot = sessions.get('available_capacity_dose1')
    #print ('Slot availability in %s is %d' % (center, available_slot))
    for session in sessions:
        available_slot1 = session.get('available_capacity_dose1')
        available_slot2 = session.get('available_capacity_dose2')
        slots = session.get('slots')
        print ('Dose 1 availability in %s for slot %s is %d' % (center_name, slots, available_slot1))
        print ('Dose 2 availability in %s for slot %s is %d' % (center_name, slots, available_slot2))