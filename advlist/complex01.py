#!/usr/bin/env python3
"""Alta3 Research | RZFeeser
   List - simple list"""

def main():
    # create a list called list1
    list1 = ["cisco_nxos", "arista_eos", "cisco_ios"]

    # display list1
    print(list1)

    # display second item in list
    print(list1[1])

    # create a new list containing a single item
    list2=["juniper"]

    # extend list1 by list2 (smush them together)
    list1.extend(list2)

    # display updated list 1
    print(list1)

    # create list3
    list3=["10.1.0.1", "10.2.0.1", "10.3.0.1"]

    # use append to add list 3 to end of list 1
    list1.append(list3)

    # display the new complex list1
    print(list1)

    #display item 5 in list1
    print(list1[4])

    #display only first ip address in item5 of list1
    print(list1[4][0])




main()

