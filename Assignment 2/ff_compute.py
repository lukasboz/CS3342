# Written by: Lukas Bozinov
# Date: 2024-10-27
# Professor: Lucian Ilie

from collections import defaultdict
import sys 

def main(): 

    grammar = processG()
    print("proc'd g: ", grammar) 

    totalfirst = defaultdict(set)
    eps = {}
    first = {}

    def epsAndFirst(g):
        
        for token in g:#every elem in g
            for prod in g.get(token, []): #every rhs prod in g
                for c in prod: #every letter in that rhs prod
                    if c.islower() or c == '$':
                        eps[c] = False
                        first[c] = set(c)

        print(eps)
        print(first)
        
        for x in g.keys():
            for i in range(len(g[x])):
                if g[x][i] == '':
                    eps[x] = True
                else:
                    eps[x] = False
                first[x] = set()


        print(eps)
        print(first)

        progress = True
        while progress:
            progress = False
 
            for token in g:
                for prod in g[token]:
                    all_nullable = True
                    
                    for c in prod:
                        
                        initial_first = first[token].copy()
                        first[token].update(first[c])
                        if first[token] != initial_first:
                            progress = True 

                        if not eps.get(c, False):
                            all_nullable = False
                            break

                    if all_nullable and not eps[token]:
                        eps[token] = True
                        progress = True  
        
        print('fina eps: ', eps)
        print('fina first: ', first)
        return eps, first
    
    def follow(g):
        follow = {symbol: set() for symbol in g.keys()} 
        print('INIT FOLLOW: ', follow) 

        progress = True
        while progress:
            progress = False
      
            for A in g:
                print(A)
                for prod in g[A]:
                    print(prod)
                    for i in range(len(prod)):
                        print('prod i : ', prod[i])
                        B = prod[i]

                        if B.isupper():  
                            
                            beta = prod[i + 1:]
                            print('currenlty proces: ', beta)


                            if beta:
                                initial_follow = follow[B].copy()
                                follow[B].update(string_FIRST(beta))  
                                if follow[B] != initial_follow:
                                    progress = True

                            if not beta or string_EPS(beta):
                                initial_follow = follow[B].copy()
                                follow[B].update(follow[A])
                                if follow[B] != initial_follow:
                                    progress = True

        print("Final FOLLOW sets:", follow)
        return follow
                        
        
    def string_EPS(g):
        for lhsTerm in g:
            if not eps.get(g, False):
                return False
        return True
    
    def string_FIRST(g):
        rv = set()
        for lhsTerm in g:
            rv.update(first[lhsTerm])
            if not eps.get(g, False):
                break
        return rv
    

    eps_sets, first_sets = epsAndFirst(grammar)
    follow_sets = follow(grammar)

    writeOutput(first_sets, follow_sets)

def processG():
    g = {"S'":['S$$']}

    with open(sys.argv[1], "r") as file:
        lines = file.readlines()[1:]
        for line in lines:
            line = line.strip()
            if not line:
                continue
            lhs, rhs = line.split('->')
            lhs=lhs.strip().replace(" ", "")
            rhs=rhs.strip().replace(" ", "")
            print(rhs.split())
            if lhs in g:
                g[lhs].append(rhs)
            else:
                g[lhs] = [rhs]
    return g

def writeOutput(first_sets, follow_sets):
    print(first_sets)
    print(follow_sets)
    toPop = []
    for term in first_sets.keys():
        print('okok')
        if term.islower() or term == '$': toPop.append(term)
    for term in toPop:
        first_sets.pop(term)
    toPop = []
    print(toPop)
    for term in follow_sets.keys():
        print('okok')
        if term.islower() or term == '$': toPop.append(term)
    for term in toPop:
        follow_sets.pop(term)

    print(first_sets)
    print(follow_sets)
    
    with open(sys.argv[2], "w") as f:
        # Write "S'" first
        if "S'" in first_sets:
            if '$' in first_sets["S'"]:
                formatted_elements1 = sorted(first_sets["S'"] - {'$'})
                formatted_elements1.insert(len(formatted_elements1), '$$')
            else:
                formatted_elements1 = sorted(first_sets["S'"])
        if "S'" in follow_sets:
            if '$' in follow_sets["S'"]:
                formatted_elements2 = sorted(follow_sets["S'"] - {'$'})
                formatted_elements2.insert(len(formatted_elements2), '$$')
            else:
                formatted_elements2 = sorted(follow_sets["S'"])
        
            print(formatted_elements1)
            print(formatted_elements2)
            f.write("S'\n" + ", ".join(formatted_elements1) + "\n".join(formatted_elements2) + "\n\n")
            
        
        for nonterminal in sorted(k for k in first_sets if k != "S'"):
            if "$" in first_sets[nonterminal]:
                formatted_elements1 = sorted(first_sets[nonterminal] - {'$'})
                formatted_elements1.insert(len(formatted_elements1), '$$')
            else:
                formatted_elements1 = sorted(first_sets[nonterminal])
            if "$" in follow_sets[nonterminal]:
                formatted_elements2 = sorted(follow_sets[nonterminal] - {'$'})
                formatted_elements2.insert(len(formatted_elements2), '$$')
            else:
                formatted_elements2 = sorted(follow_sets[nonterminal])

            print(formatted_elements2)

            f.write(f"{nonterminal}\n" + ", ".join(formatted_elements1) + "\n" + ", ".join(formatted_elements2) + "\n")

        print()

main()