Profiling Tool
===================

.. contents:: **Table of Contents**
    :backlinks: none

Installation
------------

This app runs on Python 3.5+.

For installation of run requirements:

.. code-block:: bash

    $ pipenv install

For installation of development requirements:

.. code-block:: bash

    $ pipenv install --dev


Usage
-------------

Run web tool using WSGI tool, or, for development purposes by:

.. code-block:: bash

    $ ./manage.py runserver

And connecting on http://127.0.0.1:8000

Instructions
------------

The task:

To demonstrate the potential for a data profiling tool in python 3 or pyspark (suggested timeframe of approx.. four hours).

Context: this tool is required to support work on ML models, where we need to rapidly query and understand the data landscape prior to model development.

One or more of the road safety data csv files from 2015/16/17/etc., should be used as an example. See data link here: https://data.gov.uk/dataset/road-accidents-safety-data



Create a python data profiling tool with the following features:

* The data profiling tool should enable the user to either individually or on mass action the following:

* Specify a particular data frame

* Specify a particular column and generate basic statistical information and visuals for that column, i.e., histograms, pareto plots etc.

* Specify a particular column and generate statistical information about how that column varies over a specified time window. For example, we might be interested in knowing how the distribution in the ‘Number_of_Casualties varies by day, week or month for a given dataframe.



Core Output:

Creating a complete profiling package could take a long time and is not expected as there are multiple issues to contend with regarding data type and quality.

Instead the idea here is to demonstrate the ‘potential’ for a data profiling tool to aid ML workflows. The focus should be on creating a clear minimal viable product for demo purposes in order guide future development.

Work should demonstrate:

* Good coding practise

* Presence of unit, integration and acceptance tests

* Test driven development

* Use of class methods

Results should include:

* Code should be made available on a GIT Repo and accessible via a web URL.

* Git documentation highlighting what the profiling tool does and how to execute it. It should also highlight its scope, scalability/limitations and future features that could be considered for development.

* Documentation regarding func/class methods inputs/outputs should also be available in sphinx.

License
-------

This tool is distributed under the terms of `GPL v3 License <https://choosealicense.com/licenses/gpl-3.0/>`_
