# input_file = open('inputfile.txt', 'rU')

with open('world_bank_indicators.tsv', 'rU') as f:
    next(f)
    data_dict = {}
    stats_dict = {}
    avg_dict = {}
    country_list = []

    for line in f:
        (country, year, tran_1, tran_2, bus_1, bus_2, health_1, health_2, health_3, pop_total, pop_urban, pop_br, le_f, le_m, life_expec_total, pop_1, pop_2, pop_3, finance1, finance_2) = line.split('\t')

        data_dict[(country, year)] = [pop_total.replace(",", ""), pop_urban.replace(",", ""), life_expec_total.replace(",", "")]


        if country not in country_list:
            country_list.append(country)

    # for key, value in data_dict.iteritems():
    #     if value not in data_dict:
    #         data_dict[(year, party)] = 1
    #     else:
    #         data_dict[(year, party)] += 1

    # print country_list
    # print data_dict

    country_set_sorted = sorted(set(country_list))
    # print country_set_sorted

    for country in country_set_sorted:
        total_pop = 0
        total_urb_pop = 0
        total_life_expec = 0
        tally_life_expec = 0
        for key, value in data_dict.iteritems():


            # print 'country: ' + country
            # print 'key: ' + key
        # print key[0]
            if key[0] == country:

                # print country
                # print value

                for i in range(3):
                    temp = value[i]
                    # if i == 2:
                    #     if temp:
                    #         print 'HUSKY' + key[0] + str(temp)
                    if temp:
                        if temp.startswith('"') and temp.endswith('"'):
                            temp = temp[1:-1]
                        if i == 0:
                            # print 'temp1 ' + temp
                            total_pop += int(temp)
                        if i == 1:
                            # print 'temp2' + temp
                            total_urb_pop += int(temp)
                        if i == 2:
                            # print 'temp3 ' + temp
                            total_life_expec += int(temp)
                            tally_life_expec += 1
                            # print 'HUSKY' + key[0] + str(temp) + ' ' + str(tally_life_expec)
                stats_dict[(country)] = (total_pop, total_urb_pop, total_life_expec, tally_life_expec)
    print stats_dict


        # print stats_dict.keys()
    for key, value in stats_dict.iteritems():
        if value[1]:
            avg_urb_pop = float(value[1]) / float(value[0])
            if value[3] > 0:
                avg_life_expec = float(value[2]) / float(value[3])
            print key
            print avg_urb_pop
            avg_dict[(key)] = (avg_urb_pop, avg_life_expec)
    # print country
    # print avg_dict

    line = 'country name' + '\t' + 'average urban population ratio' + '\t' + 'average life expectancy' + '\t' + 'sum of total population in all years'  + '\t' + 'sum of urban population in all years'

    ds = [stats_dict, avg_dict]
    d = {}
    for k in stats_dict.iterkeys():
        d[k] = tuple(d[k] for d in ds)
    print d



                # print country
                # print total_pop
                # print total_urb_pop

                # print key
                # print value[0]


                # print value
                # print 'country ' + country
                # print 'key ' + key[0]

        # print country_list
        # for key in data_dict:
        #     print key
    # print data_dict
    # for key in data_dict:
    #     if key not in country_list:
    #         country_list.append(key)
    #
    #
    # # #
    #     for x in data_dict:
    #         print x
    # #     for key in data_dict:
                # print data_dict[(country, year)][0]
    #         temp_pop = data_dict[(country)][0]
    #         # print temp_pop
    #         if temp_pop.startswith('"') and temp_pop.endswith('"'):
    #             temp_pop = temp_pop[1:-1]
    #                     #why didn't this work: temp.replace('\"','') OR temp.strip()
    #             # print temp
    #         if temp_pop:
    #                 # print str(temp_pop) '+ '
    #             total_pop += int(temp_pop)
    #                 # print total_pop
    #         print country
    #         print total_pop
    # # #
    #
    #
    #             # for i in range(2):
    #             # # print range
    #             #     temp = data_dict[(country)][i]
    #             #     if temp.startswith('"') and temp.endswith('"'):
    #             #         temp = temp[1:-1]
    #             #         #why didn't this work: temp.replace('\"','') OR temp.strip()
    #             # # print temp
    #             #     if temp:
    #             #         if i == 0:
    #             #             total_pop += int(temp)
    #             #         if i == 1:
    #             #             total_urb_pop += int(temp)
    #             #             print 'TEMP URBAN' + str(temp)
    #             #         if i == 2:
    #             #             total_life_expec += int(temp)
    #             #             print 'LIFE EXPEC' + str(temp)
    #             #
    #             # print total_pop
    #             # print total_urb_pop
    #             # print total_life_expec
    #
    #
    #
    #             temp_urb_pop = data_dict[(country)][1]
    #             if temp_urb_pop.startswith('"') and temp_urb_pop.endswith('"'):
    #                 temp_urb_pop = temp_urb_pop[1:-1]
    #                     #why didn't this work: temp.replace('\"','') OR temp.strip()
    #             # print temp
    #             if temp_urb_pop:
    #                 total_urb_pop += int(temp_urb_pop)
    #                 # print total_urb_pop
    #
    #     #
    #     # print country
    #     # print total_pop
    #     # print total_urb_pop
    #
    #     # if key not in country_list:
    #     #     country_list.append(key)
    #     #     break
    # # print sorted(country_list) #working
    #
    #
    #
    #
    #
    # # country_list = data_dict.keys()
    # # sorted_countries = sorted(set([x[0] for x in year_party_list]))
