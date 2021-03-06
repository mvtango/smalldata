# UNIX pipe fittings for statistics

In the quest for [command line data science](https://github.com/jeroenjanssens/data-science-at-the-command-line), 
this kit contains three command line utilities intended to be used in UNIX pipes.

All three process STDIN to STDOUT output their docstrings if run without parameters.

Python 3 is required. 

## sd_c  (smalldata count)

Is a regular expression counter filter, contained in `smalldata/counter.py`. Please see docstring for further help.

## sd_g  (smalldata groupby) 

Concatenates lines from stdin that match a regular expression, contained in `smalldata/groupby.py`. Please see docstring.

## sd_e (smalldata extract)  

In the spirit of [RegExSerDe](https://github.com/apache/hive/blob/trunk/contrib/src/java/org/apache/hadoop/hive/contrib/serde2/RegexSerDe.java), this
tool uses regular expressions to generate a CSV file from a free-form text file. It is contained in `smalldata/extract.py` and has a docstring.


## Other Useful Tools

If you've got CSV files, you should definitively check out [q](http://harelba.github.io/q/). 

## To Do

A cookbook would be nice. Showing how to analyze log files etc.

## History

Used to live in a gist: https://gist.github.com/martinvirtel/94cf47f64bf304e1c66598e93cd565c4


