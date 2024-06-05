# school_data.py
# Daniel Ikponmwen
#
# A terminal-based application for computing and printing statistics based on given input.



import numpy as np
from given_data import year_2013, year_2014, year_2015, year_2016, year_2017, year_2018, year_2019, year_2020, year_2021, year_2022
year_2013

# Dictionary for School data
schools_data = {
    'school_1': {'name': 'Centennial High School', 'code': 1224},
    'school_2': {'name': 'Robert Thirsk School', 'code': 1679},
    'school_3': {'name': 'Louise Dean School', 'code': 9626},
    'school_4': {'name': 'Queen Elizabeth High School', 'code': 9806},
    'school_5': {'name': 'Forest Lawn High School', 'code': 9813},
    'school_6': {'name': 'Crescent Heights High School', 'code': 9815},
    'school_7': {'name': 'Western Canada High School', 'code': 9816},
    'school_8': {'name': 'Central Memorial High School', 'code': 9823},
    'school_9': {'name': 'James Fowler High School', 'code': 9825},
    'school_10': {'name': 'Ernest Manning High School', 'code': 9826},
    'school_11': {'name': 'William Aberhart High School', 'code': 9829},
    'school_12': {'name': 'National Sport School', 'code': 9830},
    'school_13': {'name': 'Henry Wise Wood High School', 'code': 9836},
    'school_14': {'name': 'Bowness High School', 'code': 9847},
    'school_15': {'name': 'Lord Beaverbrook High School', 'code': 9850},
    'school_16': {'name': 'Jack James High School', 'code': 9856},
    'school_17': {'name': 'Sir Winston Churchill High School', 'code': 9857},
    'school_18': {'name': 'Dr E. P. Scarlett High School', 'code': 9858},
    'school_19': {'name': 'John G Diefenbaker High School', 'code': 9860},
    'school_20': {'name': 'Lester B. Pearson High School', 'code': 9865}
}

# Create 3D array with enrolments data provided by reshaping list of 1D arrays
enrollments = np.array([
    year_2013, year_2014, year_2015, year_2016, year_2017, 
    year_2018, year_2019, year_2020, year_2021, year_2022
]).reshape(10, 20, 3)



