#match case statement (SWITCH)= an alternatice to use many elif statements 
#                               execute some code when a value matches a case
#                               benefits=cleaner and syntax is more readable 

def day_of_week(day):
    match day:
        case 1:
            return "its sunday"
        case 2:
            return "its monday"
        case 3:
            return "its tuesday"
        case 4:
            return "its wednesday"
        case 5:
            return "its thursday"
        case 6:
            return "its friday"
        case 7:
            return "its saturday"
        case _:
            return "not a valid day!"
        
    

def is_weekend (day) :
    match day:
        case "Saturday" | "Sunday":
            return True
        case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
            return False
        case _:
            return "not a valid day"
        

print (is_weekend("Friday"))