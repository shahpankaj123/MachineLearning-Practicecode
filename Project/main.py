import requests
import json
import pandas as pd

res = requests.get("https://data.cityofnewyork.us/resource/52dp-yji6.json")

if res.status_code == 200:
   data =json.loads(res.content)
   tracking_number=[]
   boiler_id=[]
   report_type=[]
   pressure_type=[]
   inspection_date=[]
   defects_exist=[]
   lff_45_days=[]
   lff_180_days=[]
   filing_fee=[]
   total_amount_paid=[]
   report_status=[]
   bin_number=[]

   for d in data:
        print(d)
        tracking_number.append(d.get('tracking_number') if d.get('tracking_number') is not None else None)
        boiler_id.append(d.get('boiler_id') if d.get('boiler_id') is not None else None)
        report_type.append(d.get('report_type') if d.get('report_type') is not None else None)
        pressure_type.append(d.get('pressure_type') if d.get('pressure_type') is not None else None)
        inspection_date.append(d.get('inspection_date') if d.get('inspection_date') is not None else None)
        defects_exist.append(d.get('defects_exist') if d.get('defects_exist') is not None else None)
        lff_45_days.append(d.get('lff_45_days') if d.get('lff_45_days') is not None else None)
        lff_180_days.append(d.get('lff_180_days') if d.get('lff_180_days') is not None else None)
        filing_fee.append(d.get('filing_fee') if d.get('filing_fee') is not None else None)
        total_amount_paid.append(d.get('total_amount_paid') if d.get('total_amount_paid') is not None else None)
        report_status.append(d.get('report_status') if d.get('report_status') is not None else None)
        bin_number.append(d.get('bin_number') if d.get('bin_number') is not None else None)

# Create a DataFrame from the lists
data_dict = {
    'tracking_number': tracking_number,
    'boiler_id': boiler_id,
    'report_type': report_type,
    'pressure_type': pressure_type,
    'inspection_date': inspection_date,
    'defects_exist': defects_exist,
    'lff_45_days': lff_45_days,
    'lff_180_days': lff_180_days,
    'filing_fee': filing_fee,
    'total_amount_paid': total_amount_paid,
    'report_status': report_status,
    'bin_number': bin_number
}

# Create the DataFrame
df = pd.DataFrame(data_dict)
df.to_csv('data.csv')

    