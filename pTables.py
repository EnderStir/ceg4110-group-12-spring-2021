
import prettytable

"""
This module is designed to print the data returned from the Monster Hunter World bot.  This module implements the 
REQ 260 in the Information/Requirements.md file. 
"""

class ASCiiTable:

    def __init__(self, matrix_table, max_width):
        self.matrix_table = matrix_table
        self.table_length = len(self.matrix_table)
        self._t = prettytable.PrettyTable(hrules=prettytable.ALL)
        self.max_width = int(max_width)
        self.max_column_width = []
        self.header = []
        self.data_row_length = 0
        self._make_table()
        self._set_data_row_length()

    def is_table_empty(self):
        """
        Function checks whether the table passed to the constructor was empty or not.
        :return: a boolean value
        """
        return self.table_length == 0

    def delete_table(self):
        """
        Clears the table
        """
        self._t.clear()

    def delete_a_row(self, row_number):
        """

        :param row_number: caller specifies the row number in which they wanted deleted from the table.
        If the row number is valid, it is deleted from the table.
        """

        row_number = int(row_number)
        row_number -= 1
        if row_number >= 0 and row_number <= self.data_row_length -1 :
            self._t.del_row(row_number)
            self.data_row_length -= 1
            self.table_length -= 1

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

    def get_table_length(self):
        """
        :return: table length instance variable
        """
        return self.table_length

    def get_data_row_length(self):
        """
        :return: number of data rows in table
        """
        return self.data_row_length

    def get_max_width(self):
        """
        :return: the max width instance variable
        """
        return self.max_width

    def get_total_width_of_columns(self):
        """
        :return: the sum of all max length strings in each column in the matrix table of an ACSii instance
        """
        return sum(self.max_column_width)






########################################################################################################################
########################################################################################################################
############################# Private functions to class: ASCiiTable   Please No Touch #################################
########################################################################################################################
########################################################################################################################

    def _set_data_row_length(self):
        """
        Private function to class ASCiiTable
.

        Function assigns the member variable self.dataRowLength with the length of all rows in the table
        containing the data. This length excludes the header of the table, self.matrixTable[0]
        """

        if not self.is_table_empty():
            self.data_row_length = len(self.matrix_table[1:])
        else:
            self.data_row_length = 0

    def _set_max_column_lengths(self):
        """
         Private function to class ASCiiTable
.
         Function loops through an calculates the maximum length of each column in the table. It does this by
         finding the longest string present in any column in the table. Then installs this value in the member variable
         self.columnWidth array. Where each number in the array corresponds to that columns max width.
        :return:
        """
        if not self.is_table_empty():
            for i in range(len(self.header)):
                self.max_column_width.append(max([sub[i] for sub in [[len(word) for word in index] for index in self.matrix_table[:]]]))



    @staticmethod
    def _decrement_column_width(column_width):
        """
        Function decrements a column value by one.
        :param column_width:
        :return: integer
        """
        return column_width - 1

    def _is_bigger_than_max_width(self, column_width):

        """
        Private function of class ASCiiTable
        Function gets a specified column width, and test to see if it bigger or equal to the maximum allowed
        width of the table.
        :param column_width:
        :return: boolean value
        """
        return column_width >= self.max_width

    def _resize_column_width(self, column_width):
        """
        Private function of class ASCiiTable
        Function loops through a given column width value, and decrements it by one. This is done until the column width
        value passed by caller is strictly less than the maximum allowed width of the table.
        This function is the first step in calculation of the tables maximum width per column. I formatted table's max
        width size cannot come from one single column in the table. Therefore, this function ensures this shall not
        occur.
        :param column_width:
        :return: Nothing
        """
        i = int(column_width)
        while self._is_bigger_than_max_width(i):
            i = self. _decrement_column_width(i)
        return i

    def _adjust_total_width_of_table(self):
        """
        Private function of class ASCiiTable
        Function is designed to loop until the total width of the table is re-sized to be at least less than the
        maximum width of the table, which is specified at instantiation.
        :return: Nothing
        """
        total_width_of_columns = sum(self.max_column_width)
        while self._is_bigger_than_max_width(total_width_of_columns):
            i = max(self.max_column_width)
            self._adjust_a_column_width(i)
            total_width_of_columns = sum(self.max_column_width)

    def _adjust_a_column_width(self, column_width):
        """
        Private function of class ASCiiTable
        Function exists to aid in the single decrement process of resizing a column size if needed. This function simply
        calls the decrement function, and installs the return value of that function, into the appropriate column index.
        :param column_width:  Is a single column size value.
        :return:Nothing
        """
        self.max_column_width[self.max_column_width.index(column_width)] = self._decrement_column_width(column_width)

    def _adjust_each_column_width(self):
        """
        Private function of class ASCiiTable
        Function loops through the column widths and decrements each one IF needed, until each column is at least
        less than the maximum width of the table.
        :return: Nothing
        """
        for width in self.max_column_width:
            if self._is_bigger_than_max_width(width):
                self.max_column_width[self.max_column_width.index(width)] = self._resize_column_width(width)

    def _compute_table_size(self):
        """
        Private function of class ASCiiTable
        Function acts as a glue function, which calls the functions responsible for calculating the column widths and
        resizing them if needed.
        :return: Nothing
        """
        if self.get_table_length() < 1:
            self.max_width = 0
            return
        self._adjust_each_column_width()
        self._adjust_total_width_of_table()

    def _set_column_widths(self):
        """
        Private function of class ASCiiTable
        Function loops through and installs the pre calculated column widths into the prettyTable instance.
        :return: Nothing
        """
        if self.get_table_length() < 1:
            return
        for i in range(len(self.header)):
            self._t.max_width[self.header[i]] = self.max_column_width[i]

    def _create_pretty_table(self):
        """
        Private function of class ASCiiTable
        Function installs the header fields, data of table, and size and column widths into the prettyTable
        instance (_t).
        :return: nothing
        """
        if self.get_table_length() < 1:
            return
        self._t.field_names = self.header
        [self._t.add_row(i) for i in self.matrix_table[1:]]
        self._set_column_widths()

    def _make_table(self):
        """
         Private function to class ASCiiTable
.
         Function installs the data in the table passed to this table objects constructor.
        :return:
        """
        if not self.is_table_empty():
            self.header = self.matrix_table[0]
            self._set_max_column_lengths()
            self._compute_table_size()
            self._create_pretty_table()





















