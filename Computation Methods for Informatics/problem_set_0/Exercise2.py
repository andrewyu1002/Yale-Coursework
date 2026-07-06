import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv("problem_set_0/us-states.csv")

# list of states
states = ['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'Florida', 
          'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 
          'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 
          'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 
          'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 
          'Washington', 'West Virginia', 'Wisconsin', 'Wyoming']

num_states = len(states)
colormap = plt.cm.get_cmap('tab20c', num_states)
state_colors = {state: colormap(i / num_states) for i, state in enumerate(states)}

def case_visualization(states):
    plt.figure(figsize=(14, 7))
    for state in states:
        state_data = data[data['state'] == state].copy()
        state_data['date'] = pd.to_datetime(state_data['date'])
        state_data['new_cases'] = state_data['cases'].diff().fillna(0).astype(int)
        plt.plot(state_data['date'], state_data['new_cases'], label=state, color = state_colors[state])
    plt.xlabel('Date')
    plt.ylabel('Number of New Covid Cases')
    plt.title('New Covid Cases in Each U.S. State')
    plt.legend(loc='upper left', bbox_to_anchor=(1, 1), fontsize='small', ncol = 2, frameon=True)
    plt.tight_layout()
    plt.show()

def peak_case_date(state):
    state_data = data[data['state'] == state].copy()
    state_data['new_cases'] = state_data['cases'].diff().fillna(0).astype(int)
    peak_date = state_data.loc[state_data['new_cases'].idxmax(), 'date']
    return peak_date

def comp_peaks(state1, state2):
    state1_peak = pd.to_datetime(peak_case_date(state1))
    state2_peak = pd.to_datetime(peak_case_date(state2))
    if(state1_peak < state2_peak):
        peak_diff = (state2_peak - state1_peak).days
        print(state1, "had its peak", peak_diff, "days before", state2)
    elif(state2_peak < state1_peak):
        peak_diff = (state1_peak - state2_peak).days
        print(state2, "had its peak", peak_diff, "days before", state1)
    else:
        print("Both states had their peak on the same day")

case_visualization(states)
print("Illinois had its peak number of new cases on", peak_case_date("Illinois"))
comp_peaks("California", "Illinois")