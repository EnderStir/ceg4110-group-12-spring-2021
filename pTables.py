

"""
Might be an issue with this library of prettyTable
Thus you might have to install the package (PTable) in order to get this reference issue ironed out.
 """
from prettytable import PrettyTable



class MyTable:

    def __init__ (self, matrixTable, maxWidth):

        self._t = PrettyTable()
        self.matrixTable = matrixTable
        self.maxWidth = maxWidth
        self.columnWidth = []
        self.header = []
        self.TableLength = len(self.matrixTable)
        self.dataRowLength = 0
        self._put_data()
        self._get_data_row_length()



    def is_table_empty(self):
        """
        Function checks whether the table passed to the constructor was empty or not.
        :return: a boolean value
        """
        return self.TableLength == 0


    def clear_My_table(self):
        """
        Clears the table of all its rows.
        """
        self._t.clear_rows()


    def delete_a_row(self, row_number):
        """

        :param row_number: caller specifies the row number in which they wanted deleted from the table.
        If the row number is valid, it is deleted from the table.
        """

        row_number = int(row_number)
        row_number -= 1
        if row_number >= 1 and row_number <= self.dataRowLength-1 :
            self._t.del_row(row_number)


    def output_table(self):
        """
        prints the object form of the table
        """
        if not self.is_table_empty():
            print(self._t)


    def get_string_version(self):
        """
        :return: The string variable of the table representation.
        """
        if not self.is_table_empty():
            return self._t.get_string()


    def sort_table(self, s):
        """
        function checks whether or not the string passed is in the header of the table or not. If it is not,
        the function does nothing.
        :param s: String passed by the caller. If not a string when classed, function converts (s) to a string.
        :return: the string representation of the table object, sorted by the string passed by caller.
        """
        if not self.is_table_empty():
            s = str(s)
            if s in self.header:
                return self._t.get_string(sortBy=s)



########################################################################################################################
########################################################################################################################
############################# Private functions to class: MyTable    Please No Touch ###################################
########################################################################################################################
########################################################################################################################

    def _get_data_row_length(self):
        """
        Private function to class MyTable.

        Function assigns the member variable self.dataRowLength with the length of all rows in the table
        containing the data. This length excludes the header of the table, self.matrixTable[0]
        """

        if not self.is_table_empty():
            self.dataRowLength = len(self.matrixTable[1:])


    def _put_data(self):

        """
         Private function to class MyTable.
         Function installs the data in the table passed to this table objects constructor.
        :return:
        """
        if not self.is_table_empty():
            self._t.field_names = self.header = self.matrixTable[0]
            [self._t.add_row(i) for i in self.matrixTable[1:]]
            self._get_max_column_lengths()

    def _get_max_column_lengths(self):
        """
         Private function to class MyTable.
         Function loops through an calculates the maximum length of each column in the table. It does this by
         finding the longest string present in any column in the table. Then installs this value in the member variable
         self.columnWidth array. Where each number in the array corresponds to that columns max width.
        :return:
        """
        if not self.is_table_empty():
            for i in range(len(self.matrixTable[0])):
                self.columnWidth.append(max([sub[i] for sub in [[len(word) for word in index] for index in self.matrixTable[:]]]))


    def _is_String_to_long(self, s):

        """
         Private function to class MyTable.
         Function tests whether the string passed is longer or equal to the member variable self.maxWidth.

        :param s: String passed by caller
        :return: boolean value
        """
        s = str(s)
        return len(s) >= self.maxWidth

    def _truncate_word_length(self):

        pass

    def _compute_Table_width(self):

        strLength = sum(self.columnWidth)
        if self._is_String_to_long(strLength):
            pass














































#table = [["Name", "Email", "Location", "Occupation"],
#         ["Rupp, Josh", "JMan@yahoo.com", "Atlanta", "Police Officer"],
#        ["Buck, Eric", "erick.buck@wright.edu", "Dayton", "Professor"],
#       ["Smith, James", "james.smithk@wright.edu", "Clemson", "Stripper"],
#]

#my_Table = MyTable(table, 80)


#my_Table.output_table()






























