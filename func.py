import math

class Function:
    def __init__(self, string):
         self.eq=string
    
    def perform(self, num):
        return individual_perform(self.eq)(num)
        
disconts=[]
nondifferens=[]
            

def individual_perform(equ):
    if all_in_paren(equ):
        return individual_perform(equ[1:-1])
    elif int_checker(equ)==True:
        def ans(x):
            return eval(equ)
    elif find_loci(equ, '+')!=False:
        sym_loci=find_loci(equ,'+')
        pre= equ[:sym_loci]
        post= equ[sym_loci+1:]
        def ans(x):
            return individual_perform(pre)(x)+individual_perform(post)(x)
    elif find_loci(equ, '-')!=False:
        sym_loci=find_loci(equ,'-')
        pre= equ[:sym_loci]
        post= equ[sym_loci+1:]
        def ans(x):
            return individual_perform(pre)(x)-individual_perform(post)(x)
    elif find_loci(equ, '*')!=False:
        sym_loci=find_loci(equ,'*')
        pre= equ[:sym_loci]
        post= equ[sym_loci+1:]
        def ans(x):
            return individual_perform(pre)(x)*individual_perform(post)(x)
    elif find_loci(equ, '/')!=False:
        sym_loci=find_loci(equ,'/')
        pre= equ[:sym_loci]
        post= equ[sym_loci+1:]
        def ans(x):
            bottom=individual_perform(post)(x)
            if bottom==0:
                disconts.append(x)
                print('Discontinuity found: x =',x)
                return 0.0
            else:
                return individual_perform(pre)(x)/bottom
    elif find_loci(equ,'^')!=False:
        sym_loci=find_loci(equ, '^')
        pre= equ[:sym_loci]
        post= equ[sym_loci+1:]
        def ans(x):
            return individual_perform(pre)(x)**individual_perform(post)(x)
    elif equ[:3]=='sin':
        contents=equ[3:]
        def ans(x):
            return math.sin(individual_perform(contents)(x))
    elif equ[:3]=='cos':
        contents=equ[3:]
        def ans(x):
            return math.cos(individual_perform(contents)(x))
    elif equ[:3]=='tan':
        contents=equ[3:]
        def ans(x):
            if near_zero(math.cos(individual_perform(contents)(x)),2.5):
                disconts.append(x)
                print('Discontinuity found: x =',x)
                return 0.0
            return math.tan(individual_perform(contents)(x))
    elif equ[:3]=='csc':
        contents=equ[3:]
        def ans(x):
            if near_zero(math.sin(individual_perform(contents)(x)),2.5):
                disconts.append(x)
                print('Discontinuity found: x =',x)
                return 0.0
            return 1/math.sin(individual_perform(contents)(x))
    elif equ[:3]=='sec':
        contents=equ[3:]
        def ans(x):
            if near_zero(math.cos(individual_perform(contents)(x)),2.5):
                disconts.append(x)
                print('Discontinuity found: x =',x)
                return 0.0
            return 1/math.cos(individual_perform(contents)(x))
    elif equ[:3]=='cot':
        contents=equ[3:]
        def ans(x):
            if near_zero(math.sin(individual_perform(contents)(x)),2.5):
                disconts.append(x)
                print('Discontinuity found: x =',x)
                return 0.0
            return 1/math.tan(individual_perform(contents)(x))
    elif equ[:3]=='log':
        end=find_loci(equ,'_')
        base=equ[3:end]
        contents=equ[end+1:]
        def ans(x):
            if (individual_perform(contents)(x))<0:
                disconts.append(x)
                print('Discontinuity found: x =', x)
                return 0.0
            else:
                return math.log(individual_perform(contents)(x))/math.log(individual_perform(base)(x))
    elif equ=='e':
        def ans(x):
            return math.e
    elif equ=='pi':
        def ans(x):
            return math.pi
    elif equ[:4]=='asin':
        contents=equ[4:]
        def ans(x):
            if (individual_perform(contents)(x))<(math.pi/(-2)) or (individual_perform(contents)(x))>(math.pi/2):
                disconts.append(x)
                print('Discontinuity found: x =', x)
                return 0.0
            return math.asin(individual_perform(contents)(x))
    elif equ[:4]=='acos':
        contents=equ[4:]
        def ans(x):
            if (individual_perform(contents)(x))<0 or (individual_perform(contents)(x))>math.pi:
                disconts.append(x)
                print('Discontinuity found: x =', x)
                return 0.0
            return math.acos(individual_perform(contents)(x))
    elif equ[:4]=='atan':
        contents=equ[4:]
        def ans(x):
            return math.atan(individual_perform(contents)(x))
    elif equ[:4]=='acsc':
        contents=equ[4:]
        def ans(x):
            if (individual_perform(contents)(x))>(math.pi/(-2)) and (individual_perform(contents)(x))<(math.pi/2):
                disconts.append(x)
                print('Discontinuity found: x =', x)
                return 0.0
            return 1/math.asin(individual_perform(contents)(x))
    elif equ[:4]=='asec':
        contents=equ[4:]
        def ans(x):
            if (individual_perform(contents)(x))>0 and (individual_perform(contents)(x))<math.pi:
                disconts.append(x)
                print('Discontinuity found: x =', x)
                return 0.0
            return 1/math.acos(individual_perform(contents)(x))
    elif equ[:4]=='acot':
        contents=equ[4:]
        def ans(x):
            return 1/math.atan(individual_perform(contents)(x))
    else:
        def ans(x):
            return x
    return ans

