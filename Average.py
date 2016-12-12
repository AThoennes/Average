class Average:
    # main method
    def main():

        # take in the number of grades
        numOfGrades = int(input("How many grades are there? "))

        # set the list size to the amount of grades
        grades = [numOfGrades]

        points = 0.0
        average = 0.0

        i = 0
        while (i < numOfGrades):

            #take in a grade
            grade = int(input("Enter a grade: "))

            # add it to the list
            grades.append(grade)

            # add tot he point total
            points = points + grade

            i += 1

        # show the total points
        print ("\nTotal Points: " , points)

        # calculate the average
        average = points / numOfGrades

        # show the average
        print ("Average: " , average)

    main()
