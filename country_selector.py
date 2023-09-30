




# country_matrix = [[ 'Iran, Islamic Republic', 'kachel-439-0-1', 'accordion-439-0-1-3', 'SERVICEWAHL_EN439-0-1-3-324289', 'SERVICEWAHL_EN439-0-1-3-329337', 'SERVICEWAHL_EN439-0-1-4-324269'],
#                   [ 'India', 'kachel-436-0-1', '', '', ''],
#                   [ 'Nigeria', 'kachel-232-0-1', 'accordion-232-0-1-3', 'SERVICEWAHL_EN232-0-1-3-324289', 'SERVICEWAHL_EN232-0-1-3-329337', 'SERVICEWAHL_EN232-0-1-4-324269'],
#                   [ 'Turkey', 'kachel-163-0-1', 'accordion-163-0-1-3', '', '']

#                  ]


# citizenship = 'Afghanistan'

# def country_selector(input_country):
#     for i in range(2):
#         if country_matrix[i][0] == input_country :
#             return i
        

# def id_selector():
#     id_array = ['','','','','']
#     for i in range(4):
#         id_array[i+1] = country_matrix[country_selector(citizenship)][i+1]
#     return id_array



# id_name = id_selector()
# print(id_name[1])


def id_selector(country, arg1, arg2, arg3):

    id_array =['','','']

    country_dict = {
        "*unresolved nationality (Palestinians and Kurds from Lebanon)": "998",
        "*unresolved nationality / Palestinians from Syria (Family name  A - E)": "999",
        "Iran, Islamic Republic": "439",
        "Syria (family name A - E)": "475",
        "Nigeria": "232",
        "Vietnam": "432",
        "Jordan": "445",
        "Germany": "0",
        "New Zealand": "536",
        "Tunisia": "285",
        "Egypt": "287",
        "Indonesia": "437",
        "India": "436",
        "Turkey": "163",
        "Israel": "441",
        "Pakistan": "461",
        "United States of America": "368",
        "Georgia": "430"
    }

    residency_dict = {
        # kachel-{citizenship}-0-{residence_title}
        "Apply for a residence title": '1',
        "Extend a residence title": '2'
    }

    category_dict = {
        # accordion-{citizenship}-0-{residence_title}-{category}
        "Educational purposes": "3",
        "Economic activity": "1",
        "Family reasons": "4",
        "Humanitarian grounds": "5",
        "Special rights of residence": "6"
    }

    request_type_dict = {
        # SERVICEWAHL_EN{citizenship}-0-{residence_title}-{category}-{request_type}
        # Educational purposes
        "Residence permit for attending a language course (sect. 16f para. 1)": "324289",
        "Residence permit for in-service training (sect. 16a)": "329337",
        "Residence permit for study preparation (sect. 16b para. 1)": "305156",
        "Residence permit for the purpose of studying (sect. 16b)": "305244",
        "Residence permit for the recognition of a foreign professional qualification in a non-regulated profession (sect. 16d para. 1)": "329340",
        "Residence permit for the recognition of a foreign professional qualification in a non-regulated profession (§ 16d para. 3)": "329358",
        "Residence permit for vocational training (sect. 16a)": "328338",
        "Residence permit to start a traineeship (sect. 19c para. 1)": "305303",
        "Residence permit to take part in a student exchange or to attend school (sect. 16f)": "326239",
        # Economic activity
        "EU Blue Card / Blaue Karte EU (sect. 18b para. 2)": "324659",
        "Residence permit for a freelance employment - Issuance (sect. 21 para. 5)": "328332",
        "Residence permit for foreigners with a long-term residence in an EU member state (sect. 38a)": "325475",
        "Residence permit for freelancers and self-employed persons - Extension (sect. 21)": "324288",
        "Residence permit for job-seeking qualified skilled workers - Issuance (sect. 20)": "324661",
        "Residence permit for qualified skilled workers with an academic education (sect. 18b para. 1)": "329328",
        "Residence permit for qualified skilled workers with vocational training (sect. 18a)": "305304",
        "Residence permit for scientific staff and research workers (sect. 18d)": "328457",
        "Residence permit for skilled employment in information and communication technology (sect. 19c para. 2)": "350480",
        "Residence permit for the purpose of self-employment - Issuance (sect. 21)": "305249",
        "Residence permit to start a traineeship (sect. 19c para. 1)": "305303",
        "Residence permit for Turkish employees and their family members (DAC 1/80) - Extension (sect. 4 para. 2)": "324995",
        "Residence permit to start an employment as an Au-pair (sect. 19c para. 1)": "305267",
        # Family reasons
        "Residence permit for a newborn foreign child - Initial issuance (section 33)": "324269",
        "Residence permit for spouses and children of holders of an EU Blue Card (sect. 29-32)": "328188",
        "Residence permit for spouses and children of skilled workers, students, trainees, scientists and teachers (sect. 29-32)": "327471",
        "Residence permit for spouses, parents and children of foreign citizens (sect. 29-34)": "305289",
        "Residence permit for spouses, parents and children of German citizens (sect. 28)": "328191",
        "Residence permit for spouses, parents and children of persons eligible for subsidiary protection (sect. 36a)": "328281",
        "Residence permit for Turkish employees and their family members (DAC 1/80) - Extension (sect. 4 para. 2)": "324995",
        # Humanitarian grounds
        "Residence permit in cases of hardship - extension (sect. 23a)": "324861",
        "Residence permit issued on humanitarian grounds - Extension (sect. 22 - 25)": "324859",
        # Special rights of residence
        "Residence card for family members of EU (except Germany) and EEA citizens": "324282",
        "Residence permit for foreigners with a long-term residence in an EU member state (sect. 38a)": "325475",
        "Residence permit to participate in the Working-Holiday or Youth-Mobility-Program (sect. 19c para. 1)": "305265",
        "Residence permit for Turkish employees and their family members (DAC 1/80) - Extension (sect. 4 para. 2)": "324995",
    }


    id_array[0] = f'kachel-{country_dict[country]}-0-{residency_dict[arg1]}' 
    id_array[1] = f'accordion-{country_dict[country]}-0-{residency_dict[arg1]}-{category_dict[arg2]}'
    id_array[2] = f'SERVICEWAHL_EN{country_dict[country]}-0-{residency_dict[arg1]}-{category_dict[arg2]}-{request_type_dict[arg3]}'

    return id_array


