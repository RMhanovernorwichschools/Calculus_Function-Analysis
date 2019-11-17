import math

disconts=[]
nondifferens=[]

class Function:
    def __init__(self, string):
         self.eq=string
    
    def perform(self, num):
        return individual_perform(self.eq)(num)

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
            bottom= individual_perform(post)(x)
            top= individual_perform(pre)(x)
            if bottom==0:
                disconts.append(x)
                print('Discontinuity found: x =',x)
                if top==0:
                    return 0.
                else:
                    return 1000000.0
            else:
                return top/bottom
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
                return 1000000.0
            return math.tan(individual_perform(contents)(x))
    elif equ[:3]=='csc':
        contents=equ[3:]
        def ans(x):
            if near_zero(math.sin(individual_perform(contents)(x)),2.5):
                disconts.append(x)
                print('Discontinuity found: x =',x)
                return 1000000.0
            return 1/math.sin(individual_perform(contents)(x))
    elif equ[:3]=='sec':
        contents=equ[3:]
        def ans(x):
            if near_zero(math.cos(individual_perform(contents)(x)),2.5):
                disconts.append(x)
                print('Discontinuity found: x =',x)
                return 1000000.0
            return 1/math.cos(individual_perform(contents)(x))
    elif equ[:3]=='cot':
        contents=equ[3:]
        def ans(x):
            if near_zero(math.sin(individual_perform(contents)(x)),2.5):
                disconts.append(x)
                print('Discontinuity found: x =',x)
                return 1000000.0
            return 1/math.tan(individual_perform(contents)(x))
    elif equ[:3]=='log':
        end=find_loci(equ,'_')
        base=equ[3:end]
        contents=equ[end+1:]
        def ans(x):
            if (individual_perform(contents)(x))<0:
                disconts.append(x)
                print('Discontinuity found: x =', x)
                return 1000000.0
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
            top= ((individual_perform(post)(x)*individual_deriv(pre)(x))-(individual_deriv(post)(x)*individual_perform(pre)(x)))
            if bottom==0:
                nondifferens.append(x)
                print('Nondifferentiability found: x =',x)
                if top==0:
                    return 0
                else:
                    return 1000000.0
            return top/bottom
    elif find_loci(equ,'^')!=False:
        sym_loci=find_loci(equ, '^')
        pre= equ[:sym_loci]
        post= equ[sym_loci+1:]
        if not('x' in set(post)):
            def ans(x):
                if (individual_perform(post)(x)-1)<0 and individual_perform(pre)(x)==0:
                    nondifferens.append(x)
                    print('Nondifferentiability found: x =',x)
                    return 1000000.0
                return individual_perform(post)(x)*individual_perform(pre)(x)**(individual_perform(post)(x)-1)
        else:
            def ans(x):
                if (individual_perform(post)(x)-1)<0 and individual_perform(pre)(x)==0:
                    nondifferens.append(x)
                    print('Nondifferentiability found: x =',x)
                    return 1000000.0
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
                    return 1000000.0
                return 1/((math.cos(individual_perform(contents)(x)))**2)
        else:
            def ans(x):
                if math.cos(individual_perform(contents)(x))==0:
                    nondifferens.append(x)
                    print('Nondifferentiability found: x =',x)
                    return 1000000.0
                return individual_deriv(contents)(x)*1/((math.cos(individual_perform(contents)(x)))**2)
    elif equ[:3]=='csc':
        contents=equ[3:]
        if not('x' in set(contents)):
            def ans(x):
                if math.sin(individual_perform(contents)(x))==0:
                    nondifferens.append(x)
                    print('Nondifferentiability found: x =',x)
                    return 1000000.0
                return (-1)*(math.cos(individual_perform(contents)(x)))*(1/math.sin(individual_perform(contents)(x))**2)
        else:
            def ans(x):
                if math.sin(individual_perform(contents)(x))==0:
                    nondifferens.append(x)
                    print('Nondifferentiability found: x =',x)
                    return 1000000.0
                return individual_deriv(contents)(x)*(-1)*(math.cos(individual_perform(contents)(x)))*(1/math.sin(individual_perform(contents)(x))**2)
    elif equ[:3]=='sec':
        contents=equ[3:]
        if not('x' in set(contents)):
            def ans(x):
                if math.cos(individual_perform(contents)(x))==0:
                    nondifferens.append(x)
                    print('Nondifferentiability found: x =',x)
                    return 1000000.0
                return (math.sin(individual_perform(contents)(x)))*(1/math.cos(individual_perform(contents)(x))**2)
        else:
            def ans(x):
                if math.cos(individual_perform(contents)(x))==0:
                    nondifferens.append(x)
                    print('Nondifferentiability found: x =',x)
                    return 1000000.0
                return individual_deriv(contents)(x)*(math.sin(individual_perform(contents)(x)))*(1/math.cos(individual_perform(contents)(x))**2)
    elif equ[:3]=='cot':
        contents=equ[3:]
        if not('x' in set(contents)):
            def ans(x):
                if math.sin(individual_perform(contents)(x))==0:
                    nondifferens.append(x)
                    print('Nondifferentiability found: x =',x)
                    return 1000000.0
                return (-1)*(1/math.sin(individual_perform(contents)(x))**2)
        else:
            def ans(x):
                if math.sin(individual_perform(contents)(x))==0:
                    nondifferens.append(x)
                    print('Nondifferentiability found: x =',x)
                    return 1000000.0
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
                if individual_perform(contents)(x)==1:
                    nondifferens.append(x)
                    print('Nondifferentiability found: x =',x)
                    return 0.0
                return individual_deriv(contents)(x)*1/math.sqrt(1-(individual_perform(contents)(x))**2)
        else:
            def ans(x):
                if individual_perform(contents)(x)==1:
                    nondifferens.append(x)
                    print('Nondifferentiability found: x =',x)
                    return 0.0
                return 1/math.sqrt(1-(individual_perform(contents)(x))**2)
    elif equ[:4]=='acos':
        contents=equ[4:]
        if 'x' in set(contents):
            def ans(x):
                if individual_perform(contents)(x)==1:
                    nondifferens.append(x)
                    print('Nondifferentiability found: x =',x)
                    return 0.0
                return individual_deriv(contents)(x)*(-1)/math.sqrt(1-(individual_perform(contents)(x))**2)
        else:
            def ans(x):
                if individual_perform(contents)(x)==1:
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
                if individual_perform(contents)(x)==1 or individual_perform(contents)(x)==-1:
                    nondifferens.append(x)
                    print('Nondifferentiability found: x =',x)
                    return 0.0
                return individual_deriv(contents)(x)*(-1)/(math.fabs(individual_perform(contents)(x))*math.sqrt((individual_perform(contents)(x))**2-1))
        else:
            def ans(x):
                if individual_perform(contents)(x)==1 or individual_perform(contents)(x)==-1:
                    nondifferens.append(x)
                    print('Nondifferentiability found: x =',x)
                    return 0.0
                return (-1)/(math.fabs(individual_perform(contents)(x))*math.sqrt((individual_perform(contents)(x))**2-1))
    elif equ[:4]=='asec':
        contents=equ[4:]
        if 'x' in set(contents):
            def ans(x):
                if individual_perform(contents)(x)==1 or individual_perform(contents)(x)==-1:
                    nondifferens.append(x)
                    print('Nondifferentiability found: x =',x)
                    return 0.0
                return individual_deriv(contents)(x)*1/(math.fabs(individual_perform(contents)(x))*math.sqrt((individual_perform(contents)(x))**2-1))
        else:
            def ans(x):
                if individual_perform(contents)(x)==1 or individual_perform(contents)(x)==-1:
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
            return 1.0
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

