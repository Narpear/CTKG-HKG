from download_html import download_html
from get_div import get_pi_names
from delete_html import delete_file

import pandas as pd

# Load the trials data
trials = pd.read_csv('All_Trials_Data.csv')
n = len(trials)
trials['Principal_Investigators'] = ''
# Process each trial
for i in range(n):  # Changed range to iterate through all rows
    print("Trial: ", i)
    trial = trials.iloc[i]
    nct = trial['NCT Number']
    
    # Download the HTML content for the trial
    download_html(nct)
    print("Downloaded file successfully.")
    
    # Extract the principal investigator names
    pis = get_pi_names(nct)
    print("PI extracted successfully: ", pis)
    
    # Assign the extracted names to the DataFrame using .loc
    if pis is not None:
        trials.loc[i, 'Principal_Investigators'] = pis  # Modified this line
        print("PI name appended")
    
    # Delete the downloaded HTML file
    delete_file(nct)
    print("Deleted file successfully")

print("Task completed successfully")

# Save the updated DataFrame to a new CSV file
trials.to_csv('All_Trials_Data_With_PIs.csv', index=False)
print("Data saved successfully to All_Trials_Data_With_PIs.csv")