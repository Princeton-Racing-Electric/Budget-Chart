from matplotlib import pyplot as plt
from matplotlib import rcParams as rcp

outer_width = 0.3
outer_radius = 1
inner_width = 0.3
inner_radius = outer_radius-outer_width

subgroup_budget = [11674, 14866.70, 1500, 5461.60, 7500]
total_budget = sum(subgroup_budget)

subgroup_percents = []
for subgroups in subgroup_budget:
    subgroup_percents.append(str(round((100 * subgroups / total_budget), 2)))
subgroup = ['Business ' + subgroup_percents[0] + '%', 'Mechanical ' + subgroup_percents[1] + '%',
            'Systems (Electromechanical) ' + subgroup_percents[2] + '%', 'Electrical ' + subgroup_percents[3] + '%',
            'Marine ' + subgroup_percents[4] + '%']


inner = []
inner_budget = [3425, 5000, 748.96, 2500, #Business
                5900, 2789.70, 2177, 4000, #Mechanical
                500, 700, 300, #Systems
                461.45, 366.89, 671.41, 461.85, 500, 3000, #Electrical
                4000, 3500] #Marine
for project_budget in inner_budget:
    inner.append((str(round((100 * (project_budget / total_budget)), 2))) + '%')

inner_name = [f'Team & Member Registration {inner[0]}', f'Travel & Lodging {inner[1]}', f'Website & Other Recurring Fees {inner[2]}', f'Merch & Social Events {inner[3]}', #Business
         f'Chassis {inner[4]}', f'Suspension {inner[5]}', f'Drivetrain & Steering {inner[6]}', f'Body & Aero {inner[7]}', #Mechanical
         f'Firewall {inner[8]}', f'Cooling {inner[9]}', f'Motor Controllers {inner[10]}', #Systems
         f'Vehicle Control Unit {inner[11]}', f'Grounded Low Voltage Parts {inner[12]}', f'High Voltage Parts {inner[13]}', f'Dashboard {inner[14]}', f'Motor Controller Isolation {inner[15]}', f'General Electrical Buffer Fund {inner[16]}', #Electrical
         f'Autonomous Boat Parts {inner[17]}', f'Driven Boat Parts {inner[18]}'] #Marine

a, b, c, d, o = [plt.cm.Blues, plt.cm.Reds, plt.cm.Greens, plt.cm.Purples, plt.cm.Oranges]
outer_colors = [c(0.7), a(0.7), d(0.7), b(0.7), o(0.7)]
inner_colors = [c(0.6), c(0.5), c(0.4), c(0.3), #Business
                a(0.6), a(0.5), a(0.4), a(0.3), #Mechanical
                d(0.6), d(0.5), d(0.4), #Systems
                b(0.6), b(0.5), b(0.4), b(0.3), b(0.2), b(0.1), #Electrical
                o(0.6), o(0.5)] #Marine

fig, ax = plt.subplots()
ax.axis('equal')

inner_pie = ax.pie(inner_budget, radius=inner_radius, labels = inner, labeldistance=1.05, colors=inner_colors,
                 wedgeprops=dict(width=inner_width, edgecolor='w'))
plt.setp(inner_pie)

subgroup_pie, texts = ax.pie(subgroup_budget, radius=outer_radius, labels=subgroup, labeldistance=1.1, colors=outer_colors,
                      wedgeprops = dict(width=outer_width, edgecolor='w'))
plt.setp(subgroup_pie)

for t in texts:
    t.set_fontsize(14)

plt.legend(inner_name, loc=3)

plt.text(0, 0, '$' + str(total_budget), fontsize=30, ha='center', va='center')
plt.title('Princeton Racing Electric 2021-2022 Budget', fontsize=18)

plt.show()
