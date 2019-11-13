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
            return math.tan(individual_perform(contents)(x))
    elif equ[:3]=='csc':
        contents=equ[3:]
        def ans(x):
            return 1/math.sin(individual_perform(contents)(x))
    elif equ[:3]=='sec':
        contents=equ[3:]
        def ans(x):
            return 1/math.cos(individual_perform(contents)(x))
    elif equ[:3]=='cot':
        contents=equ[3:]
        def ans(x):
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
    elif equ[:3]=='asin':
        contents=equ[3:]
        def ans(x):
            if (individual_perform(contents)(x))<(math.pi/(-2)) or (individual_perform(contents)(x))>(math.pi/2):
                disconts.append(x)
                print('Discontinuity found: x =', x)
                return 0.0
            return math.asin(individual_perform(contents)(x))
    elif equ[:3]=='acos':
        contents=equ[3:]
        def ans(x):
            if (individual_perform(contents)(x))<0 or (individual_perform(contents)(x))>math.pi:
                disconts.append(x)
                print('Discontinuity found: x =', x)
                return 0.0
            return math.acos(individual_perform(contents)(x))
    elif equ[:3]=='atan':
        contents=equ[3:]
        def ans(x):
            return math.atan(individual_perform(contents)(x))
    elif equ[:3]=='acsc':
        contents=equ[3:]
        def ans(x):
            if (individual_perform(contents)(x))>(math.pi/(-2)) and (individual_perform(contents)(x))<(math.pi/2):
                disconts.append(x)
                print('Discontinuity found: x =', x)
                return 0.0
            return 1/math.asin(individual_perform(contents)(x))
    elif equ[:3]=='asec':
        contents=equ[3:]
        def ans(x):
            if (individual_perform(contents)(x))>0 and (individual_perform(contents)(x))<math.pi:
                disconts.append(x)
                print('Discontinuity found: x =', x)
                return 0.0
            return 1/math.acos(individual_perform(contents)(x))
    elif equ[:3]=='acot':
        contents=equ[3:]
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
            return ((individual_perform(post)(x)*individual_deriv(pre)(x))-(individual_deriv(post)(x)*individual_perform(pre)(x)))/((individual_perform(post)(x))**2)
    elif find_loci(equ,'^')!=False:
        sym_loci=find_loci(equ, '^')
        pre= equ[:sym_loci]
        post= equ[sym_loci+1:]
        if not('x' in set(post)):
            def ans(x):
                return individual_perform(post)(x)*individual_perform(pre)(x)**(individual_perform(post)(x)-1)
        else:
            def ans(x):
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
                return 1/((math.cos(individual_perform(contents)(x)))**2)
        else:
            def ans(x):
                return individual_deriv(contents)(x)*1/((math.cos(individual_perform(contents)(x)))**2)
    elif equ[:3]=='csc':
        contents=equ[3:]
        if not('x' in set(contents)):
            def ans(x):
                return (-1)*(math.cos(individual_perform(contents)(x)))*(1/math.sin(individual_perform(contents)(x))**2)
        else:
            def ans(x):
                return individual_deriv(contents)(x)*(-1)*(math.cos(individual_perform(contents)(x)))*(1/math.sin(individual_perform(contents)(x))**2)
    elif equ[:3]=='sec':
        contents=equ[3:]
        if not('x' in set(contents)):
            def ans(x):
                return (math.sin(individual_perform(contents)(x)))*(1/math.cos(individual_perform(contents)(x))**2)
        else:
            def ans(x):
                return individual_deriv(contents)(x)*(math.sin(individual_perform(contents)(x)))*(1/math.cos(individual_perform(contents)(x))**2)
    elif equ[:3]=='cot':
        contents=equ[3:]
        if not('x' in set(contents)):
            def ans(x):
                return (-1)*(1/math.sin(individual_perform(contents)(x))**2)
        else:
            def ans(x):
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
        contents=equ[3:]
        if 'x' in set(contents):
            def ans(x):
                return individual_deriv(contents)(x)*1/math.sqrt(1-(individual_perform(contents)(x))**2)
        else:
            def ans(x):
                return 1/math.sqrt(1-(individual_perform(contents)(x))**2)
    elif equ[:4]=='acos':
        contents=equ[3:]
        if 'x' in set(contents):
            def ans(x):
                return individual_deriv(contents)(x)*(-1)/math.sqrt(1-(individual_perform(contents)(x))**2)
        else:
            def ans(x):
                return (-1)/math.sqrt(1-(individual_perform(contents)(x))**2)
    elif equ[:4]=='atan':
        contents=equ[3:]
        if 'x' in set(contents):
            def ans(x):
                return individual_deriv(contents)(x)*1/((individual_perform(contents)(x))**2+1)
        else:
            def ans(x):
                1/((individual_perform(contents)(x))**2+1)
    elif equ[:4]=='acsc':
        contents=equ[3:]
        if 'x' in set(contents):
            def ans(x):
                return individual_deriv(contents)(x)*(-1)/(math.fabs(individual_perform(contents)(x))*math.sqrt((individual_perform(contents)(x))**2-1))
        else:
            def ans(x):
                return (-1)/(math.fabs(individual_perform(contents)(x))*math.sqrt((individual_perform(contents)(x))**2-1))
    elif equ[:4]=='asec':
        contents=equ[3:]
        if 'x' in set(contents):
            def ans(x):
                return individual_deriv(contents)(x)*1/(math.fabs(individual_perform(contents)(x))*math.sqrt((individual_perform(contents)(x))**2-1))
        else:
            def ans(x):
                return 1/(math.fabs(individual_perform(contents)(x))*math.sqrt((individual_perform(contents)(x))**2-1))
    elif equ[:4]=='acot':
        contents=equ[3:]
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
    
#def first_derivative(func):
    
    
func_str = input ("Input the function: ")
func_str=filter(func_str, [' '])
interval_str = input("Input closed interval in format [a,b]: ")
interval_str=filter(interval_str, [' '])

func_1=Function(func_str)
print(func_1.perform(1))
print(individual_deriv(func_str)(1))
