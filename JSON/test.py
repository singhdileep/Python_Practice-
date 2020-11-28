import json
# people_details='''

# {
#     "people":[
#         {
#             "name":"Dileep",
#             "phone":"9005512324",
#             "addr":"Deoria",
#             "pin":"274703"

#         },
#         {
#             "name":"Raj",
#             "phone":"9005512324",
#             "addr":"GKP",
#             "pin":"274702"
#         }



#     ]
# }

# '''

# data=json.loads(people_details)
# print(data)

'''Retriving data from API'''

# from urllib.request import urlopen

# # with urlopen("https://finance.yahoo.com/webservice/v1/symbols/allcurrencies/quote?format=json") as response:
# with urlopen('http://data.nba.net/prod/v2/2018/teams.json') as response:
#     source=response.read()
# data=json.loads(source)    
# data1=json.dumps(data,indent=2)
# # print(data.keys())
# # print(data1)  

'''This code is for dump data into the json file'''
# nba_teams = [team for team in data['league']['standard'] if team['isNBAFranchise']]
# with open('nba_teams.json', 'w') as f:
#     json.dump(nba_teams, f, indent = 4, sort_keys = True)




'''Reading JSON from Files'''


# with open('nba_teams.json')as f:
#     data=json.load(f)
#     data1=json.dumps(data,indent=2)
# print(data1)    


