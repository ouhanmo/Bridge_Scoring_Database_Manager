# BRIDGE SCORE KEEPER Version 2.1


## Usage
Read csv files used to keep bridge scoring records.<br>
Scoring of each deal and total score is calculated automatically.

### Update Version 2.1 :
Basic database commands added:<br>
<ul>
<li>Delete</li>
<li>Switch</li>
</ul>
Program is now able to keep multiple records.<br>
CSV error processing bug fixed.

### Update Version 2.0 :
Command Line added.<br>
Write function added.<br>
Users are allowed to use the program as a score counting tool.<br>

## Run 
```
./bsk
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


