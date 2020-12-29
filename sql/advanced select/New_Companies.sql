select com.company_code, 
        com.founder,  
        count(DISTINCT l.lead_manager_code), 
        count(DISTINCT sm.senior_manager_code),
        count(DISTINCT m.manager_code), 
        count(DISTINCT e.employee_code)
from Company com,  Lead_Manager l, Senior_Manager sm, Manager m, Employee e
       where com.company_code = l.company_code AND
              l.lead_manager_code = sm.lead_manager_code AND
              sm.senior_manager_code = m.senior_manager_code AND
              m.manager_code = e.manager_code
group by com.company_code, com.founder
order by com.company_code;