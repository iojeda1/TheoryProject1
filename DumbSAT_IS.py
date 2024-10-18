# Incremental Search 

import time
import random

def incremental(Wff, Nvars, Nclauses, Assignment):
    satisfiable = False
    attempts = 0 
    max_attempts = 2**Nvars  # 2^N max attempts
    while attempts < max_attempts:
        satisfiable = True  
        for i in range(0, Nclauses):
            clause = Wff[i]
            clauseSat = False
            for literal in clause:
                index = abs(literal)
                val = Assignment[index]
                if literal > 0 and val == 1:
                    clauseSat = True
                    break
                elif literal < 0 and val == 0:
                    clauseSat = True
                    break
            if not clauseSat:
                satisfiable = False
                break
        if satisfiable:
            return True, Assignment
    # make small flips to generate more combinations
        flip = random.randint(1, Nvars)
        Assignment[flip] = 1 - Assignment[flip]
        attempts += 1
    return False, Assignment


#Num_Vars = 4
#Num_Clauses = 5
#wff = [[1, -2, 3], [-1, 2, -3], [1, 2, -4], [-1, 3, 4], [2, -3, 4]]

#wff = [[1], [-1]]
#Num_Vars = 1
#Num_Clauses = 2
# Run the incremental SAT solver


def build_wff(Nvars,Nclauses,LitsPerClause):
    wff=[]
    for i in range(1,Nclauses+1):
        clause=[]
        for j in range(1,LitsPerClause+1):
            var=random.randint(1,Nvars)
            if random.randint(0,1)==0: var=-var
            clause.append(var)
        wff.append(clause)
    return wff

def test_cases(num):
    if num == 1:
        # Test Case 1: (x1 OR NOT x2) AND (NOT x1 OR x2)
        # Expected: Satisfiable, e.g., x1 = True, x2 = True
        wff = [[1, -2], [-1, 2]]
        Nvars = 2
        Nclauses = 2
        return wff, Nvars, Nclauses
    elif num == 2:
        # Test Case 2: (x1 OR x2) AND (NOT x1 OR x2) AND (x1 OR NOT x2)
        # Expected: Satisfiable
        wff = [[1, 2], [-1, 2], [1, -2]]
        Nvars = 2
        Nclauses = 3
        return wff, Nvars, Nclauses
    elif num == 3:
        # Test Case 3: (x1 OR x2 OR x3) AND (NOT x1 OR NOT x2) AND (x2 OR NOT x3) AND (x1 OR x2)
        # Expected: Satisfiable
        wff = [[1, 2, 3], [-1, -2], [2, -3], [1,2]]
        Nvars = 3
        Nclauses = 3
        return wff, Nvars, Nclauses
    elif num == 4:
        # Test Case 4: (x1 OR x2) AND (x1 OR NOT x2) AND (x2 OR x3) AND (NOT x1 OR x3) AND (NOT x3 OR NOT x2)
        # Expected: Satisfiable 
        wff = [[1, 2], [1, -2], [2, 3], [-1, 3], [-3, -2]]
        Nvars = 3
        Nclauses = 5
        return wff, Nvars, Nclauses
    elif num == 5:
        wff = [[1], [-1]]
        Nvars = 1
        Nclauses = 2
        return wff, Nvars, Nclauses


def test_wff(num):
    wff, Nvars, Nclauses = test_cases(num)
    Assignment = [random.randint(0, 1) for x in range(Nvars + 1)]
    #Assignment=list((0 for x in range(Nvars+2)))
    #start = time.time() # Start timer
    SatFlag, Assignment2=incremental(wff,Nvars, Nclauses, Assignment)
    #SatFlag=check(wff,Nvars,Nclauses,Assignment)
    #end = time.time() # End timer
    #exec_time=int((end-start)*1e6)
    #return [wff,Assignment,SatFlag,exec_time]
    print(f"Test Case {num}:")
    print(f"SAT Result: {'Satisfiable' if SatFlag else 'Unsatisfiable'}")
    print(f"Assignment: {Assignment2[1:Nvars+1]}")
    #print(f"Execution Time: {exec_time}\n")

def run_cases():
    start = time.time() # Start timer
    for num in range(1, 6): 
        test_wff(num)
    end = time.time() # End timer
    exec_time=int((end-start)*1e6)
    print(f"Execution Time f: {exec_time}")

run_cases()