class SchoolEnrollmentStats:
    """
    Class for handling school enrollment statistics.
    """

    def __init__(self, data, schools):
        self.enrollments = data
        self.schools = {school['code']: school for school in schools.values()}
        self.school_names = {school['name']: school['code'] for school in schools.values()}

    def get_array_info(self):
        """
        Prints the shape and dimensions of the enrollment array.
        """
        print("Shape of full data array: ", self.enrollments.shape)
        print("Dimensions of full data array: ", self.enrollments.ndim)

    def get_school_stats(self, school_identifier):
        """
        Prints the statistics for a specific school given its name or code.
        
        Parameters:
        school_identifier (str/int): The name or code of the school.
        
        Raises:
        ValueError: If the school name or code is not valid.
        """
        if isinstance(school_identifier, int) and school_identifier in self.schools:
            print("\n***Requested School Statistics***\n")
            school_code = school_identifier
            school_name = self.schools[school_code]['name']
        elif isinstance(school_identifier, str) and school_identifier in self.school_names:
            print("\n***Requested School Statistics***\n")
            school_name = school_identifier
            school_code = self.school_names[school_name]
        else:
            raise ValueError("You must enter a valid school name or code.\n")
        
        index = list(self.schools.keys()).index(school_code)
        school_data = self.enrollments[:, index, :]
        
        print(f"School Name: {school_name}, School code: {school_code}")
        self.print_school_statistics(school_data)

    def print_school_statistics(self, school_data):
        """
        Helper method to calculate and print school-specific statistics.
        
        Parameters:
        school_data (ndarray): The enrollment data for the school.
        """
        mean_grade_10 = int(np.nanmean(school_data[:, 0]) )
        mean_grade_11 = int(np.nanmean(school_data[:, 1]) )
        mean_grade_12 = int(np.nanmean(school_data[:, 2]) )
        
        highest_enrollment =int(np.nanmax(school_data))
        lowest_enrollment = int(np.nanmin(school_data) )
        
        total_enrollment_yearly = np.nansum(school_data, axis=1).astype(int)
        total_ten_year_enrollment = int(np.nansum(total_enrollment_yearly) )
        mean_total_yearly_enrollment = int(np.nanmean(total_enrollment_yearly))
        
        enrollments_over_500 = school_data[school_data > 500].astype(int)
        
        print(f"Mean enrollment for Grade 10: {int(mean_grade_10)}")
        print(f"Mean enrollment for Grade 11: {int(mean_grade_11)}")
        print(f"Mean enrollment for Grade 12: {int(mean_grade_12)}")
        print(f"Highest enrollment for a single grade: {int(highest_enrollment)}")
        print(f"Lowest enrollment for a single grade: {int(lowest_enrollment)}")
        print(f"Total enrollment for each year from 2013: {total_enrollment_yearly[0]}")
        print(f"Total enrollment for each year from 2014: {total_enrollment_yearly[1]}")
        print(f"Total enrollment for each year from 2015: {total_enrollment_yearly[2]}")
        print(f"Total enrollment for each year from 2016: {total_enrollment_yearly[3]}")
        print(f"Total enrollment for each year from 2017: {total_enrollment_yearly[4]}")
        print(f"Total enrollment for each year from 2018: {total_enrollment_yearly[5]}")
        print(f"Total enrollment for each year from 2019: {total_enrollment_yearly[6]}")
        print(f"Total enrollment for each year from 2020: {total_enrollment_yearly[7]}")
        print(f"Total enrollment for each year from 2021: {total_enrollment_yearly[8]}")
        print(f"Total enrollment for each year from 2022: {total_enrollment_yearly[9]}")
        print(f"Total ten-year enrollment: {int(total_ten_year_enrollment)}")
        print(f"Mean total enrollment over 10 years: {int(mean_total_yearly_enrollment)}")
        if enrollments_over_500.size == 0:
            print("No enrollments over 500.")
        else:
            median_over_500 = int(np.median(enrollments_over_500))
            print(f"For all enrolments over 500, the median value was: {int(median_over_500)}")

    def print_general_stats(self):
        """
        Prints general statistics about the enrollment data.
        """
        mean_2013 = int(np.nanmean(self.enrollments[0, :, :]))
        mean_2022 = int(np.nanmean(self.enrollments[-1, :, :]))
        total_graduating_2022 = int(np.nansum(self.enrollments[-1, :, 2]) )
        highest_enrollment = int(np.nanmax(self.enrollments))
        lowest_enrollment = int(np.nanmin(self.enrollments) )
        
        print(f"The mean enrollment in 2013: {int(mean_2013)}")
        print(f"The mean enrollment in 2022: {int(mean_2022)}")
        print(f"Total graduating class of 2022: {int(total_graduating_2022)}")
        print(f"Highest enrollment for a single grade: {int(highest_enrollment)}")
        print(f"Lowest enrollment for a single grade: {int(lowest_enrollment)}\n")

 


def main():
    
    print("\nENSF 692 School Enrollment Statistics\n")
    stats = SchoolEnrollmentStats(enrollments, schools_data)
    
    # Print Stage 1 requirements here
    stats.get_array_info()

    # Prompt for user input and print stage 2 requirements
    while True:
        try:
            user_input = input("Please enter the high school name or school code: ")
            if user_input.isdigit():
                user_input = int(user_input)
            stats.get_school_stats(user_input)
            break
        except ValueError as e:
            print(e)
    
    # Print Stage 3 requirements here
    print("\n***General Statistics for All Schools***\n")
    stats.print_general_stats()


if __name__ == '__main__':
    main()

