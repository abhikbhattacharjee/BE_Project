import pandas as pd

peak_calling=pd.read_excel("Peakcalling_1e-4__PePr_peaks_homer.xlsx",'notdiff1-1.1')
peak_calling['Length'] = peak_calling['End'] - peak_calling['Start'] 

peak_calling1=pd.read_excel("Peakcalling_1e-4__PePr_peaks_homer.xlsx",'down1.5')
peak_calling1['Length'] = peak_calling1['End'] - peak_calling1['Start'] 

peak_calling2=pd.read_excel("Peakcalling_1e-4__PePr_peaks_homer.xlsx",'up1.5')
peak_calling2['Length'] = peak_calling2['End'] - peak_calling2['Start'] 

with pd.ExcelWriter('Excel/Peak_calling_length.xlsx') as writer:
    peak_calling.to_excel(writer, sheet_name='not_diff')
    peak_calling1.to_excel(writer, sheet_name='down_toptags')
    peak_calling2.to_excel(writer, sheet_name='up_toptags')

