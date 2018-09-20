# tdwpDB

## Goals

```
1 - Collect and aggregate unit sales of tour merchandise into a mySQL database.
2 - Analyze historic sales trends to forecast sales and enhance stock mgmt.
3 - More accurately predict merchandise sales for tour budgeting.
```

## Overall Process
 
```
1 - Collect data (internal, scrapers, etc.)
2 - Generate features 
3 - store processed data into mySQL
4 - EDA FTW
5 - Explore models
6 - Report findings and methods of implementation
```

## Loading Data
```
(1) upload new data files from atvenue into appropriate _data/raw/_ dirs.
	|--> summaries from _report/tour summary_ 
	|--> sales from _report/sales report_ 
	|--> daily from _tours/shows/completed_

(2) RUN src/data/**process_data.bat**

(3) RUN src/features/**generate_features.bat**
```