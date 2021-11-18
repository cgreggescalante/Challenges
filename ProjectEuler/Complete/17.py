ones = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
teens = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
tens = ['', 'ten', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
total = 11

for i in range(1, 1000):
    num = ''
    if len(str(i)) == 1:
        num += (ones[i])
    elif len(str(i)) == 3:
        num += ones[int(str(i)[0])] + 'hundred'
        if not str(i)[-2:] == '00':
            num += 'and'
        if str(i)[-2] == '1':
            num += (teens[int(str(i)[-1]) - 10])
        else:
            num += (tens[int(str(i)[-2])] + ones[int(str(i)[-1])])

    elif len(str(i)) == 2:
        if str(i)[-2] == '1':
            num += (teens[int(str(i)[-1]) - 10])
        else:
            num += (tens[int(str(i)[-2])] + ones[int(str(i)[-1])])

    print(num)
    total += len(num)

print(total)