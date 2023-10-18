def calculate_grade(maths, physics, geo, chem):
    # checking for negative values
    if any(mark < 0 or mark > 100 for mark in [maths, physics, geo, chem]):
        return 'unrecognized marks/avg'
    # calculate avg
    avg = (maths + physics + geo + chem) / 4

    # determining grade based on the avg
    if 0 <= avg <= 30:
        return 'D'
    elif 31 <= avg <= 50:
        return 'C'
    elif 51 <= avg <= 70:
        return 'B'
    elif 71 <= avg <= 100:
        return 'A'

# input marks for each subject


maths = float(input('Enter Maths mark: '))
physics = float(input('Enter physics mark: '))
geo = float(input('Enter geo marks: '))
chem = float(input('Enter chem marks: '))

# get the grade and display it
result = calculate_grade(maths, physics, geo, chem)
print(f'Grade: {result}')