def individual_deriv(equ):
    if all_in_paren(equ):
        return individual_deriv(equ[1:-1])
    elif int_checker(equ)==True or not('x' in set(equ)):
        def ans(x):
            return 0.0
    elif find_loci(equ, '+')!=False:
        sym_loci=find_loci(equ,'+')
        pre= equ[:sym_loci]
        post= equ[sym_loci+1:]
        def ans(x):
            return individual_deriv(pre)(x)+individual_deriv(post)(x)
    elif find_loci(equ, '-')!=False:
        sym_loci=find_loci(equ,'-')
        pre= equ[:sym_loci]
        post= equ[sym_loci+1:]
        def ans(x):
            return individual_deriv(pre)(x)-individual_deriv(post)(x)
    elif find_loci(equ, '*')!=False:
        sym_loci=find_loci(equ,'*')
        pre= equ[:sym_loci]
        post= equ[sym_loci+1:]
        def ans(x):
            return (individual_perform(pre)(x)*individual_deriv(post)(x))+(individual_deriv(pre)(x)*individual_perform(post)(x))
    elif find_loci(equ, '/')!=False:
        sym_loci=find_loci(equ,'/')
        pre= equ[:sym_loci]
        post= equ[sym_loci+1:]
        def ans(x):
            bottom= (individual_perform(post)(x))**2
            if bottom==0:
                nondifferens.append(x)
                print('Nondifferentiability found: x =',x)
                return 0.0
            return ((individual_perform(post)(x)*individual_deriv(pre)(x))-(individual_deriv(post)(x)*individual_perform(pre)(x)))/bottom
    elif find_loci(equ,'^')!=False:
        sym_loci=find_loci(equ, '^')
        pre= equ[:sym_loci]
        post= equ[sym_loci+1:]
        if not('x' in set(post)):
            def ans(x):
                if (individual_perform(post)(x)-1)<0 and individual_perform(pre)(x)==0:
                    nondifferens.append(x)
                    print('Nondifferentiability found: x =',x)
                    return 0.0
                return individual_perform(post)(x)*individual_perform(pre)(x)**(individual_perform(post)(x)-1)
        else:
            def ans(x):
                if (individual_perform(post)(x)-1)<0 and individual_perform(pre)(x)==0:
                    nondifferens.append(x)
                    print('Nondifferentiability found: x =',x)
                    return 0.0
                return math.log(individual_perform(pre)(x))*individual_deriv(post)(x)*individual_perform(post)(x)*individual_perform(pre)(x)**(individual_perform(post)(x)-1)
    elif equ[:3]=='sin':
        contents=equ[3:]
        if not('x' in set(contents)):
            def ans(x):
                return math.cos(individual_perform(contents)(x))
        else:
            def ans(x):
                return individual_deriv(contents)(x)*math.cos(individual_perform(contents)(x))
    elif equ[:3]=='cos':
        contents=equ[3:]
        if not('x' in set(contents)):
            def ans(x):
                return -1*math.sin(individual_perform(contents)(x))
        else:
            def ans(x):
                return individual_deriv(contents)(x)*-1*math.sin(individual_perform(contents)(x))
    elif equ[:3]=='tan':
        contents=equ[3:]
        if not('x' in set(contents)):
            def ans(x):
                if math.cos(individual_perform(contents)(x))==0:
                    nondifferens.append(x)
                    print('Nondifferentiability found: x =',x)
                    return 0.0
                return 1/((math.cos(individual_perform(contents)(x)))**2)
        else:
            def ans(x):
                if math.cos(individual_perform(contents)(x))==0:
                    nondifferens.append(x)
                    print('Nondifferentiability found: x =',x)
                    return 0.0
                return individual_deriv(contents)(x)*1/((math.cos(individual_perform(contents)(x)))**2)
    elif equ[:3]=='csc':
        contents=equ[3:]
        if not('x' in set(contents)):
            def ans(x):
                if math.sin(individual_perform(contents)(x))==0:
                    nondifferens.append(x)
                    print('Nondifferentiability found: x =',x)
                    return 0.0
                return (-1)*(math.cos(individual_perform(contents)(x)))*(1/math.sin(individual_perform(contents)(x))**2)
        else:
            def ans(x):
                if math.sin(individual_perform(contents)(x))==0:
                    nondifferens.append(x)
                    print('Nondifferentiability found: x =',x)
                    return 0.0
                return individual_deriv(contents)(x)*(-1)*(math.cos(individual_perform(contents)(x)))*(1/math.sin(individual_perform(contents)(x))**2)
    elif equ[:3]=='sec':
        contents=equ[3:]
        if not('x' in set(contents)):
            def ans(x):
                if math.cos(individual_perform(contents)(x))==0:
                    nondifferens.append(x)
                    print('Nondifferentiability found: x =',x)
                    return 0.0
                return (math.sin(individual_perform(contents)(x)))*(1/math.cos(individual_perform(contents)(x))**2)
        else:
            def ans(x):
                if math.cos(individual_perform(contents)(x))==0:
                    nondifferens.append(x)
                    print('Nondifferentiability found: x =',x)
                    return 0.0
                return individual_deriv(contents)(x)*(math.sin(individual_perform(contents)(x)))*(1/math.cos(individual_perform(contents)(x))**2)
    elif equ[:3]=='cot':
        contents=equ[3:]
        if not('x' in set(contents)):
            def ans(x):
                if math.sin(individual_perform(contents)(x))==0:
                    nondifferens.append(x)
                    print('Nondifferentiability found: x =',x)
                    return 0.0
                return (-1)*(1/math.sin(individual_perform(contents)(x))**2)
        else:
            def ans(x):
                if math.sin(individual_perform(contents)(x))==0:
                    nondifferens.append(x)
                    print('Nondifferentiability found: x =',x)
                    return 0.0
                return individual_deriv(contents)(x)*(-1)*(1/math.sin(individual_perform(contents)(x))**2)
    elif equ[:3]=='log':
        end=find_loci(equ,'_')
        base=equ[3:end]
        contents=equ[end+1:]
        if 'x' in set(contents):
            def ans(x):
                return individual_deriv(contents)(x)*1/(individual_perform(contents)(x)*math.log(individual_perform(base)(x)))
        else:
            def ans(x):
                return 1/(individual_perform(contents)(x)*math.log(individual_perform(base)(x)))
    elif equ[:4]=='asin':
        contents=equ[4:]
        if 'x' in set(contents):
            def ans(x):
                if individual_peform(contents)(x)==1:
                    nondifferens.append(x)
                    print('Nondifferentiability found: x =',x)
                    return 0.0
                return individual_deriv(contents)(x)*1/math.sqrt(1-(individual_perform(contents)(x))**2)
        else:
            def ans(x):
                if individual_peform(contents)(x)==1:
                    nondifferens.append(x)
                    print('Nondifferentiability found: x =',x)
                    return 0.0
                return 1/math.sqrt(1-(individual_perform(contents)(x))**2)
    elif equ[:4]=='acos':
        contents=equ[4:]
        if 'x' in set(contents):
            def ans(x):
                if individual_peform(contents)(x)==1:
                    nondifferens.append(x)
                    print('Nondifferentiability found: x =',x)
                    return 0.0
                return individual_deriv(contents)(x)*(-1)/math.sqrt(1-(individual_perform(contents)(x))**2)
        else:
            def ans(x):
                if individual_peform(contents)(x)==1:
                    nondifferens.append(x)
                    print('Nondifferentiability found: x =',x)
                    return 0.0
                return (-1)/math.sqrt(1-(individual_perform(contents)(x))**2)
    elif equ[:4]=='atan':
        contents=equ[4:]
        if 'x' in set(contents):
            def ans(x):
                return individual_deriv(contents)(x)*1/((individual_perform(contents)(x))**2+1)
        else:
            def ans(x):
                1/((individual_perform(contents)(x))**2+1)
    elif equ[:4]=='acsc':
        contents=equ[4:]
        if 'x' in set(contents):
            def ans(x):
                if individual_peform(contents)(x)==1 or individual_peform(contents)(x)==-1:
                    nondifferens.append(x)
                    print('Nondifferentiability found: x =',x)
                    return 0.0
                return individual_deriv(contents)(x)*(-1)/(math.fabs(individual_perform(contents)(x))*math.sqrt((individual_perform(contents)(x))**2-1))
        else:
            def ans(x):
                if individual_peform(contents)(x)==1 or individual_peform(contents)(x)==-1:
                    nondifferens.append(x)
                    print('Nondifferentiability found: x =',x)
                    return 0.0
                return (-1)/(math.fabs(individual_perform(contents)(x))*math.sqrt((individual_perform(contents)(x))**2-1))
    elif equ[:4]=='asec':
        contents=equ[4:]
        if 'x' in set(contents):
            def ans(x):
                if individual_peform(contents)(x)==1 or individual_peform(contents)(x)==-1:
                    nondifferens.append(x)
                    print('Nondifferentiability found: x =',x)
                    return 0.0
                return individual_deriv(contents)(x)*1/(math.fabs(individual_perform(contents)(x))*math.sqrt((individual_perform(contents)(x))**2-1))
        else:
            def ans(x):
                if individual_peform(contents)(x)==1 or individual_peform(contents)(x)==-1:
                    nondifferens.append(x)
                    print('Nondifferentiability found: x =',x)
                    return 0.0
                return 1/(math.fabs(individual_perform(contents)(x))*math.sqrt((individual_perform(contents)(x))**2-1))
    elif equ[:4]=='acot':
        contents=equ[4:]
        if 'x' in set(contents):
            def ans(x):
                return individual_deriv(contents)(x)*(-1)/((individual_perform(contents)(x))**2+1)
        else:
            def ans(x):
                (-1)/((individual_perform(contents)(x))**2+1)
    else:
        def ans(x):
            return x
    return ans

