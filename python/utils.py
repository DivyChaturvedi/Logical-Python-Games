def finding_max(numbers):
    a=numbers[0]
    for i in range(len(numbers)):
        if a < numbers[i]:
            a=numbers[i]
    return a  
