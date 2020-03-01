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
    def are_dates_close(dates1, dates2):
        """
        takes 2 lists of dates and checks if there is one date that "clashes" with another one
        """
        NUM_HOURS_CONTAMINATION = 4

        if len(dates1) >= len(dates2):
            for i in range(len(dates2)):
                for j in range(len(dates1)):
                    if abs(dates2[i] - dates1[j]) <= datetime.timedelta(hours=NUM_HOURS_CONTAMINATION):
                        return True
        else:
            for i in range(len(dates1)):
                for j in range(len(dates2)):
                    if abs(dates1[i] - dates2[j]) <= datetime.timedelta(hours=NUM_HOURS_CONTAMINATION):
                        return True
        return False

    @staticmethod
    def is_dangerous(list1, list2):
        """
        should be in the form as after the method connect_dates
        takes 2 inputs, one from the contaminated, one from the healthy, and returns true if the healthy one is in danger
        """
        if len(list1) >= len(list2):
            for i in range(len(list2)):
                place_1 = list2[i][1]
                dates_1 = list2[i][2]
                for j in range(len(list2)):
                    place_2 = list1[j][1]
                    dates_2 = list1[j][2]
                    if place_1 == place_2 and GettingData.are_dates_close(dates_1, dates_2):
                        return True
        else:
            for i in range(len(list1)):
                place_1 = list1[i][1]
                dates_1 = list1[i][2]
                for j in range(len(list1)):
                    place_2 = list2[j][1]
                    dates_2 = list2[j][2]
                    if place_1 == place_2 and GettingData.are_dates_close(dates_1, dates_2):
                        return True
        return False

    @staticmethod
    def main_function(corona, healthy):
        corona_week1 = GettingData.get_weekly_data(corona)[0]
        corona_week2 = GettingData.get_weekly_data(corona)[1]
        corona_week3 = GettingData.get_weekly_data(corona)[2]
        corona_week4 = GettingData.get_weekly_data(corona)[3]

        healthy_week1 = GettingData.get_weekly_data(healthy)[0]
        healthy_week2 = GettingData.get_weekly_data(healthy)[1]
        healthy_week3 = GettingData.get_weekly_data(healthy)[2]
        healthy_week4 = GettingData.get_weekly_data(healthy)[3]

        is_contaminated = False

        if len(corona_week1) > 0:
            if len(healthy_week1) > 0:
                corona_temp1 = GettingData.count_per_week(corona_week1)
                healthy_temp1 = GettingData.count_per_week(healthy_week1)
                corona_other1 = GettingData.connect_dates(corona_temp1)
                healthy_other1 = GettingData.connect_dates(healthy_temp1)
                if GettingData.is_dangerous(corona_other1, healthy_other1):
                    is_contaminated = True

        if len(corona_week2) > 0:
            if len(healthy_week2) > 0:
                corona_temp2 = GettingData.count_per_week(corona_week2)
                healthy_temp2 = GettingData.count_per_week(healthy_week2)
                corona_other2 = GettingData.connect_dates(corona_temp2)
                healthy_other2 = GettingData.connect_dates(healthy_temp2)
                if GettingData.is_dangerous(corona_other2, healthy_other2):
                    is_contaminated = True

        if len(corona_week3) > 0:
            if len(healthy_week3) > 0:
                corona_temp3 = GettingData.count_per_week(corona_week3)
            healthy_temp3 = GettingData.count_per_week(healthy_week3)
            corona_other3 = GettingData.connect_dates(corona_temp3)
            healthy_other3 = GettingData.connect_dates(healthy_temp3)
            if GettingData.is_dangerous(corona_other3, healthy_other3):
                is_contaminated = True

        if len(corona_week4) > 0:
            if len(healthy_week4) > 0:
                corona_temp4 = GettingData.count_per_week(corona_week4)
                healthy_temp4 = GettingData.count_per_week(healthy_week4)
                corona_other4 = GettingData.connect_dates(corona_temp4)
                healthy_other4 = GettingData.connect_dates(healthy_temp4)
                if GettingData.is_dangerous(corona_other4, healthy_other4):
                    is_contaminated = True

        if is_contaminated:
            print("You are in trouble")
        else:
            print("Don't worry, you are not in trouble")
