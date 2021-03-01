# Task 3 By Dinesh Karthikeyan
# Student ID: 29592461
# created Date: 20th September 2018
# Completed Date: 12th October 2018
"""
Task 3 : DataVisualisation Class: This class has a pandas data frame as the instance variable, and the input for this
task is the list of objects (SLI , TD) of the DataAnalyser class from Task 2.  The compute_average method is used to
calculate the average of the statistics' lists from the data frame. visualise_statistics method is used to show a bar
graph of the 6 statistics' means for comparing SLI and TD. __str__ function is overloaded to display the Data frame so
as to show the values in a tabular format.
"""
# region Import Section
import task2_29592461 as data_analyser
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


# endregion
# region Data Visualisation Class
class DataVisualisation:
    def __init__(self, data):

        sli_dict = dict()
        td_dict = dict()

        if isinstance(data, list):
            if len(data) == 2:
                if isinstance(data[0], data_analyser.DataAnalyser):
                    sli_dict = {"Length of Transcript": data[0].length_of_transcript,
                                "Size of Vocabulary": data[0].size_of_vocabulary,
                                "Number of Repetition": data[0].number_of_repetition,
                                "Number of Retracing": data[0].number_of_retracing,
                                "Number of Grammatical Errors": data[0].number_of_grammatical_errors,
                                "Number of Pauses": data[
                                    0].number_of_pauses}  # SLI Dictionary with the value from task 2
                if isinstance(data[1], data_analyser.DataAnalyser):
                    td_dict = {"Length of Transcript": data[1].length_of_transcript,
                               "Size of Vocabulary": data[1].size_of_vocabulary,
                               "Number of Repetition": data[1].number_of_repetition,
                               "Number of Retracing": data[1].number_of_retracing,
                               "Number of Grammatical Errors": data[1].number_of_grammatical_errors,
                               "Number of Pauses": data[1].number_of_pauses}  # TD Dictionary with the value from task 2
        self.data_frame = pd.DataFrame([sli_dict, td_dict])  # Data frame with the list of dictionaries
        self.data_frame.index = ["SLI", "TD"]  # Index of the data frame

    def __str__(self):
        return pd.DataFrame.to_string(self.data_frame)

    # region Compute Average Method
    def compute_averages(self):

        for i in self.data_frame.index:  # Accessing values of a row with column title in the data frame
            if len(self.data_frame["Length of Transcript"][i]) != 0:
                self.data_frame["Length of Transcript"][i] = sum(self.data_frame["Length of Transcript"][i]) / len(
                    self.data_frame["Length of Transcript"][i])  # Average of the list using sum and len on the list
                self.data_frame["Size of Vocabulary"][i] = sum(self.data_frame["Size of Vocabulary"][i]) / len(
                    self.data_frame["Size of Vocabulary"][i])
                self.data_frame["Number of Repetition"][i] = sum(self.data_frame["Number of Repetition"][i]) / len(
                    self.data_frame["Number of Repetition"][i])
                self.data_frame["Number of Retracing"][i] = sum(self.data_frame["Number of Retracing"][i]) / len(
                    self.data_frame["Number of Retracing"][i])
                self.data_frame["Number of Grammatical Errors"][i] = sum(
                    self.data_frame["Number of Grammatical Errors"][i]) / len(
                    self.data_frame["Number of Grammatical Errors"][i])
                self.data_frame["Number of Pauses"][i] = sum(self.data_frame["Number of Pauses"][i]) / len(
                    self.data_frame["Number of Pauses"][i])

    # endregion

    # region Visualise Statistics Method
    def visualise_statistics(self):
        if not isinstance(self.data_frame["Length of Transcript"][0], list) != 0:
            no_Statistics = 6
            value_list = sorted(self.data_frame.values.tolist())
            y_index = list(range(5, 39 * 5, 5))
            fig, ax = plt.subplots()  # Creating the Plot
            x_index = np.arange(no_Statistics)
            bar_width = 0.35
            opacity = 0.8

            plot1 = plt.bar(x_index, value_list[0], bar_width,
                            alpha=opacity,
                            color='b',
                            label='SLI')  # Plot for SLI data

            plot2 = plt.bar(x_index + bar_width, value_list[1], bar_width,
                            alpha=opacity,
                            color='g',
                            label='TD')  # Plot for TD data

            plt.xlabel('Statistics')  # Plot's X axis Label
            plt.ylabel('Means of each Statistics')  # Plot's Y axis Label
            plt.title('Comparison of SLI and TD on Mean Statistics')  # Plot's Title
            plt.yticks(y_index)  # Plot's Y axis ticks
            plt.xticks(x_index + bar_width,
                       ('Length of \nTranscript', 'Number of\nGrammatical Errors', 'Number of\nPauses',
                        'Number of\nRepetitions', 'Number of\nRetracing',
                        'Size of\nVocabulary'))  # Plot's X axis ticks
            plt.legend()  # Legend for two groups
            # region For each bar placing Y value as label
            bars = ax.patches
            for bar in bars:
                y_value = bar.get_height()  # Y value for the label
                x_value = bar.get_x() + bar.get_width() / 2  # X value where the Y label to be placed
                space = 10  # Space between bar and label
                va = 'top'  # Vertical alignment of the label
                label = "{:.1f}".format(y_value)  # Y value as label with one digit after decimal point
                plt.annotate(
                    label,
                    (x_value, y_value),
                    xytext=(0, space),  # Placing Labels above the bar
                    textcoords="offset points",  # Placing the Labels on the specific position
                    ha='center',  # Horizontal Alignment of the labels
                    va=va)  # Vertical Alignment of the labels
            # endregion
            fig.set_size_inches(10, 10)  # Size of the output graph in inches
            plt.tight_layout()  # Fitting the Graph to the layout
            plt.savefig("Statistics_output.pdf")  # Saving the graph as pdf
            plt.show()  # Displaying the graph
        else:
            print("\n No Data to be visualised")
        # endregion


# endregion
# region Main
def main():
    data = data_analyser.main()
    sli_analyser = data[0]
    td_analyser = data[1]
    input_data = [sli_analyser, td_analyser]
    data_visualisation = DataVisualisation(input_data)
    print("\n" + "TABLE OF STATISTICS".center(150, " ") + "\n" + "__________________".center(150, " ") + "\n")
    print(data_visualisation)
    data_visualisation.compute_averages()
    print("\n" + "MEAN OF STATISTICS".center(150, " ") + "\n" + "__________________".center(150, " ") + "\n")
    print(str(data_visualisation))
    data_visualisation.visualise_statistics()


# endregion
if __name__ == "__main__":
    main()
