today=int(input())
if today>30:
    tommorow=1
else:
    tommorow=(today+1)
yesterday=(today-1)
print(yesterday, today, tommorow)
