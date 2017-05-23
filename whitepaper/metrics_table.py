from __future__ import print_function
import lsst.sims.maf.metrics as metrics
import mafContrib as mafc
from inspect import cleandoc
import pandas as pd
import re

# Make sure strings don't get truncated.
pd.set_option('display.max_colwidth', -1)
# Go through MAF and mafContrib and generate a table of all the available metrics

def metrics2df(metricNames, metrics):
    metricList = [getattr(metrics, metric) for metric in metricNames]

    output = []
    github_root = "https://github.com/lsst/sims_maf/tree/master/python/lsst/sims/maf"
    for name, metric in zip(metricNames, metricList):
        if name[0] != name[0].lower():
            doc = metric.__doc__
            if doc is None:
                doc = 'None'
            # Take just the first line
            doc = doc.splitlines()[0]
            #path = metric.__file__
            #path = re.sub(".*sims/maf", "", path)
            #path = re.sub(".pyc", ".py", path)
            #url = github_root + path
            #output.append([name, "\href{"+url+"}{"+cleandoc(doc)+"}"])
            output.append([name, cleandoc(doc)])

    df = pd.DataFrame(output, columns=['Metric Name', 'Description'])
    return df


def table_clean(df_table):
    """
    ugh, of course the default pandas table is stupid
    """
    df_table = df_table.replace('bottomrule', 'hline')
    df_table = df_table.replace('toprule', 'hline')
    df_table = df_table.replace('midrule', 'hline')
    result = "\\begin{table} \n" + df_table + "\n \\end{table}"
    return result

excludeList = ['baseMetric', 'MetricRegistry']
metricNames = [metric for metric in dir(metrics) if ('Metric' in metric) & ('Metrics' not in metric) & (metric not in excludeList)]
df = metrics2df(metricNames, metrics)

latex_table = df.to_latex(index=False)
latex_table = table_clean(latex_table)
f = open('metrics_table.tex', 'w')
f.write(latex_table)
f.close()
main_metrics = metricNames

# Now to do the MAF contrib metrics
metricNames = [metric for metric in dir(mafc) if ('Metric' in metric) & (metric not in main_metrics)]
df = metrics2df(metricNames, mafc)
latex_table = df.to_latex(index=False)
latex_table = table_clean(latex_table)
f = open('contrib_metrics_table.tex', 'w')
f.write(latex_table)
f.close()

