# Task 2 By Dinesh Karthikeyan
# Student ID: 29592461
# created Date: 20th September 2018
# Completed Date: 12th October 2018
"""
Task 2: DataAnalyser Class  : This class has six lists as instance variables each representing one statistics ,
that is to be calculated from the Child statements in the output file created from Task1.
analyse_script method is used to Analyse the files (one file at a time) and collect values for :- Length of Transcript, Number of Repetition,
Number of Retracing, Number of Grammatical Errors, Number of Pauses and Size of the child's Vocabulary.
these statistics for each child are stored in their respective lists and are displayed by overloaded __str__ method.

Since Task 2 is dependent on Task 1 , Task 1 is run first by importing the Task 1 and calling its main function.
"""
# region Import Section
import os
import re
import task1_29592461 as file_parser


# endregion
# region DataAnalyser Class
class DataAnalyser:
    def __init__(self):
        self.length_of_transcript = []  # List for Saving Length of Statements
        self.size_of_vocabulary = []  # List for Saving Vocabulary size of each child
        self.number_of_repetition = []  # List for Saving Number of Repetition
        self.number_of_retracing = []  # List for Saving Number of Retracing
        self.number_of_grammatical_errors = []  # List for Saving Number of Grammatical Errors
        self.number_of_pauses = []  # List for Saving Number of Pauses

    def __str__(self):
        return " Length of Transcript : {0} \n " \
               " Size of Vocabulary : {1} \n " \
               " Number of Repetition : {2} \n " \
               " Number of Retracing : {3} \n " \
               " Number of Grammatical Errors : {4} \n " \
               " Number of Pauses : {5}\n ".format(sum(self.length_of_transcript),
                                                   sum(self.size_of_vocabulary),
                                                   sum(self.number_of_repetition),
                                                   sum(self.number_of_retracing),
                                                   sum(self.number_of_grammatical_errors),
                                                   sum(self.number_of_pauses))

    def analyse_script(self, cleaned_file):
        file = open(cleaned_file)
        file_content = file.readlines()
        unique_words = set()  # Using Set to find the Vocabulary of a Child from the transcript
        length_of_statements = 0
        number_of_repetition = 0
        number_of_retracing = 0
        number_of_grammatical_errors = 0
        number_of_pauses = 0
        for line in file_content:
            if line.strip().endswith(".") or line.strip().endswith("!") \
                    or line.strip().endswith("?"):  # Counting the Number of Statements in a transcript
                length_of_statements += 1
            if line.count("[/]") > 0:  # Counting Number of Repetition in a transcript
                number_of_repetition += line.count("[/]")
            if line.count("[//]") > 0:  # Counting Number of Retracing in a transcript
                number_of_retracing += line.count("[//]")
            if line.count("[*") > 0:  # Counting Number of Grammatical Errors
                number_of_grammatical_errors += line.count("[*")
            if line.count("(.)") > 0:  # Counting Number of Pauses in a Transcript
                number_of_pauses += line.count("(.)")
            line_content = re.split(" ", line)
            for word in line_content:
                if not word.strip() == '' and word.strip() != "(.)" and \
                        word.strip() != "[/]" and word.strip() != "[//]" and \
                        word.count("[*") == 0 and word.strip() != "." and \
                        word.strip() != "," and word.strip() != "!" and \
                        word.strip() != "?" and word.strip() != ".." and \
                        word.strip() != "...":  # Neglecting empty string, Punctuations and other CHAT Symbols to find the vocabulary
                    unique_words.add(word.strip())

        self.length_of_transcript.append(length_of_statements)
        self.number_of_repetition.append(number_of_repetition)
        self.number_of_retracing.append(number_of_retracing)
        self.number_of_grammatical_errors.append(number_of_grammatical_errors)
        self.number_of_pauses.append(number_of_pauses)
        self.size_of_vocabulary.append(len(unique_words))


# endregion
# region Main
def main():
    file_parser.main()  # Running Task1
    sli_analyser = DataAnalyser()  # Object for SLI Group
    td_analyser = DataAnalyser()  # Object for TD Group
    output_path_sli = "SLI_Cleaned"  # SLI Output Folder
    output_path_td = "TD_Cleaned"  # TD Output Folder
    if os.path.exists(output_path_sli):
        file_list_sli = os.listdir(output_path_sli)  # Reading Files into list From SLI Output Folder
        for file in file_list_sli:
            sli_analyser.analyse_script(output_path_sli + "/" + file)  # Analysing each Files in SLI Output Folder
    if os.path.exists(output_path_td):
        file_list_td = os.listdir(output_path_td)  # Reading Files into list From TD Output Folder
        for file in file_list_td:
            td_analyser.analyse_script(output_path_td + "/" + file)  # Analysing each Files in SLI Output Folder
    print("\n" + "STATISTICS".center(80, " ") + "\n" + "__________________".center(80, " ") + "\n")
    print("SLI : \n {0}".format(sli_analyser))
    print("TD : \n {0}".format(td_analyser))

    return [sli_analyser, td_analyser]  # Sending Object List for Task 3


# endregion

if __name__ == "__main__":
    main()
