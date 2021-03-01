# Task 1 By Dinesh Karthikeyan
# Student ID: 29592461
# created Date: 20th September 2018
# Completed Date: 12th October 2018


"""
Task1: FileParser class : This class is used to perform the cleaning process on the SLI and TD files provided in the ENNI Dataset.
the static method parse_clean takes in two arguments one is the path of the SLI and TD files from the ENNI Dataset and the second is the output_path,
where the cleaned files are to be saved. The outcome of this function will be cleaned SLI and TD files (i.e) the files will have oly the child
statements without any other expressions or examiner comments.
This method is called twice (i.e) one for SLI folder and one for TD folder.
"""

# region Import Section
import os
import re


# endregion
# region File Parser Class
class FileParser:
    @staticmethod
    # region Parse Clean Method
    def parse_clean(path, output_path):
        # region Check whether the output path is present else create the output folder
        if not os.path.exists(output_path):
            os.makedirs(output_path)
        # endregion
        # region If Input path is present proceed for cleaning
        if os.path.exists(path):
            # region Read the files into a list from input folder
            file_list = os.listdir(path)
            # endregion
            for file in file_list:
                output_content = []

                if file.startswith("SLI-") and file.endswith(".txt") or file.startswith("TD-") \
                        and file.endswith(".txt"):  # Check for the files to be SLI and TD text files
                    file_name = file
                    new_file = open(path + "\\" + file_name)
                    content = new_file.readlines()  # Reading contents from the file
                    for line in range(0, len(content)):
                        if content[line].startswith("*CHI:"):  # Selecting only child statements
                            if content[line].endswith(".\n"):
                                output_content.append(content[line].replace("*CHI:", "") + "\n")
                            else:

                                new_index = line + 1
                                while not content[new_index].startswith("%") \
                                        and not content[new_index].startswith("*EXA:") \
                                        and new_index != len(content) - 1:
                                    content[line] = content[line] + content[new_index]

                                    new_index += 1
                                output_content.append(
                                    content[line].replace("*CHI:", "") + "\n")  # Selecting multi line child statements
                    output_file = output_path + "\\" + file_name
                    new_cleaned_file = open(output_file.replace(".txt", "_cleaned.txt"), 'w+')
                    new_cleaned_file.writelines(
                        output_content)  # Writing only the Child statements into the output file
                    new_cleaned_file.close()
            # region Read the output files from output folder into list
            new_file_list = os.listdir(output_path)
            # endregion
            lookup_list = ["[/]", "[//]", "[*]", "(.)"]  # Look up List to keep the CHAT Symbols
            for file in new_file_list:
                new_cleaned_content = []
                new_cleaned_file = open(output_path + "\\" + file, 'r')
                new_content = new_cleaned_file.readlines()  # Reading from the each file that has child statements alone
                new_cleaned_file.close()
                for line in new_content:
                    words = re.split("[ |\t]", line)  # Converting lines to list of words
                    for word in words:
                        new_index = words.index(word)
                        # region Cleaning ">" and "<" from the words
                        if words[new_index].count(">") > 0 and words[new_index].strip() not in lookup_list:
                            words[new_index] = words[new_index].replace(">", "")
                        if words[new_index].count("<") > 0 and words[new_index].strip() not in lookup_list:
                            words[new_index] = words[new_index].replace("<", "")
                        # endregion
                        # region Cleaning "(" and ")" from the words
                        if words[new_index].count("(") > 0 and words[new_index].strip() not in lookup_list:
                            words[new_index] = words[new_index].replace("(", "")
                        if words[new_index].count(")") > 0 and words[new_index].strip() not in lookup_list:
                            words[new_index] = words[new_index].replace(")", "")
                        # endregion
                        # region Cleaning words starting with "&" and "+"
                        if words[new_index].startswith("&") and words[new_index].strip() not in lookup_list:
                            words[new_index] = words[new_index].replace(words[new_index], "")
                        if words[new_index].startswith("+") and words[new_index].strip() not in lookup_list:
                            words[new_index] = words[new_index].replace(words[new_index], "")
                        # endregion
                        # region Cleaning words enclosed in "[" and "]"
                        if words[new_index].startswith("[") and words[new_index].strip() not in lookup_list:
                            if word[word.index("[") + 1] == "*":
                                local_new = new_index
                                while words[local_new].count("]") == 0:
                                    local_new += 1
                                    words[new_index] = words[new_index] + words[local_new]
                                    lookup_list.append(words[new_index])
                            if words[new_index][words[new_index].index("[") + 1] == "^":
                                local_new = new_index
                                while words[local_new].count(
                                        "]") == 0:  # Cleaning multiple words enclosed within "[" and "]"
                                    temp_word = words[local_new]
                                    words[local_new] = words[local_new].replace(words[local_new], "")
                                    words[new_index] = words[new_index] + temp_word
                                    local_new += 1
                        if words[new_index].startswith("[") and words[new_index].strip() not in lookup_list:
                            if words[new_index].count("\n") > 0:
                                words[new_index] = words[new_index].replace(words[new_index][:-1], "")
                                words.insert(new_index, "\n")
                            words[new_index] = words[new_index].replace(words[new_index], "")
                        if words[new_index].count("[") > 0 and words[new_index].strip() not in lookup_list:
                            if words[new_index].count("\n") > 0:
                                words[new_index] = words[new_index].replace(words[new_index][:-1], "")
                                words.insert(new_index, "\n")
                            words[new_index] = words[new_index].replace(
                                words[new_index][words[new_index].index("["):len(words[new_index])], "")
                        if words[new_index].strip().endswith("]") and words[new_index].strip() not in lookup_list:
                            if words[new_index].count("\n") > 0:
                                words[new_index] = words[new_index].replace(words[new_index][:-1], "")
                                words.insert(new_index, "\n")
                            words[new_index] = words[new_index].replace(words[new_index], "")
                        # endregion
                    space = " "
                    new_line = space.join(words)  # Joining the list again to a line
                    new_cleaned_content.append(new_line)
                new_cleaned_file = open(output_path + "\\" + file, 'w')
                new_cleaned_file.flush()
                new_cleaned_file.writelines(new_cleaned_content)  # Writing the fully cleaned lines into the output file
                new_cleaned_file.close()
                print("File is cleaned and saved in {0} as {1}".format(output_path, file))
        # endregion
        # region If input folder is not present display directory not found
        else:
            print("ENNI Directory Not Found")
        # endregion
    # endregion


# endregion
# region Main
def main():
    path_sli = "ENNI Dataset/SLI"  # SLI Input folder path
    output_path_sli = "SLI_Cleaned"  # SLI Output folder path
    path_td = "ENNI Dataset/TD"  # TD Input folder path
    output_path_td = "TD_Cleaned"  # TD Output folder path
    FileParser.parse_clean(path_sli, output_path_sli)  # Calling static method of FileParser Class for SLI
    FileParser.parse_clean(path_td, output_path_td)  # Calling static method of FileParser Class for TD


# endregion

if __name__ == "__main__":
    main()
