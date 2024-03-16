# plot.py

import matplotlib.pyplot as plt

# Create plot
def plot(output_name, x_values, y_values, title, x_label, y_label, scatter=True):
    # create plot
    print(f" - Creating plot: {output_name}")
    if scatter:
        plt.scatter(x_values, y_values)
    else:
        plt.plot(x_values, y_values)
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    
    # save plot
    #plt.show()
    output_png = f"{output_name}.png"
    output_pdf = f"{output_name}.pdf"
    plt.savefig(output_png, bbox_inches='tight')
    plt.savefig(output_pdf, bbox_inches='tight')
    plt.close('all')

