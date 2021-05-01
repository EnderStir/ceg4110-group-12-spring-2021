
import pTables as pt

"""
This test file tests the formatted table in the pTable.py module. This table is designed to print the data returned 
from the Monster Hunter World bot.  
"""
emptyTable = []

table1 = [["Name", "Email", "Location", "Occupation"],
        ["Rupp, Josh", "JMan@yahoo.com", "Atlanta", "Police Officer"],
        ["Buck, Eric", "erick.buck@wright.edu", "Dayton", "Professor"],
      ["Smith, James", "james.smithk@wright.edu", "Clemson", "Stripper"],
]

table2 = [["name", "type", "item", "location", "weapon", "event"],
          ["skylark", "monster", "none", "katikat", "great swoard", "stone wall"],
          ["shang hi kid", "doomer", "medicine", "north pole", "ban saw", "stonehenge"],
          ["", "", "", "", "", ""]
          ]


epyt = pt.ASCiiTable(emptyTable, 69)
t1 = pt.ASCiiTable(table1, 40)
t2 = pt.ASCiiTable(table2, 50)


def test_is_table_empty():

    assert epyt.is_table_empty()
    assert t1.is_table_empty() == False


def test_delete_a_row():

    assert t2.get_data_row_length() == 3
    t2.delete_a_row(3)
    assert t2.get_data_row_length() == 2
    assert t1.get_data_row_length() == 3
    t1.delete_a_row(4.65)
    assert t1.get_data_row_length() == 3
    t1.delete_a_row(2.65)
    assert t1.get_data_row_length() == 2
    t1.delete_a_row(1.65)
    assert t1.get_data_row_length() == 1
    t1.delete_a_row(0)
    assert t1.get_data_row_length() == 1


def test_get_string_version():

    assert len(t1.get_string_version()) > 0
    assert len(t2.get_string_version()) > 0


def test_output_table():

    """
    This function has been tested many times manually throughout development
    of this ASCiiTable module. Therefore, there is not need to test a print
    statement at this time.
    """
    pass


def test_get_table_length():

    assert epyt.get_table_length() == 0
    assert t1.get_table_length() == 2
    assert t2.get_table_length() == 3


def test_get_data_row_length():

    assert t1.get_data_row_length() == 1
    assert t2.get_data_row_length() == 2


def test_decrement_column_width():

    assert t1._decrement_column_width(2) == 1
    assert t1._decrement_column_width(3) == 2
    assert t1._decrement_column_width(4) == 3
    assert t1._decrement_column_width(5) == 4


def test_is_bigger_than_max_width():

    assert t1._is_bigger_than_max_width(66)
    assert t2._is_bigger_than_max_width(70)
    assert epyt._is_bigger_than_max_width(0) == False


def test_resize_column_width():

    assert t1._resize_column_width(70) < t1.get_max_width()
    assert t2._resize_column_width(100) < t2.get_max_width()


def test_adjust_total_width_of_table():

    assert t1.get_total_width_of_columns() < t1.get_max_width()
    assert t2.get_total_width_of_columns() < t2.get_max_width()


def test_compute_table_size():

    assert t1.get_total_width_of_columns() > 0
    assert t2.get_total_width_of_columns() > 0


def test_set_column_widths():

    """
    Function does not need to be explicitly tested. If this function
    did not work, then there would be no column widths installed in
    the prettyTable instance and there would be no ability to text
    wrap or see data in the table when printed.
    """
    pass


def test_create_pretty_table():

    """
    This function does not need to be explicitly tested. If this function
    was not working properly then, there would be no table at all. To even
    test the other functions above.  This function takes the ASCiiTable data
    and installs all that data into the prettyTable instance. Thus this is
    a glue function like main in C.
    """
    pass


def test_make_table():

    """
    This function does not need to be explicitly tested. This function
    installs the data into the ASCiiTable instance variables and is the
    glue function that calls all necessary functions to make a ASCiiTable.
    This is a glue function like main in C.
    """
    pass






