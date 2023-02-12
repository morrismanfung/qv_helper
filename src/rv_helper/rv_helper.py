import numpy as np
import pandas as pd
import seaborn as sns
from scipy import stats
from tabulate import tabulate

def qv_groups(value, group, data, title, xlabel, ylabel, stat):
    fix, axes = plt.subplots(1, 2, figsize=(10, 4), constrained_layout=True)
    sns.histplot(x=value, data=data, ax=axes[0]).set(
        title=title, xlabel=xlabel, ylabel='Count'
    )
    sns.boxplot(x=value, y=group, data=data, ax=axes[1]).set(
        title=title, xlabel=xlabel, ylabel=ylabel
    )

    if (data[value].isnull().any() | data[group].isnull().any()):
            data = data.dropna()
            print('Null values are dropped in statistical tests.')
    
    group_list = data[group].unique()
    n_group = len(group_list)

    if n_group == 0:
        raise Exception('Pleaes use a data frame with data inside.')
    elif n_group == 1:
        raise Exception('Please consider using rv_dist in the package when only 1 class is used.')
    elif stat == True:
        if n_group == 2:
            if np.var(data[value]) == 0:
                raise Exception('A t test is not performed as the total variance is 0.')
            else:
                group_a = data[data[group] == group_list[0]]
                group_b = data[data[group] == group_list[0]]
                t_eq, p_eq = stats.ttest_ind(group_a[value], group_b[value])
                t_w, p_w = stats.ttest_ind(group_a[value], group_b[value], equal_var=False)
                table = [['Equal var. assumed', t_eq, p_eq], ['Equal var. not assumed', t_w, p_w]]
                print(tabulate(table, headers=['Test', 't', 'p'], floatfmt=('', '.2f', '.4f')))
                print( table)
        elif n_group > 2:
            vectors = dict()
            for i in group_list:
                vectors[i] = data[data[group] == i][value]
            if (np.array([np.var(i) for i in list(vectors.values())]) == 0).any():
                raise Exception('F statistic is not defined when within group variance is 0 in at least one of the groups.')
            else:
                F, p = stats.f_oneway(*[list(i) for i in vectors.values()])
                table = [['One-way ANOVA', F, p]]
                print(tabulate(table, headers=['Test', 'F', 'p'], floatfmt=('', '.2f', '.4f')))

def qv_scatter():
    pass

def qv_2cat():
    pass

def qv_count():
    pass

def qv_dist():
    pass

