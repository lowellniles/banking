# banking
A python code repository demonstrating the use of pandas and ofxparse to read and analyze bank statements.

In this project, we will read and analyze financial data from a bank. The banks often provide files in csv (standard comma-separated-value), qbo (quickbooks), or qfx (quicken) formats.

I've tested this code on my own files, but for privacy I will not share my bank statements. You'll need to download your own from your online bank account.

For csv files
-------------
Check if pandas is installed with this command line:
pip show pandas

If pandas is not installed, run:
pip install pandas

Use the file banking-csv.py and modify as desired.

For qbo files
-------------
We will use ofxparse's file parsing to convert the qbo file to a pandas dataframe. That way, we can reuse the code from the csv example.

Check the pandas installation as shown above.

To install ofxparse from the command line:
pip install ofxparse

Use the file banking-qbo.py and modify as desired.

For qfx files
-------------
We will use ofxparse's file parsing to convert the qfx file to a pandas dataframe. That way, we can reuse the code from the csv example.

Check the pandas installation as shown above.

To install ofxparse from the command line:
pip install ofxparse

Use the file banking-qfx.py and modify as desired.
