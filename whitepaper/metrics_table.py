from __future__ import print_function
import lsst.sims.maf.metrics as metrics
import mafContrib as mafc
from inspect import cleandoc
import pandas as pd
import re


def metrics2df(metricNames, metrics):
    metricList = [getattr(metrics, metric) for metric in metricNames]

    output = []
    github_root = "https://github.com/lsst/sims_maf/tree/master/python/lsst/sims/maf"
    for name, metric in zip(metricNames, metricList):
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

    df = pd.DataFrame(output)
    return df

metricNames = [metric for metric in dir(metrics) if ('Metric' in metric) & ('Metrics' not in metric)]
df = metrics2df(metricNames, metrics)

latex_table = df.to_latex(index=False)
f = open('metrics_table.tex', 'w')
f.write(latex_table)
f.close()
main_metrics = metricNames

# Now to do the MAF contrib metrics
metricNames = [metric for metric in dir(mafc) if ('Metric' in metric) & (metric not in main_metrics)]
df = metrics2df(metricNames, mafc)
latex_table = df.to_latex(index=False)
f = open('contrib_metrics_table.tex', 'w')
f.write(latex_table)
f.close()

