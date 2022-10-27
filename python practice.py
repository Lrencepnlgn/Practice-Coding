print("My name is Laurence Panaligan")
print("")
    #Today im going to show you my coding skills <33

valorantagent = ["Sage Abilities", "Phoenix Abilities", "Jett Abilities"]    
S, P, J = valorantagent   #in line 5 and line 6, this is for assigning multiple values
                                        #this is called "UNPACKING"
print(S)
print("")
print(' "BARRIER ORB" ')
print("EQUIP a barrier orb. FIRE places a wall that fortifies after a few seconds.\n"
                        "           ALT FIRE rotates the targeter.")
print("")
print(' "SLOW ORB" ')
print("EQUIP a slowing orb. FIRE to throw a slowing orb forward that detonates upon landing,\n" 
                        "       creating a lingering field that slows players caught inside of it.")
print("")
print(' "HEALING ORB" ')
print("EQUIP a healing orb. FIRE with your crosshairs over a damaged ally to activate a heal-over-time on them.\n" 
                        "       ALT FIRE while Sage is damaged to activate a self heal-over-time.")
print("")
print(' "RESURRECTION" ')
print("EQUIP a resurrection ability. FIRE with your crosshairs placed over a dead ally to begin resurrecting them.\n" 
                        "      After a brief channel, the ally will be brought back to life with full health.")

print("\n")
print("---------------------------------------------------------------------------------------------------------------")
print("\n")

print(P)
print("")
print(' "BLAZE" ')
print("     EQUIP a flame wall. FIRE to create a line of flame that moves forward,\n"
                "creating a wall of fire that blocks vision and damages players passing through it.\n"
                        "                       ALT FIRE rotates the targeter.")
print("")
print(' "CURVEBALL" ')
print("     EQUIP a flare orb that takes a curving path and detonates shortly after throwing.\n"
                "FIRE to curve the flare orb to the left, detonating and blinding any player who sees the orb.\n"
                        "                       ALT FIRE to curve the flare orb to the right.")
print("")
print(' "HOT HANDS" ')
print("     EQUIP a fireball. FIRE to throw a fireball that explodes after a set amount of time\n"
                "            or upon hitting the ground, creating a lingering fire zone that\n"
                        "                       damages enemies. ALT FIRE to lob.")
print("")
print(' "RUN IT BACK" ')
print("     INSTANTLY place a marker at Phoenix's location. While this ability is active, dying or allowing\n"
                "    the timer to expire will end this ability and bring Phoenix back to this location with full health\n"
                        "                       and the amount of armor he had when the ability was cast.")

print("\n")
print("---------------------------------------------------------------------------------------------------------------")
print("\n")


print(J)
print("")
print(' "CLOUDBURST" ')
print("     INSTANTLY throw a projectile that expands into a brief vision-blocking cloud on impact with a surface. \n"
                "             HOLD the ability key to curve the smoke in the direction of your crosshair.")
print("")             
print(' "UPDRAFT" ')
print("    INSTANTLY propel Jett high into the air.")

print("")             
print(' "TAILWIND" ')
print("      ACTIVATE to prepare a gust of wind for a limited time.\n" 
        "   RE-USE the wind to propel Jett in the direction she is moving.")

print("")             
print(' "BLADE STORM" ')
print(" EQUIP a set of highly accurate throwing knives. FIRE to throw a single knife\n" 
        "   and recharge knives on a kill. ALTERNATE FIRE to throw all\n"
        "       remaining daggers but does not recharge on a kill.")

print("\n")
print("---------------------------------------------------------------------------------------------------------------")
print("\n")

valorantagent = {"SAGE", "PHOENIX", "JETT"}     #this line 81 is a sets
print(valorantagent)

print("\n")
print("---------------------------------------------------------------------------------------------------------------")
print("\n")

sage = 10
phoenix = 11        #this is the Python Conditions and If statements
omen = 12

if sage > phoenix:
    print(" Sage is not a DUELIST.")
elif sage == omen:
    print(" Sage is a CONTROLLER.")
else:
    print(" Sage is a SENTINEL.")

print("\n")
print("---------------------------------------------------------------------------------------------------------------")
print("\n")

for x in range(21):         #this is the Else in For Loop
  print(x)
else:
  print("My age is 20!")

print("\n")
print("---------------------------------------------------------------------------------------------------------------")
print("\n")

valosentinel = ["Chamber", "Sage", "Killjoy"]
valoduelist = ["Reyna", "Raze", "Neon"]
        
    #this is nested loop
    #this is to print each valosentinel for every valoduelist

for x in valosentinel:
    for y in valoduelist:
        print(x, y)

print("\n")
print("---------------------------------------------------------------------------------------------------------------")
print("\n")


def my_valoagents(Rname, Origin, Gender):
    print(Rname + " " + Origin + " " + " "+ Gender)    #in line 127 to 136 this is a FUNCTION

print("-YORU-")
print("")
my_valoagents("Ryo Kiritani -", "Japan -", "Male")
print("\n")
print("-OMEN-")
print("")
my_valoagents("Marcus -", "Earth -", "Male")


print("\n")
print("---------------------------------------------------------------------------------------------------------------")
print("\n")

                    #this is Python Arrays

valoagents = ["Astra", "Breach", "Brimstone", "Chamber", "Cypher", "Jett",
                    "Kay/O, ", "Killjoy", "Neon", "Omen", "Phoenix",
                        "Raze", "Reyna", "Sage", "Skye", "Sova",
                            "Viper", "Yoru", "Harbor",]
x = valoagents[5]
print(x)

print("\n")
print("---------------------------------------------------------------------------------------------------------------")
print("\n")