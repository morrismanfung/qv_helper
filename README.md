# Quick Visualization Helper

> THE helper package for Quick Visualization that you need

`qv_helper` is a newly designed package to faciliate data visualization. As researchers or analysts, we often need to perform preliminary visualizations before analysis. While the plots may show some seemingly promosing effects, a statistical test may reveal the other wise.

Sometimes, we will want to look at both the plots and the statistical tests results. Currently, there is no single package or function that performs both visualization and tests simutaneously. Having statistical tests results automatically generated can facilitate the pipeline of exploratory data analysis (EDA) while helping researchers to quickly grap a better sense of the data with statistics as supplements to plots. This is why I wanto to build `qv_helper`. With `qv_helper`, visualizations and statistical tests are no longer separated by parallel processes, achieving by just 1 line of code.

While the package is specially designed for EDA, it is more recommended to be used in notebook documents instead of in the terminal.

## Usage

### Installation

Installation is easy as the package is published in PyPI.

```bash
$ pip install qv_helper
```

### `qv_groups`

To illustrate the functionalities, the [Palmer penguins dataset](https://github.com/mcnakhaee/palmerpenguins) will be used.

`qv_groups` take 1 numeric variable and 1 categorical variable to build a histogram for the numeric variable and a boxplot of the numeric variable grouped by the categorical variable. When there are more than 2 classes in the grouping variable, a one-way ANOVA test will be performed.

```python
from palmerpenguins import load_penguins
df = load_penguins()
from qv_helper.qv_helper import qv_groups
qv_groups(value='bill_length_mm', group='species', data=df, title='Bill Length in Different Species', xlabel='Bill length (mm)', ylabel='Species')
```

```text
Null values are dropped in statistical tests.
Test                F       p
-------------  ------  ------
One-way ANOVA  397.30  0.0000
```

![](docs/img/README-01-qv_groups-F.png)

When there are only 2 groups, t-tests will be performed automatically.

```python
qv_groups(value='bill_length_mm', group='sex', data=df, title='Bill Length in 2 Sex', xlabel='Bill length (mm)', ylabel='Sex')
```

```text
Null values are dropped in statistical tests.
Test                       t       p
----------------------  ----  ------
Equal var. assumed      0.00  1.0000
Equal var. not assumed  0.00  1.0000
```

![](docs/img/README-01-qv_groups-t.png)

### `qv_scatter`

`qv_scatter` takes 2 numeric values as arguments and plot the corresponding scatter plot. 2 correlation statistics will be printed based on the needs of users.

```python
qv_scatter(valuex='bill_length_mm', valuey='bill_depth_mm', data=df, title='Relationship between Bill Length and Bill Depth', xlabel='Bill Length (mm)', ylabel='Bill Depth (mm)')
```

```text
Null values are dropped in statistical tests.
Test                r       p
------------  -------  ------
Pearson's r   -0.2286  0.0000
Spearman's r  -0.2139  0.0001
```

![](docs/img/README-02-qv_scatter.png)

### `qv_2cat`

`qv_2cat` takes 2 categorical variables as arguments and plot the corresponding heatmap and a stacked barchart for to illustrate the proportion of each class in `groupx` in `groupy`. When both of the categorical variables are with exactly 2 classes, Barnard's exact test and Fisher's exact test will also be performed.

```python
qv_2cat(groupx='species', groupy='island', data=df, title_heatmap='Count of each Species on each Island',
    title_bar='Proportion of each Species on each Island', xlabel='Species', ylabel='Island')
```

```text
Test              Test statistic      Value    df       p
----------------  ----------------  -------  ----  ------
Chi-squared test  Chi-squared        299.55     4  0.0000
```

![](docs/img/README-03-qv_2cat.png)

### `qv_count`

`qv_count` takes 1 categorical variable as argument and plot a barchart. The count in numeric values will also be printed and supplemented by the the number of null values.

```python
qv_count(value='species', data=df, title='Count of each Species', label='Species')
```

```text
Group        Count
---------  -------
Adelie         152
Gentoo         124
Chinstrap       68
NA               0
```

![](docs/img/README-04-qv_count.png)

### `qv_dist`

`qv_dist` takes 1 numeric variable as argument and plot a histogram. Summary statistics will be printed as well.

```python
qv_dist(value='bill_length_mm', data=df, title='Distribution of Bill Length', label='Bill Length (mm)')
```

```text
Null values are dropped in the chart and statistics.
Statistics      Value
------------  -------
Mean            43.99
Variance        29.82
Sample size    333.00
# of NAs         0.00
Skewness         0.05
```

![](docs/img/README-05-qv_dist.png)

## Contributing

Interested in contributing? Check out the contributing guidelines. Please note that this project is released with a Code of Conduct. By contributing to this project, you agree to abide by its terms.

## License

`qv_helper` was created by Morris Chan. It is licensed under the terms of the MIT license.

## Credits

`qv_helper` was created with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).

Special thanks go to @MNBhat, @Lorraine97, @austin-shih, who finished an academic project in `prelim_eda_helper` with me. `Quick Visualizaiont Helper` is inspired by `prelim_eda_helper`. The development of the current project is agreed by all authors of `prelim_eda_helper`.
