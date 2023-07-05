# CpanelChecker
Application written in Python to Checker Cpanel

Cpanel_Checker.py it is the modification that I made to the original file that I found online SpecCpanel.py

# Description:

This code is a cpanel and domain taught. The main functions of the code are as follows:

Ask the user two input files, one with a list of CPAnel URLs and another with a list of user/password pairs.

Open and read these two files, keeping the URLs on one list and user/password pairs in another.

It generates all possible combinations of URLs and user/password pairs using the Product () function of the Itetools Library.

For each combination, try to log in to the CPAEL corresponding to the URL with the user/password pair provided. Use the Requests Library to send a post application to the CPAnel with the login data.

If the login is successful, make a second post application to obtain information on the domains associated with that CPanel account.

It states the domains and subdomains associated with the account and prints them, together with the URL of the CPAnel and the login credentials, the console and two output files: Succescpanels.log and Domainnumber.txt.

If the login fails, records the CPAnel URL and the login credentials in an output file called FailedCpanels.log.

The entire process is carried out in parallel with a maximum of 10 work threads, thanks to the use of Threadoolexecator of the Concurrent.futures library.

At the end, the program waits for the user to press Enter before leaving, allowing the user to read the exit on the console.

In addition, the code includes a series of purification messages that are printed at several points to help understand what is happening.

# Website: 
https://level23hacktools.com/hackers/profile/1-deepest
