from __future__ import print_function
import lsst.sims.maf.metrics as metrics
import mafContrib as mafc
from inspect import cleandoc
import pandas as pd
import re
import textwrap
import numpy as np

# Make sure strings don't get truncated.
pd.set_option('display.max_colwidth', -1)
# Go through MAF and mafContrib and generate a table of all the available metrics

def metrics2df(metricNames, metrics, wraplength=80):
    metricList = [getattr(metrics, metric) for metric in metricNames]

    output = []
    github_root = "https://github.com/lsst/sims_maf/tree/master/python/lsst/sims/maf"
    names = []
    docs = []
    for name, metric in zip(metricNames, metricList):
        #if name[0] != name[0].lower():
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
        doc = textwrap.wrap(cleandoc(doc), wraplength)
        #if len(doc) > 1:
        #    doc = ' \n '.join(doc)
        #else:
        #    doc = doc[0]
        names.append(name)
        docs.append(doc)
        #output.append([name, doc])
    for name, doc in zip(names, docs):
        output.append([name, doc[0]])
        if len(doc) > 1:
            for add_doc in doc[1:]:
                output.append(['', add_doc])


    df = pd.DataFrame(output, columns=['Metric Name', 'Description'])
    return df


def table_clean(df_table, title=''):
    """
    ugh, of course the default pandas table is stupid
    """
    df_table = df_table.replace('bottomrule', 'hline')
    df_table = df_table.replace('toprule', 'hline')
    df_table = df_table.replace('midrule', 'hline')
    result = '\\begin{table}\n\\scriptsize\n\\caption{%s}\n'%title + df_table+'\n\\end{table}'
    #result = "\\begin{deluxetable}{ll} \n \\startdata \n" + df_table + "\n \\end{deluxetable}"
    # XXX insert \enddata before end tabular
    #loc = result.find('\\end{tabular}')
    #result = result[0:loc] + "\n \\enddata \n" + result[loc:]
    #result = result.replace('\\end{tabular}', '')
    #result = result.replace('\\begin{tabular}{ll}', '')

    return result

excludeList = ['baseMetric', 'MetricRegistry']
metricNames = [metric for metric in dir(metrics) if ('Metric' in metric) & ('Metrics' not in metric) & (metric not in excludeList)]
# get rid of some lower case issues
newList = []
for metric in metricNames:
    if metric[0] != metric[0].lower():
        newList.append(metric)
    elif metric[0].upper()+metric[1:] not in metricNames:
        newList.append(metric)
    else:
        pass
metricNames = newList

df = metrics2df(metricNames, metrics)
block_size = 45
ind = np.arange(0, len(df)+block_size, block_size)
ind[np.where(ind > len(df)-1)] = len(df)-1
#import pdb ; pdb.set_trace()
f = open('metrics_table.tex', 'w')
for i in range(len(ind)-1):
    if i ==0:
        title = "MAF Metrics"
    else:
        title = "MAF Metrics Continued..."
    sub_df = df.iloc[ind[i]:ind[i+1]]
    latex_table = sub_df.to_latex(index=False)
    latex_table = table_clean(latex_table, title=title)
    f.write(latex_table)
    f.write('\n')
f.close()
main_metrics = metricNames

# Now to do the MAF contrib metrics
metricNames = [metric for metric in dir(mafc) if ('Metric' in metric) & (metric not in main_metrics) & ('Metrics' not in metric) ]
# Toss out some remnant lower-case things
metricNames = [metric for metric in metricNames if (metric[0] != metric[0].lower())]

df = metrics2df(metricNames, mafc)
latex_table = df.to_latex(index=False)
latex_table = table_clean(latex_table, title='Contributed MAF Metrics')
f = open('contrib_metrics_table.tex', 'w')
f.write(latex_table)
f.close()

