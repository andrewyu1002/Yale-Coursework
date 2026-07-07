import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import plotnine as p9

def SIR_model(S0, I0, R0, beta, gamma, t_max):
    N = S0 + I0 + R0
    dt = 1
    t = np.arange(0, t_max + dt, dt)
    S = np.zeros(t_max + 1)
    I = np.zeros(t_max + 1)
    R = np.zeros(t_max + 1)
    S[0] = S0
    I[0] = I0
    R[0] = R0

    for i in range(1, t_max + 1):
        dS_dt = -beta * S[i-1] * I[i-1] / N
        dI_dt = beta * S[i-1] * I[i-1] / N - gamma * I[i-1]
        dR_dt = gamma * I[i-1]
        S[i] = S[i-1] + dS_dt * dt
        I[i] = I[i-1] + dI_dt * dt
        R[i] = R[i-1] + dR_dt * dt
        if I[i] < 1:
            return t[:i+1], S[:i+1], I[:i+1], R[:i+1]
    return t, S, I, R

def plot_time_vs_infected(t, I):
    plt.plot(t, I)
    plt.xlabel("Days")
    plt.ylabel("Infected Individuals")
    plt.title("Infected Individuals Over Time")
    plt.show()

def peak_infection(I):
    peak_infected = max(I)
    peak_time = np.argmax(I)
    return peak_infected, peak_time

t1, S1, I1, R1 = SIR_model(S0 = 136999, I0 = 1, R0 = 0, beta = 2, gamma = 1, t_max = 365)
plot_time_vs_infected(t1, I1)
peak_infected_1, peak_time_1 = peak_infection(I1)
print("The number of infected people reached its peak on day " + str(peak_time_1) + ", with the number being " + str(peak_infected_1))

beta_values = np.linspace(1, 3, 20)
gamma_values = np.linspace(0.1, 2, 20)
results = []

for beta in beta_values:
    for gamma in gamma_values:
        t, S, I, R = SIR_model(136999, 1, 0, beta, gamma, 365)
        peak_infected, peak_time = peak_infection(I)
        results.append({
            'beta': beta,
            'gamma': gamma,
            'peak_infected': peak_infected,
            'peak_time': peak_time
        })

infection_data = pd.DataFrame(results)

heatmap_time = p9.ggplot(data = infection_data, mapping = p9.aes(x = 'beta', y = 'gamma', fill = 'peak_time'))
heatmap_time += p9.geom_tile()
heatmap_time += p9.ggtitle("Day of Peak Infection Varied with Beta and Gamma")
heatmap_time += p9.theme(panel_background = p9.element_rect(fill = "white"))
heatmap_time += p9.labs(x = 'Beta', y = 'Gamma', fill = 'Peak Infection Day')
heatmap_time += p9.scale_fill_gradient(low = "yellow", high = "red")
heatmap_time.show()

heatmap_infected = p9.ggplot(data = infection_data, mapping = p9.aes(x = 'beta', y = 'gamma', fill = 'peak_infected'))
heatmap_infected += p9.geom_tile()
heatmap_infected += p9.ggtitle("Peak Number of Infected People Varied with Beta and Gamma")
heatmap_infected += p9.theme(panel_background = p9.element_rect(fill = "white"))
heatmap_infected += p9.labs(x = 'Beta', y = 'Gamma', fill = 'Peak Infected People')
heatmap_infected += p9.scale_fill_gradient(low = "yellow", high = "red")
heatmap_infected.show()