def NUMERICALderiv(func, num):
    first= func(num+0.00000000001)
    second= func(num-0.00000000001)
    return (first-second)/0.00000000002
    
func_str = input ("     Input the function: ")
func_str=filter(func_str, [' '])
a_str = input("     Input x-value for tangent: ")
a_str=filter(a_str, [' '])
a_val=eval(a_str)

multer=individual_deriv(func_str)(a_val)
adder=individual_perform(func_str)(a_val)

print('')
N_multer=0
N_flag=False
T_flag=False
Ty_flag=False

if a_val in set(disconts):
    T_flag=True
elif a_val in set(nondifferens) and multer==1000000.0:
    Ty_flag=True

ans='N(x) = '
new_ans= 'T(x) = '

if multer!=0:
    N_multer=-1/multer
    ans+=str(N_multer)+'x '
    new_ans+=str(multer)+'x '
else:
    ans+='UNDEFINED'
    N_flag=True

adder_full = (-a_val)*multer
Nadder_full = (-a_val)*N_multer 

modi_full = adder_full + adder
Nmodi_full = Nadder_full + adder

if not(T_flag):
    if modi_full!=0:
        if new_ans=='T(x) = ':
            new_ans+=str(modi_full)
        else:
            if modi_full>0:
                new_ans+='+ '+str(modi_full)
            else:
                new_ans+='- '+str(abs(modi_full))
    else:
        if new_ans=='T(x) = ':
            new_ans+='0'
else:
    new_ans+=str(a_val)
        
if not(N_flag):
    if Nmodi_full!=0:
        if ans=='N(x) = ':
            ans+=str(Nmodi_full)
        else:
            if Nmodi_full>0:
                ans+='+ '+str(Nmodi_full)
            else:
                ans+='- '+str(abs(Nmodi_full))
    else:
        if ans=='N(x) = ':
            ans+='0'
else:
    ans='Normal line: x = '+str(adder)
    
if T_flag:
    new_ans='No Tangent at x = '+str(a_val)
    ans='No Normal at x = '+str(a_val)
elif Ty_flag:
    ans='N(x) = '+str(adder)
    new_ans = 'Tangent line: x = '+str(a_val)
print(new_ans)
print(ans)
