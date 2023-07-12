# This program just prompts the user for
# whatever log they wish to view from a list
# and displays it on the screen

capLgs=["uwu meowmeow","honk","gay","as","ping","gae","hon",]
x=len(capLgs)
mes='Please enter a number from 1 to '+str(x)
mes=mes+':\n'
# This successfully prints a numeric value
# entered by the user, and doesn't take any number
# outside of the value range.

# Function for printing so-called captain's logs.
# These were probably written by a goober
def pinga():
    co=0
    er='That is not right :<'
    while True:
        try:
            match co:
                case 3:
                    er='Please just do this correctly...'
                case 6:
                    er='Really...'
                case 10:
                    er='Why are you like this'
            inp=eval(input(mes))
            z=inp
            if(z>0):
                print(capLgs[abs(z-1)])
                break;
            else:
                print(er)
                co=co+1
        except IndexError:
            print(er)
            co=co+1
        except NameError:
            print(er)
            co=co+1
        except SyntaxError:
            print(er)
            co=co+1

pinga()
print(input('\nPress Enter to continue...'))