def filter(inp, bads):
    ans=''
    for x in inp:
        for y in bads:
            if x!=y:
                ans+=x
    return ans
def int_checker(string):
    ans=True
    for x in string:
        if not(x in set(['1','2','3','4','5','6','7','8','9','0','.',',','-'])):
            ans=False
    return ans
def find_loci(string, sym):
    paren=0
    for x in range(len(string)):
        if string[x]==sym and paren<1:
            return x
        elif string[x]=='(':
            paren+=1
        elif string[x]==')':
            paren-=1
    return False
def all_in_paren(string):
    if string[0]=='(' and string[-1]==')' and not('(' in set(string[1:-1]) or '(' in set(string[1:-1])):
        return True
    else:
        return False
def near_zero(num, sensitivity):
    if num>-1.0*10**(-sensitivity) and num<1.0*10**(-sensitivity):
        return True
    else:
        return False

'''def complex_func_reader(string):
    pieces=[]
    split_loci=[-1]
    inside_paren=0
    for x in range(len(string)):
        if string[x]=='+' and inside_paren<1:
            split_loci.append(x)
        elif string[x]=='(':
            inside_paren+=1
        elif string[x]==')':
            inside_paren-=1
    split_loci.append(len(string))
    for x in range(len(split_loci)-1):
        piece=string[split_loci[x]+1:split_loci[x+1]]
        pieces.append(piece)
    return pieces'''
    
