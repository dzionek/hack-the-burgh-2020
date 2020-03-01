import datetime


class GettingData(object):

    @staticmethod
    def get_weekly_data(alldata):
        """
        returns 4 lists of tuples representing the 4 parts of the month. Each of the lists contains the places that were there during this week
        There will still be duplicates in those lists
        Each week will look like this: [(Appleton Tower, date1),(Cowgate,date2)]
        """
        week1 = []
        week2 = []
        week3 = []
        week4 = []
        for i in range(len(alldata)):
            day = ((alldata[i])[1]).day
            if 1 <= day <= 7:
                week1.append(alldata[i])
            elif 8 <= day <= 14:
                week2.append(alldata[i])
            elif 15 <= day <= 21:
                week3.append(alldata[i])
            else:
                week4.append(alldata[i])
        return week1, week2, week3, week4

    @staticmethod
    def count_per_week(week_list):
        """
        to use after the get_weekly_data method
        returns a list of the form [(5, Appleton Tower, date1), (3, Cowgate, date2)]
        It returns in descending order according to the counter
        still can contain duplicates
        """
        places_list = []
        for j in range(len(week_list)):
            places_list.append(week_list[j][0])

        tuples = []
        for i in range(len(week_list)):
            place = week_list[i][0]
            date = week_list[i][1]
            count = places_list.count(place)
            current_tuple = (count, place, date)
            tuples.append(tuple(current_tuple))
            result = sorted(tuples, key=lambda x: x[0])
            result.reverse()
        return result

    @staticmethod
    def connect_dates(lists):
        """
        to use after the count_per_week method
        return a list of tuples of the form [(5, Appleton Tower, [date1, date2]), (3, Cowgate, [date3, date4])]
        """
        tuples = []
        for i in range(len(lists)):
            place_1 = (lists[i])[1]
            dates = [(lists[i])[2]]
            for j in range(len(lists)):
                place_2 = lists[j][1]
                if place_1 == place_2 and i != j:
                    dates.append((lists[j])[2])
            current_tuple = ((lists[i])[0], place_1, dates)
            tuples.append(current_tuple)

            seen = set()

            output = [(a, b, c) for a, b, c in tuples
                      if not (b in seen or seen.add(b))]
        return output

    @staticmethod
    def main_function(list_from_input):
        week1 = GettingData.get_weekly_data(list_from_input)[0]
        week2 = GettingData.get_weekly_data(list_from_input)[1]
        week3 = GettingData.get_weekly_data(list_from_input)[2]
        week4 = GettingData.get_weekly_data(list_from_input)[3]

        if len(week1) > 0:
            temp1 = GettingData.count_per_week(week1)
            other1 = GettingData.connect_dates(temp1)
            print(other1)
        if len(week2) > 0:
            temp2 = GettingData.count_per_week(week2)
            other2 = GettingData.connect_dates(temp2)
            print(other2)
        if len(week3) > 0:
            temp3 = GettingData.count_per_week(week3)
            other3 = GettingData.connect_dates(temp3)
            print(other3)
        if len(week4) > 0:
            temp4 = GettingData.count_per_week(week4)
            other4 = GettingData.connect_dates(temp4)
            print(other4)

    """
    @staticmethod
    def remove_occurrences(given_list):
 
        #to use after the count_per_week method
        #removes occurrences of a list
 
        result = list(dict.fromkeys(given_list))
        return result
    """