'''
print("SAT Result: ", result[2])
print("Assignment: ", result[1])
print("Execution Time: ", result[3])




def run_cases(TestCases,ProbNum,resultsfile,tracefile,cnffile):
    # TestCases: list of 4tuples describing problem
    #   0: Nvars = number of variables
    #   1: NClauses = number of clauses
    #   2: LitsPerClause = Literals per clause
    #   3: Ntrials = number of trials
    # ProbNum: Starting nunber to be given to 1st output run
    # resultsfile: path to file to hold output
    # tracefile: path to file to hold output
    # cnffile: path to file to hold output
    # For each randomly built wff, print out the following list
    #   Problem Number
    #   Number of variables
    #   Number of clauses
    #   Literals per clause
    #   Result: S or U for satisfiable or unsatisfiable
    #   A "1"
    #   Execution time
    #   If satisfiable, a binary string of assignments
    if not(ShowAnswer):
        print("S/U will NOT be shown on cnf file")
# Each case = Nvars,NClauses,LitsPerClause,Ntrials
    f1=open(resultsfile+".csv",'w')
    f2=open(tracefile+".csv",'w')
    f3=open(cnffile+".cnf","w")
    #initialize counters for final line of output
    Nwffs=0
    Nsat=0
    Nunsat=0
#    f1.write('ProbNum,Nvars,NClauses,LitsPerClause,Result,ExecTime(us)\n')
    for i in range(0,len(TestCases)):
        TestCase=TestCases[i]
        Nvars=TestCase[0]
        NClauses=TestCase[1]
        LitsPerClause=TestCase[2]
        Ntrials=TestCase[3]
        #Now run the number of trials for this wff configuration
        Scount=Ucount=0
        AveStime=AveUtime=0
        MaxStime=MaxUtime=0
        for j in range(0,Ntrials):
            #generate next trial case for this configuration
            Nwffs=Nwffs+1
            random.seed(ProbNum)
            wff = build_wff(Nvars,NClauses,LitsPerClause)
            results=test_wff(wff,Nvars,NClauses)
            wff=results[0]
            Assignment=results[1]
            Exec_Time=results[3]
            if results[2]:
                y='S'
                Scount=Scount+1
                AveStime=AveStime+Exec_Time
                MaxStime=max(MaxStime,Exec_Time)
                Nsat=Nsat+1
            else:
                y='U'
                Ucount=Ucount+1
                AveUtime=AveUtime+Exec_Time
                MaxUtime=max(MaxUtime,Exec_Time)
                Nunsat=Nunsat+1
            x=str(ProbNum)+','+str(Nvars)+','+str(NClauses)+','+str(LitsPerClause)
            x=x+str(NClauses*LitsPerClause)+','+y+',1,'+str(Exec_Time)
            if results[2]:
                for k in range(1,Nvars+1):
                    x=x+','+str(Assignment[k])
            print(x)
            f1.write(x+'\n')
            f2.write(x+'\n')
            #Add wff to cnf file
            if not(ShowAnswer):
                y='?'
            x="c "+str(ProbNum)+" "+str(LitsPerClause)+" "+y+"\n"
            f3.write(x)
            x="p cnf "+str(Nvars)+" "+str(NClauses)+"\n"
            f3.write(x)
            for i in range(0,len(wff)):
                clause=wff[i]
                x=""
                for j in range(0,len(clause)):
                    x=x+str(clause[j])+","
                x=x+"0\n"
                f3.write(x)
            #Increment problem number for next iteration
            ProbNum=ProbNum+1
        counts='# Satisfied = '+str(Scount)+'. # Unsatisfied = '+str(Ucount)
        maxs='Max Sat Time = '+str(MaxStime)+'. Max Unsat Time = '+str(MaxUtime)
        aves='Ave Sat Time = '+str(AveStime/Ntrials)+'. Ave UnSat Time = '+str(AveUtime/Ntrials)
        print(counts)
        print(maxs)
        print(aves)
        f2.write(counts+'\n')
        f2.write(maxs+'\n')
        f2.write(aves+'\n')
    x=cnffile+",TheBoss,"+str(Nwffs)+","+str(Nsat)+","+str(Nunsat)+","+str(Nwffs)+","+str(Nwffs)+"\n"
    f1.write(x)
    f1.close()
    f2.close()
    f3.close()

# Following generates several hundred test cases of 10 different wffs at each size
# and from 4 to 22 variables, 10 to 240 clauses, and 2 to 10 literals per clause 
TestCases=[
    [4,10,2,10],
    [8,16,2,10],
    [12,24,2,10],
    [16,32,2,10],
    [20,40,2,10],
    [24,48,2,10],
    [28,56,2,10]]

TC2=[
    [4,10,2,10],
    [8,16,2,10],
    [12,24,2,10]]

# Following generates a bunch of 2 literal wffs
SAT2=[
    [4,9,2,10],
    [8,18,2,10],
    [12,20,2,10],
    [16,30,2,10],
    [18,32,2,10],
    [20,33,2,10],
    [22,38,2,10],
    [24,43,2,10],
    [26,45,2,10],
    [28,47,2,10]
    ]


trace=True
ShowAnswer=True # If true, record evaluation result in header of each wff in cnffile
ProbNum = 3
resultsfile = r'ISresultsfile'
tracefile = r'IStracefile'
cnffile = r'IScnffile'# Each of these list entries describes a series of random wffs to generate

#run_cases(TC2,ProbNum,resultsfile,tracefile,cnffile)
#run_cases(SAT2,ProbNum,resultsfile,tracefile,cnffile)
run_cases(TestCases,ProbNum,resultsfile,tracefile,cnffile) # This takes a Looong Time!! 40  minutes
'''
