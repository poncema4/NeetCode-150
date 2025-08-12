def robot(s):
    
    fixed = sorted(s)

    d_count = 0
    u_count = 0

    for char in range(len(fixed)):
        if fixed[char] == "D":
            d_count += 1
        else:
            u_count += 1
    
    if d_count > u_count:
        return "D"
    elif d_count < u_count:
        return "U"
    else:
        return ""