def NUMERICALderiv(func, num):
    first= func(num+0.00000000001)
    second= func(num-0.00000000001)
    return (first-second)/0.00000000002
    
    
func_str = input ("Input the function: ")
func_str=filter(func_str, [' '])
interval_str = input("Input closed interval in format [a,b]: ")
interval_str=filter(interval_str, [' '])
first, comma, final = (find_loci(interval_str, '['), find_loci(interval_str, ','), find_loci(interval_str, ']'))
interval_start=eval(interval_str[first+1:comma])
interval_end=eval(interval_str[comma+1:final])
steps_str = input("Input numerical specificity (number of steps the program will take across the interval): ")
steps=eval(steps_str)

progression_dist = (interval_end-interval_start)/(steps)
included_values=[]
for x in range(steps):
    step=round(interval_start+progression_dist*x,8)
    included_values.append(step)
included_values.append(interval_end)

func_1=Function(func_str)
deriv_1=individual_deriv(func_str)

values={}
inc_dec={}
cup_frown={}
for x in included_values:
    a, b = (func_1.perform(x), deriv_1(x))
    c= NUMERICALderiv (deriv_1, x)
    values[x]=(a,b,c)

for x in included_values[:-1]:
    next=round(x+progression_dist,8)
    if (values[x][1]>0 and values[next][1]<0):
        inc_dec[x+progression_dist/2]='locMAX'
    elif (values[x][1]==0 and values[next][1]<0 and deriv_1(x-0.01)>0):
        inc_dec[x]='locMAX'
    elif (x==interval_start and values[next][0]<values[x][0]):
        inc_dec[interval_start]='locMAX'
    elif (x==interval_end-progression_dist and values[next][0]>values[x][0]):
        inc_dec[interval_end]='locMAX'
    elif (values[x][1]<0 and values[next][1]>0):
        inc_dec[x+progression_dist/2]='locMIN'
    elif (values[x][1]==0 and values[next][1]>0 and deriv_1(x-0.01)<0):
        inc_dec[x]='locMIN'
    elif (x==interval_start and values[next][0]>values[x][0]):
        inc_dec[interval_start]='locMIN'
    elif (x==interval_end-progression_dist and values[next][0]<values[x][0]):
        inc_dec[interval_end]='locMIN'
        
    if (values[x][2]>0 and values[next][2]<0):
        cup_frown[x+progression_dist/2]='INF_pn'
    elif (values[x][2]==0 and values[next][2]<0 and NUMERCIALderiv(deriv_1(x-0.01)>0)):
        cup_frown[x]='INF_pn'
    elif (x==interval_start and values[x][2]>0):
        cup_frown[interval_start]='END_p'
    elif (x==interval_end-progression_dist and values[next][2]>0):
        cup_frown[interval_end]='END_p'
    elif (values[x][2]<0 and values[next][2]>0):
        cup_frown[x+progression_dist/2]='INF_np'
    elif (values[x][2]==0 and values[next][2]>0 and deriv_1(x-0.01)<0):
        cup_frown[x]='INF_np'
    elif (x==interval_start and values[x][2]<0):
        cup_frown[interval_start]='END_n'
    elif (x==interval_end-progression_dist and values[next][2]<0):
        cup_frown[interval_end]='END_n'

