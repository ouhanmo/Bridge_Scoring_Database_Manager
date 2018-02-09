# BRIDGE SCORE KEEPER Version 1.0

## Usage
Read csv files used to keep bridge scoring records.<br>
Scoring of each deal and total score is calculated automatically.

## Run 
```
python scorekeeper.py
```

## How to Create A File
Writing a record file is very easy! <br>
All you have to do is list each deal by its Declarer, Contract, Penalty and Results.<br>
You can also use excel to keep the records and then save it as a csv file.<br>
Suppose the Contract is 3NT by South, Doubled and the result is one overtrick.<br>
Then the deal can be kept as:
```
S,3NT,1,+1
```
The third attribute is the number of doubles of the contract.<br>
The following are also accepted as equivalent to the above:<br>
```
s,3NT,1,+1
S,3nt,1,+1
S,3N,1,+1
S,3NT,1,1
...
```
Make sure the deals are listed in order!


