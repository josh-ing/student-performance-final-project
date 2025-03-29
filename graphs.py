import pandas as pd
import matplotlib.pyplot as plt
# --- Settings ---
ylim_range = (-0.5, 0.5)

# --- Function to plot each metric ---
def plot_fairness_metric(metric_name, value, protected_class):
    threshold_range = (-1.0, 1.0)
    if metric_name == 'Statistical Parity':
        threshold_range = (-0.1, 1.0)
        ylim_range = (-0.5, 0.5)
    else: 
        threshold_range = (0.99, 1.01)
        ylim_range = (0,1.25)
    ## stat parity = -0.1 to 0.1
    ## disparate impact = .99 to 1.01
    plt.figure(figsize=(6, 4))
    bar_color = 'skyblue' if metric_name == 'Statistical Parity' else 'lightgreen'
    lower_threshold, upper_threshold = threshold_range

    # Plot the single bar
    plt.bar(metric_name, value, color=bar_color)

    # Horizontal lines for fairness threshold
    plt.axhline(0, color='black', linewidth=1)
    plt.axhline(upper_threshold, color='red', linestyle='--', label=f'Bias Threshold ({lower_threshold}, {upper_threshold})')
    plt.axhline(lower_threshold, color='red', linestyle='--')

    # Titles and formatting
    plt.title(f'{metric_name} by {protected_class}', fontsize=14)
    plt.ylabel('Metric Value (Difference)', fontsize=12)
    plt.ylim(ylim_range)
    plt.legend()
    plt.tight_layout()

    # Save each figure
    filename = f"{metric_name.lower().replace(' ', '_')}_{protected_class}.png"
    plt.savefig(filename, dpi=300)

# --- Plot each metric ---
# Sex
plot_fairness_metric('Statistical Parity', 0.062, 'Sex')
plot_fairness_metric('Disparate Impact', 1.074, 'Sex')

# Age
plot_fairness_metric('Statistical Parity', -0.081, 'Age')
plot_fairness_metric('Disparate Impact', 0.909, 'Age')
