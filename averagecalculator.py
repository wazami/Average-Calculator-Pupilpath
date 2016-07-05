
import sys
import pymongo

def individual_class_calculator():
    name_of_class = raw_input("Insert class name: ")
    deciding_values_amount = input("How many elements decide your average for this class?: ")
    individual_class_elements = []
    all_hundreds = 100
    for x in range(deciding_values_amount):
        variable_creator = raw_input(
            "Element that is factored in to decide your average (EX: homework, tests, classwork): ")
        variable_weight = input(
            "What percent of your grade is this element?(Please put percent in decimal form, EX: 20 percent would be .20): ")
        element_grades = []
        grade_quant = input("How many %s grades have you had?: " % variable_creator)
        if grade_quant < 9:
            for x in range(grade_quant):
                grade_inputter = input("Please input a %s grade: " % variable_creator)
                element_grades.append(grade_inputter)
            num = float(sum(element_grades))
            den = float(len(element_grades))
            pre_weight_grades = num / den
            weight_grades = pre_weight_grades * variable_weight
            individual_class_elements.append(weight_grades)
        else:
            inquiryon100 = raw_input("Seems like you have a lot of grades. Are all of these grades 100s? [Y/N]: ")
            inquiryon100 == inquiryon100.lower()
            if inquiryon100 == 'y':
                for x in range(grade_quant):
                    element_grades.append(all_hundreds)
            elif inquiryon100 == 'n':
                samegrade_inquiry = raw_input("Are all of these grades the same grades? [Y/N]: ")
                samegrade_inquiry = samegrade_inquiry.lower()
                if samegrade_inquiry == 'y':
                    whatgrade = input("What grade are all of these grades?: ")
                    for x in range(grade_quant):
                        element_grades.append(whatgrade)
                    num = float(sum(element_grades))
                    den = float(len(element_grades))
                    pre_weight_grades = num / den
                    weight_grades = pre_weight_grades * variable_weight
                    individual_class_elements.append(weight_grades)
                elif samegrade_inquiry == 'n': #convert the below to function maybe and then call it?
                    for x in range(grade_quant):
                        grade_inputter = input("Please input a %s grade: " % variable_creator)
                        element_grades.append(grade_inputter)
                    num = float(sum(element_grades))
                    den = float(len(element_grades))
                    pre_weight_grades = num / den
                    weight_grades = pre_weight_grades * variable_weight
                    individual_class_elements.append(weight_grades)

    class_average = sum(individual_class_elements)
    print(individual_class_elements)
    print("Calculations complete. Your class average is %s" % class_average)


def overall_average_calculator():
    classes = input("How many total classes do you have?: ")
    amnt_wght_class = input("How many of your classes are weighted?: ")
    if amnt_wght_class == 0:
        user_classes = {}
        averages = []
        for x in range(classes):
            name_of_class = raw_input("Insert class name: ")
            grade_in_class = input("What is your grade in this class?: ")
            user_classes[name_of_class] = grade_in_class
            averages.append(grade_in_class)
        num = float(sum(averages))
        den = float(len(averages))
        overall_avg = num / den
        print("Calculations done. Your overall average is %s" % overall_avg)
        say_inputted_grades(user_classes)
    else:
        # perhaps add a dictionary here where each class gets a weight
        user_classes = {}  # dictionary with all the users classes
        weighted_grades = []  # list used to store the grades for future calculation
        for x in range(amnt_wght_class):
            name_of_class = raw_input("Insert class name: ")
            grade_in_class = input("What is your grade in this class?: ")
            weight_of_class = input(
                "What is the weight of this class? (you must represent your weighting as a decimal, like 1.05(5 per cent weighting), 1.10 (10 percent weighting), etc: ")
            weighted_avg = grade_in_class * weight_of_class
            user_classes[name_of_class] = weighted_avg
            weighted_grades.append(weighted_avg)
        if amnt_wght_class == classes:
            num = float(sum(weighted_grades))
            den = float(sum(weighted_grades))
            overall_avg = num / den
            print("Calculations complete. Your overall average is %s" % overall_avg)
            say_inputted_grades(user_classes)

        else:
            remaining = classes - amnt_wght_class
            regular_grades = []
            for x in range(remaining):
                name_of_class = raw_input("Insert class name: ")
                grade_in_class = input("What is your grade in this class?: ")
                user_classes[name_of_class] = grade_in_class
                regular_grades.append(grade_in_class)
            num = float(sum(weighted_grades)) + float(sum(regular_grades))
            den = float(len(weighted_grades)) + float(len(regular_grades))
            overall_avg = num / den
            print("Calculations complete. Your overall average is %s" % overall_avg)
            say_inputted_grades(user_classes)
def say_inputted_grades(user_classes):
    see_grades = raw_input("Would you like to double-check and see if you inputted your grades correctly? [Y/N]: ")
    see_grades = see_grades.lower()
    if see_grades == 'y':
        print("Here are the grades you inputed: %s" % user_classes)
    elif see_grades == 'n':
        print("Alright. Thank you. You may exit the program now.")
    else:
        print("No valid input given. You may exit the program.")

all_or_ind = raw_input("Would you like to calculate your (O)verall average or an (I)ndividaul class average? [O / I]: ")
all_or_ind = all_or_ind.lower()
if all_or_ind == "o":
    overall_average_calculator()

elif all_or_ind == 'i':
    individual_class_calculator()
    more_calc = raw_input("Do you need to calculate more individual class averages? [Y/N]: ")
    more_calc = more_calc.lower()
    if more_calc == 'y':
        how_many_loops = input("How many more individual class averages do you need to calculate?: ")
        for x in range(how_many_loops):
            individual_class_calculator()
    elif more_calc == 'n':
        overall_calc = raw_input("Would you like to calculate your overall average? [Y/N]: ")
        overall_calc = overall_calc.lower()
        if overall_calc == 'y':
            overall_average_calculator()
        elif overall_calc == 'n':
            print("Thank you for using the program. Exiting...")
            sys.exit()
        else:
            print("No valid input given. Exiting...")
            sys.exit()

            ##TO DO
            #Perhaps make a login system with PyMongo where they can record their data and then encrypt that data
                #well, the passwords at least