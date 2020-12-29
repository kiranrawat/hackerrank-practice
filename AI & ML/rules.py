import pandas as pd

#function for arranging rules
def arrangingRules(rules):
    # Write your code here
    x_rules_list, xy_rules_list = [], []
    #iterate through rules
    for rule in rules:
        x = rule.split('}=>{')[0][1:].split(',')
        y = rule.split('}=>{')[1][:-1].split(',')
        x_rules_list.append(x)
        xy_rules_list.append(x + y)
    #reading the census data
    census = pd.read_csv('census.csv', header=None)
    total_census = len(census)
    census_records = []
    
    #iterate through census records to convert values to string
    for i in range(0, total_census):
        census_records.append([str(census.values[i, j]) for j in range(0, 12)])
    
    #list to store support
    x_rules_support, xy_rules_support = [], []

    for j in range(len(x_rules_list)):
        x_rule_count = 0
        xy_rule_count = 0
        for i in range(len(census_records)):
            flag = True
            for rule in x_rules_list[j]:
                if rule not in census_records[i]:
                    flag = False
            if flag:
                x_rule_count += 1
            flag = True
            for rule in xy_rules_list[j]:
                if rule not in census_records[i]:
                    flag = False
            if flag:
                xy_rule_count += 1
        x_rules_support.append(x_rule_count / 30162)
        xy_rules_support.append(xy_rule_count / 30162)

    confidences = [float(xy) / float(x) for x, xy in zip(x_rules_support, xy_rules_support)]
    result = list(zip(rules, confidences))
    result = sorted(result, key=lambda x: x[1], reverse=True)
    rules = []
    #iterating through results to append the rules
    for rule, confid in result:
        rules.append(rule)
    return rules