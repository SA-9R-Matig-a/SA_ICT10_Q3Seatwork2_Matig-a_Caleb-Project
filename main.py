# Seatwork 2 - Second Quarter
from pyscript import display, document # type: ignore


def regiment_checker(e):
    document.getElementById('output').innerHTML = ' '
    document.getElementById('image').innerHTML = ' '
    document.getElementById('leader').innerHTML = ' '

    registration_input = document.querySelector('input[name="registration"]:checked')
    clearance_input = document.querySelector('input[name="clearance"]:checked')

    #checks if inputs are empty
    if registration_input is None:
        display("Please select your registration status.", target="output")
        return
    if clearance_input is None:
        display("Please select your medical clearance.", target="output")
        return

    registration = registration_input.value
    clearance = clearance_input.value
    grade_level = int(document.getElementById('level').value)
    section = document.getElementById('section').value
    registration_input = document.querySelector('input[name="registration"]:checked')
    clearance_input = document.querySelector('input[name="clearance"]:checked')
    registration = registration_input.value
    average = float(document.getElementById('average').value)

    #checks for 'no' on registration and clearance
    if registration != 'registered':
        display(f'Not eligible: student is not registered for Regiment Selection. Ask your Military School Instructor regarding the online registraton.', target='output')
    elif clearance != 'cleared':
        display(f'Not eligible: medical clearance required. Go to the field hospital and secure your clearance.', target='output')

    if average < 95:
        display(f'Not Eligible for Military Police', target='eligible')
    else:
        display(f'Eligible for Military Police', target='eligible')

    #checks first the average, then the grade level, and lastly the section to determine regiment and squad number
    #if average is less than 95, will check for other conditions to determine which regiment to join
    if average < 95:
        if grade_level == 7:
            if section == "emerald":
                display(f'Congratulations! You are part of the Training Corps, Squad 1!', target='output')
                document.getElementById("image").innerHTML = """
                <img src="https://static.wikia.nocookie.net/attack-on-titan-regiments/images/8/81/Training_Corps.png/revision/latest?cb=20180127213207" width="300">
                """
                display(f'You Report to Keith Shadis', target='leader')
            elif section == "ruby":
                display(f'Congratulations! You are part of the Training Corps, Squad 2!', target='output')
                document.getElementById("image").innerHTML = """
                <img src="https://static.wikia.nocookie.net/attack-on-titan-regiments/images/8/81/Training_Corps.png/revision/latest?cb=20180127213207" width="300">
                """
                display(f'You Report to Keith Shadis', target='leader')
        elif grade_level == 8:
            if section == "emerald":
                display(f'Congratulations! You are part of the Garrison Regiment, Squad Rico!', target='output')
                document.getElementById("image").innerHTML = """
                <img src="https://static.wikia.nocookie.net/shingekinokyojin/images/5/55/Garrison_Logo.png/revision/latest?cb=20140307090257" width="300">
                """
                display(f'You Report to Dot Pixis', target='leader')
            elif section == "ruby":
                display(f'Congratulations! You are part of the Scout Regiment, Squad Levi!', target='output')
                document.getElementById("image").innerHTML = """
                <img src="https://static.wikia.nocookie.net/shingekinokyojin/images/a/a7/Survey_Corps_Logo.png/revision/latest?cb=20140307090257" width="300">
                """
                display(f'You Report to Erwin Smith', target='leader')
        elif grade_level == 9:
            if section == "emerald":
                display(f'Congratulations! You are part of the Garrison Regiment, Squad Rico!', target='output')
                document.getElementById("image").innerHTML = """
                <img src="https://static.wikia.nocookie.net/shingekinokyojin/images/5/55/Garrison_Logo.png/revision/latest?cb=20140307090257" width="300">
                """
                display(f'You Report to Dot Pixis', target='leader')
            elif section == "ruby":
                display(f'Congratulations! You are part of the Scout Regiment, Squad Levi!', target='output')
                document.getElementById("image").innerHTML = """
                <img src="https://static.wikia.nocookie.net/shingekinokyojin/images/a/a7/Survey_Corps_Logo.png/revision/latest?cb=20140307090257" width="300">
                """
                display(f'You Report to Erwin Smith', target='leader')
        elif grade_level == 10: 
            if section == "emerald":
                display(f'Congratulations! You are part of the Garrison Regiment, Corps of Engineers!', target='output')
                document.getElementById("image").innerHTML = """
                <img src="https://static.wikia.nocookie.net/shingekinokyojin/images/5/55/Garrison_Logo.png/revision/latest?cb=20140307090257" width="300">
                """
                display(f'You Report to Dot Pixis', target='leader')
            elif section == "ruby":
                display(f'Congratulations! You are part of the Scout Regiment, Titan Research!', target='output')
                document.getElementById("image").innerHTML = """
                <img src="https://static.wikia.nocookie.net/shingekinokyojin/images/a/a7/Survey_Corps_Logo.png/revision/latest?cb=20140307090257" width="300">
                """
                display(f'You Report to Erwin Smith', target='leader')

    #if average is equal to or greater than 95, automatically join the Military Police and assign a squad
    else:
        display(f'Congratulations! You are part of the Military Police, Interior Squad - Anti-Personnel', target='output')
        document.getElementById("image").innerHTML = """
            <img src="https://static.wikia.nocookie.net/attack-on-titan-regiments/images/e/ea/Military_Police.png/revision/latest?cb=20180127213300" width="300">
                """
        display(f'You Report to Nile Dok', target='leader')