inc_dec_details={}
for x in inc_dec:
    inc_dec_details[x]=func_1.perform(x)
for x in included_values:
    inc_dec_details[x]=func_1.perform(x)
abs_max=inc_dec_details[max(inc_dec_details,key=inc_dec_details.get)]
abs_min=inc_dec_details[min(inc_dec_details,key=inc_dec_details.get)]

for x in inc_dec:
    if func_1.perform(x)==abs_max:
        inc_dec[x]='absMAX'
    elif func_1.perform(x)==abs_min:
        inc_dec[x]='absMIN'

intervals={}
INCstart=None
DECstart=None
INCend=None
DECend=None

print(inc_dec)

for x in sorted(inc_dec):
    if inc_dec[x][3:]=='MIN':
        INCstart=x
        DECend=x
        if DECstart!=None:
            intervals[(DECstart,DECend)]='Dec'
            DECstart=None
    elif inc_dec[x][3:]=='MAX':
        INCend=x
        DECstart=x
        if INCstart!=None:
            intervals[(INCstart,INCend)]='Inc'
            INCstart=None

for x in intervals:
    if x[0] in set(disconts) and x[1] in set(disconts):
        intervals[x]+='_open'
    elif x[0] in set(disconts) and not(x[1] in set(disconts)):
        intervals[x]+='_Rend'
    elif not(x[0] in set(disconts) or x[1] in set(disconts)):
        intervals[x]+='_clos'
    else:
        intervals[x]+='_Lend'
        
print(intervals)

print('Discontinuous at x =',disconts)
print('Nondifferentiable at x =',nondifferens)

print('')
print(values)
