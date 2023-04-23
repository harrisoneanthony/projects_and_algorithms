'''
expanded_from(807.304); // Should return "800 + 7 + 3/10 + 4/1000"
expanded_from(1.24); // should return "1 + 2/10 + 4/100"
expanded_from(7.304); // should return "7 + 3/10 + 4/1000"
expanded_from(0.04); // should return "4/100"
'''

def expanded_form_two(num):
    answer,num,decimal,decimal_idx=[], str(num), False, str(num).index(".")
    print(decimal_idx)
    for i in range(len(num)):
        if num[i] != '0' and decimal == False:
            if num[i] != ".":
                answer.append(f"{num[i]}{'0'*(len(num)-i-1-(len(num)-decimal_idx))}")
            else:
                decimal = True
        if num[i] != '0' and decimal == True and num[i] != ".":
            answer.append(f"{num[i]}/1{'0'*(i-decimal_idx)}")
    return " + ".join(answer)

print(expanded_form_two(807.304))