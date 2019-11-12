import math

class Function:
    def __init__(self, pieces):
         self.pieces=pieces
    
    def perform(self, num):
        parts=[]
        for x in self.pieces:
            check_for_mult = []
            check_for_div = []
            for y in range(len(x)):
                if x[y]=='*':
                    check_for_mult.append(y)
                elif x[y]=='/':
                    check_for_div.append(y)
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
    if int_checker(equ)==True:
        def ans(x):
            return eval(equ)
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
        if not(x in set(['1','2','3','4','5','6','7','8','9','0','.',','])):
            ans=False
    return ans

def complex_func_reader(string):
    pieces={}
    split_loci_pos=[-1]
    split_loci_neg=[]
    for x in range(len(string)):
        if string[x]=='+':
            split_loci_pos.append(x)
        elif string[x]=='-':
            split_loci_neg.append(x)
    split_loci=sorted(split_loci_pos+split_loci_neg)
    split_loci.append(len(string))
    for x in range(len(split_loci)-1):
        piece=string[split_loci[x]+1:split_loci[x+1]]
        if string[split_loci[x]]=='-':
            pieces[piece]='neg'
        else:
            pieces[piece]='pos'
    return pieces
    
#def first_derivative(func):
    
    
func_str = input ("Input the function: ")
func_str=filter(func_str, [' '])
interval_str = input("Input closed interval in format [a,b]: ")
interval_str=filter(interval_str, [' '])

p=(complex_func_reader(func_str))

func_1=Function(p)
print(func_1.perform(1))
