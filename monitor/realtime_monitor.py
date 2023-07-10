import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.animation as animation
from database.TransactionsDatabase import TransactionsDatabase


def create_real_time_line_graph():
    transactions_database = TransactionsDatabase()
    # ATENTION IN Frequency
    freq = 10  # Frequency for data grouping

    # Function to update the graph in real-time
    def update_graph(frame):
        # Get the data from the database
        results = transactions_database.get_all_transactions()

        # Create a DataFrame with the results
        df = pd.DataFrame(results, columns=['id', 'time', 'status', 'count'])
        df['time'] = pd.to_datetime(df['time'], format='%Y-%m-%d %H:%M:%S')

        # Group the data by selected intervals and status, and calculate the sum of counts
        df_grouped = df.groupby([pd.Grouper(key='time', freq=str(freq) + 'Min'), 'status']).sum().reset_index()

        # Limit the data to the last 7 days
        df_grouped = df_grouped.iloc[-24 * 60 * 7:]

        # Clear the previous graph
        plt.cla()

        # Iterate over the unique statuses and create the corresponding lines
        for status in df_grouped['status'].unique():
            status_data = df_grouped[df_grouped['status'] == status]
            plt.plot(status_data['time'], status_data['count'], color=colors[status], marker='o', label=status)

        # Set the axis labels and graph title
        plt.xlabel('Time')
        plt.ylabel('Count')
        plt.title('Real-Time Line Graph')

        # Format the x-axis to display only HH:MM
        ax.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))

        # Adjust the intervals of x-axis ticks
        ax.xaxis.set_major_locator(mdates.MinuteLocator(interval=10))

        # Rotate the x-axis tick labels
        plt.xticks(rotation=45)

        # Get the tick labels and locations of x-axis ticks
        x_ticks = ax.get_xticks()
        x_tick_labels = ax.get_xticklabels()

        # Set the spacing between x-axis ticks
        new_x_ticks = [x_ticks[i] for i in range(len(x_ticks)) if i % 2 == 0]
        new_x_tick_labels = [x_tick_labels[i] for i in range(len(x_tick_labels)) if i % 2 == 0]

        # Set the new x-axis ticks and labels
        plt.xticks(new_x_ticks, new_x_tick_labels)

        # Add a legend
        plt.legend()

    # Create a figure and axis for the graph
    fig, ax = plt.subplots(figsize=(12, 6))

    # Define the colors for each status
    colors = {'approved': 'green',
              'refunded': 'green',
              'denied': 'red',
              'failed': 'darkred',
              'processing': 'yellow',
              'reversed': 'blue',
              'backend_reversed': 'blue'}

    # Update the graph immediately
    update_graph(0)

    # Configure the periodic update of the graph
    ani = animation.FuncAnimation(fig, update_graph, interval=60000)  # Update every 1 minute (60000 ms)

    # Display the graph
    plt.show()


# Call the function to create the real-time graph
create_real_time_line_graph()
