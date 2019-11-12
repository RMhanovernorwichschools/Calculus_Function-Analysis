import math

class Function:
    def __init__(self, pieces):
         self.pieces=pieces
    
    def perform(self, num):
        parts=[]
        for x in self.pieces:
            check_for_mult = []
            check_for_div = []
            check_paren=0
            for y in range(len(x)):
                if x[y]=='*' and check_paren<1:
                    check_for_mult.append(y)
                elif x[y]=='/' and check_paren<1:
                    check_for_div.append(y)
                elif x[y]=='(':
                    check_paren+=1
                elif x[y]==')':
                    check_paren-=1
            if check_for_mult==[] and check_for_div==[]:
                part=individual_perform(x)(num)
            elif check_for_mult!=[] and check_for_div==[]:
                sectors = x.split('*')
                p1=individual_perform(sectors[0])(num)
                for z in sectors[1:]:
                    p2=individual_perform(z)(num)
                    p1*=p2
                part=p1
            elif check_for_div!=[] and check_for_mult==[]:
                sectors = x.split('/')
                p1=individual_perform(sectors[0])(num)
                for z in sectors[1:]:
                    p2=individual_perform(z)(num)
                    p1/=p2
                part=p1
            parts.append(part)
        return sum(parts)

def individual_perform(equ):
    if all_in_paren(equ):
        return individual_perform(equ[1:-1])
    elif int_checker(equ)==True:
        def ans(x):
            return eval(equ)
    elif find_loci(equ, '+'):
        sym_loci=find_loci(equ,'+')
        pre= equ[:sym_loci]
        post= equ[sym_loci+1:]
        def ans(x):
            return individual_perform(pre)(x)+individual_perform(post)(x)
    elif find_loci(equ, '-'):
        sym_loci=find_loci(equ,'-')
        pre= equ[:sym_loci]
        post= equ[sym_loci+1:]
        def ans(x):
            return individual_perform(pre)(x)-individual_perform(post)(x)
    elif find_loci(equ, '*'):
        sym_loci=find_loci(equ,'*')
        pre= equ[:sym_loci]
        post= equ[sym_loci+1:]
        def ans(x):
            return individual_perform(pre)(x)*individual_perform(post)(x)
    elif find_loci(equ, '/'):
        sym_loci=find_loci(equ,'/')
        pre= equ[:sym_loci]
        post= equ[sym_loci+1:]
        def ans(x):
            return individual_perform(pre)(x)/individual_perform(post)(x)
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
        def ans(x):
            return math.log(x)/math.log(base)
    elif equ=='e':
        def ans(x):
            return math.e
    elif equ=='pi':
        def ans(x):
            return math.pi
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

func_1=Function([func_str])
print(func_1.perform(1))
