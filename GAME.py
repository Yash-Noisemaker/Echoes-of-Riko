import random

def main():
    # Game introduction
    print("Welcome to the Adventure Puzzle Game!")
    print("You are about to embark on an exciting journey full of mysteries and choices.")
    print("Your decisions will determine your path. Choose wisely!")
    print("Type 'quit' at any time to exit the game.")
    print("Type 'inventory' to check your items.\n")
    
    # Initial location and inventory
    current_location = "house"
    inventory = []
    ring_taken = False
    stones_thrown = 0
    tablet_read = False
    knife_found = False
    tree_quiz_completed = False
    dwarf_awakened = False
    well_passage_opened = False
    blue_pearl_given = False
    forest_path_opened = False
    lucky_draw_played = False
    witch_choice_made = False
    market_stone_taken = False  
    
    # Game loop
    while True:
        if current_location == "house":
            print("You are in your house. It's cozy but you feel the urge to explore.")
            if forest_path_opened:
                print("Available paths: North (forest), East (river), West (old well), South (forest.), West (dyne city)")
            else:
                print("Available paths: North (forest), East (river), West (old well), South (forest.)")
            
            direction = get_direction(inventory)                    
            if direction == "north":
                current_location = "forest"
            elif direction == "east":
                current_location = "river"
            elif direction == "west":
                current_location = "old well"
            elif direction == "south":
                current_location = "forest."
            elif direction == "west" and forest_path_opened:
                current_location = "dyne city"
            else:
                handle_quit(direction)
                
        elif current_location == "forest":
            print("You are in a dense forest. The trees are tall and the path is narrow.")
            
            if not knife_found:
                print("Available paths: North (Riko Kingdom), South (house), West (broken shed)")
            else:
                print("Available paths: North (Riko Kingdom), South (house)")
            
            direction = get_direction(inventory)
            if direction == "north":
                current_location = "riko kingdom"
            elif direction == "south":
                current_location = "house"
            elif direction == "west" and not knife_found:
                current_location = "broken shed"
            else:
                print("That path is blocked by thick vegetation. Try another direction.") 
                handle_quit(direction)
                
        elif current_location == "broken shed":
            print("You found a broken, abandoned shed. The door is hanging off its hinges.")
            
            if not knife_found:
                print("Inside, you find an old but sturdy knife on a workbench.")
                take_knife = input("Do you want to take the knife? (yes/no): ").lower().strip()
                if take_knife == "yes":
                    print("You take the knife. It might be useful for cutting through vegetation.")
                    inventory.append("Knife")
                    knife_found = True
                else:
                    print("You leave the knife where it is.")
            
            print("Available paths: East (forest)")
            
            direction = get_direction(inventory)
            if direction == "east":
                current_location = "forest"
            else:
                print("There's no other exit from the shed.")
                handle_quit(direction)
                
        elif current_location == "forest.":
            print("You are in a different part of the forest. The trees here seem older and more mysterious.")
            if forest_path_opened:
                print("Available paths: West (forest.), East (shen jungle entrance), North(house), South (dyne city)")
            else:
                print("Available paths: West (forest.), East (shen jungle entrance), North(house)")
            
            direction = get_direction(inventory)
            if direction == "west":
                current_location = "forest. west"
            elif direction == "east":
                current_location = "shen jungle entrance"
            elif direction == "north":
                current_location = "house"
            elif direction == "south" and forest_path_opened:
                current_location = "dyne city"
            else:
                print("That path is blocked. Try another direction.")
                handle_quit(direction)
                
        elif current_location == "forest. west":
            print("This area of the forest is dense with no clear paths ahead.")
            print("You'll have to turn back.")
            print("Available paths: East (forest.)")
            
            direction = get_direction(inventory)
            if direction == "east":
                current_location = "forest."
            else:
                print("There's no path in that direction.")
                handle_quit(direction)
                
        elif current_location == "shen jungle entrance":
            print("You've reached the entrance to Shen Jungle. The vegetation is incredibly thick and exotic.")
            print("A sign warns: 'Dangerous territory. Proper tools required to proceed.'")
            
            if "Knife" in inventory:
                print("Your knife should help you cut through the dense vegetation.")
                enter_jungle = input("Do you want to enter Shen Jungle? (yes/no): ").lower().strip()
                if enter_jungle == "yes":
                    current_location = "shen jungle"
                else:
                    print("You decide to stay at the entrance.")
            else:
                print("You don't have the proper tools to enter this dangerous jungle.")
                print("You'll need to find something to cut through the thick vegetation.")
            
            print("Available paths: West (forest.), North()")
            
            direction = get_direction(inventory)
            if direction == "west":
                current_location = "forest."
            else:
                print("You can only return to the forest from here.")
                handle_quit(direction)
                
        elif current_location == "shen jungle":
            print("You are deep in Shen Jungle. The air is humid, and strange sounds echo around you.")
            print("The vegetation is so thick that only one path seems viable.")
            print("Available paths: North (ancient tree), West(Forest.)")
            
            direction = get_direction(inventory)
            if direction == "north":
                current_location = "ancient tree"
            if direction == "west":
                current_location = "forest."
            else:
                print("The jungle is too dense to go that way. You can only go north.")
                handle_quit(direction)
                
        elif current_location == "ancient tree":
            print("Before you stands an enormous ancient tree, its trunk wider than a house.")
            print("As you approach, the tree's bark shifts to form something resembling a face!")
            
            if not tree_quiz_completed:
                print("The tree speaks in a deep, rumbling voice:")
                print("'Traveler, to pass through me, you must answer three questions correctly.'")
                
                # Question 1
                answer1 = input("First question: I'm a tall, green giant who lives for years, I'm home to birds and lose my tears? ").lower().strip()
                if answer1 != "tree":
                    print("The tree rumbles: 'Incorrect. You may not pass.'")
                    print("Available paths: South (shen jungle)")
                    
                    direction = get_direction(inventory)
                    if direction == "south":
                        current_location = "shen jungle"
                    else:
                        print("You can only return to the jungle.")
                        handle_quit(direction)
                    continue
                
                # Question 2
                answer2 = input("Second question: What do you throw in the old well? ").lower().strip()
                if "red sun" not in answer2 and "red stone" not in answer2:
                    print("The tree rumbles: 'Incorrect. You may not pass.'")
                    print("Available paths: South (shen jungle)")
                    
                    direction = get_direction(inventory)
                    if direction == "south":
                        current_location = "shen jungle"
                    else:
                        print("You can only return to the jungle.")
                        handle_quit(direction)
                    continue
                
                # Question 3
                answer3 = input("Third question: What tool helps you enter Shen Jungle? ").lower().strip()
                if answer3 != "knife":
                    print("The tree rumbles: 'Incorrect. You may not pass.'")
                    print("Available paths: South (shen jungle)")
                    
                    direction = get_direction(inventory)
                    if direction == "south":
                        current_location = "shen jungle"
                    else:
                        print("You can only return to the jungle.")
                        handle_quit(direction)
                    continue
                
                print("The tree rumbles: 'All answers are correct!'")
                print("The ground begins to shake, leaves fall all around you,")
                print("and a passage opens at the base of the tree.")
                tree_quiz_completed = True
            
            print("Available paths: South (shen jungle), East (underground passage)")
            
            direction = get_direction(inventory)
            if direction == "south":
                current_location = "shen jungle"
            elif direction == "east":
                current_location = "underground passage"
            else:
                print("You can only go south or east from here.")
                handle_quit(direction)
                
        elif current_location == "underground passage":
            print("You enter the dark passage at the base of the tree.")
            print("After walking for what seems like hours, you emerge in a small cavern.")
            print("In the center of the cavern is a small home carved into the rock.")
            
            if not dwarf_awakened:
                print("An old dwarf is sleeping soundly in a chair.")
                wake_dwarf = input("Do you want to wake the dwarf? (yes/no): ").lower().strip()
                if wake_dwarf == "yes":
                    print("As you gently shake the dwarf, his eyes flutter open.")
                    print("He looks at you and begins to speak:")
                    print("'I am Durin, the last of the mountain dwarves. I've been sleeping for centuries.'")
                    print("'Long ago, I protected the Blue Pearl of Wisdom, but it was stolen from me.'")
                    print("'The pearl holds ancient knowledge and power. Would you like to have it?'")
                    
                    take_pearl = input("Do you want the Blue Pearl? (yes/no): ").lower().strip()
                    if take_pearl == "yes":
                        print("Durin hands you a glowing blue pearl. It feels warm to the touch.")
                        inventory.append("Blue Pearl")
                        print("'With this pearl, you enter a place you may not have permission to enter.'")
                        
                        open_path = input("Would you like me to open a path to the forest for you? (yes/no): ").lower().strip()
                        if open_path == "yes":
                            print("Durin waves his hand, and you feel the ground shake.")
                            print("A new path has opened in the forest!")
                            forest_path_opened = True
                        else:
                            print("Durin nods. 'The path will remain closed for now.'")
                    else:
                        print("Durin looks disappointed. 'Very well, the pearl shall remain with me.'")
                    
                    dwarf_awakened = True
                else:
                    print("You decide not to disturb the sleeping dwarf.")
            else:
                print("Durin is awake and smiles at you. 'Have you made your decision about the pearl?'")
            
            print("Available paths: West (ancient tree)")
            
            direction = get_direction(inventory)
            if direction == "west":
                current_location = "ancient tree"
            else:
                print("The only way out is back through the passage.")
                handle_quit(direction)
                
        elif current_location == "river":
            print("You are at a beautiful river. The water flows gently.")
            print("Available paths: West (House), North (Forest)")
            
            direction = get_direction(inventory)
            if direction == "west":
                current_location = "house"
            elif direction == "north":
                current_location = "forest"
            else:
                print("You can't go that way from here. Try another direction.")
                handle_quit(direction)
                
        elif current_location == "old well":
            print("You are at an old, mysterious well. It seems abandoned for years.")
            
            
            if not tablet_read:
                read_tablet = input("There's a stone tablet nearby. Do you want to read it? (yes/no): ").lower().strip()
                if read_tablet == "yes":
                    print("\nThe tablet reads: 'Throw three red sun stones into the well to reveal its secret.'")
                    tablet_read = True
                else:
                    print("You decide not to read the tablet.")
            
            
            if "Red Sun Stone" in inventory and stones_thrown < 3:
                throw_stone = input("Do you want to throw a Red Sun Stone into the well? (yes/no): ").lower().strip()
                if throw_stone == "yes":
                    inventory.remove("Red Sun Stone")
                    stones_thrown += 1
                    print(f"You throw a Red Sun Stone into the well. It makes an echoing splash. ({stones_thrown}/3 stones thrown)")
                    
                    if stones_thrown == 3:
                        print("As the third stone hits the water, the well begins to glow with a soft light!")
                        print("A hidden passage is revealed at the bottom of the well!")
                        well_passage_opened = True
                else:
                    print("You decide to keep your stone.")
            elif stones_thrown >= 3:
                print("You've already thrown all three Red Sun Stones into the well.")
                print("The well glows with a soft light, and a hidden passage is visible at the bottom.")
            
            
            if well_passage_opened:
                print("Available paths: East (house), West (well passage)")
            else:
                print("Available paths: East (house)")
            
            direction = get_direction(inventory)
            if direction == "east":
                current_location = "house"
            elif direction == "west" and well_passage_opened:
                current_location = "well passage"
            else:
                if direction == "west" and not well_passage_opened:
                    print("There's no path to the west yet. You need to throw all three Red Sun Stones into the well.")
                else:
                    print("There's no path in that direction. Try another way.")
                handle_quit(direction)
                
        elif current_location == "well passage":
            print("You climb down into the well and enter the newly revealed passage.")
            print("The tunnel is dark and damp, but you can see light at the end.")
            print("This area is still under development. More adventures await here!")
            print("Available paths: East (old well)")
            
            direction = get_direction(inventory)
            if direction == "east":
                current_location = "old well"
            else:
                print("You can only return to the well from here.")
                handle_quit(direction)
                
        elif current_location == "riko kingdom":
            print("You've arrived at Riko Kingdom. The buildings are magnificent!")
            print("Available paths: North (border of castle), South (forest), West (riko market)")
            
            direction = get_direction(inventory)
            if direction == "north":
                current_location = "border of castle"
            elif direction == "south":
                current_location = "forest"
            elif direction == "west":
                current_location = "riko market"
            else:
                print("The kingdom walls prevent you from going that way.")
                handle_quit(direction)
                
        elif current_location == "border of castle":
            print("You are at the border of the castle. Guards are patrolling the area.")
            
            if "Blue Pearl" in inventory and not blue_pearl_given:
                print("The guards notice the Blue Pearl in your possession.")
                print("'The Blue Pearl! You may enter the castle.'")
                print("They take the pearl from you and allow you to pass.")
                inventory.remove("Blue Pearl")
                blue_pearl_given = True
                print("Available paths: South (Riko Kingdom), North (castle)")
            elif blue_pearl_given:
                print("The guards recognize you and allow you to pass.")
                print("Available paths: South (Riko Kingdom), North (castle)")
            else:
                print("You don't have permission to enter now!")
                print("Available paths: South (Riko Kingdom)")
            
            direction = get_direction(inventory)
            if direction == "south":
                current_location = "riko kingdom"
            elif direction == "north" and (blue_pearl_given or "Blue Pearl" in inventory):
                current_location = "castle"
            elif direction == "north":
                print("The guards stop you: 'No one is allowed beyond this point!'")
            elif direction == "east":
                print("There's waterfall, you can't go ahead.")       
            else:
                print("You can't go that way from the border.")
                handle_quit(direction)
            
        elif current_location == "castle":
            print("You have entered the castle of Riko Kingdom!")
            print("The interior is magnificent, but the creator hasn't developed this area further.")
            print("You've explored most of the map! Type 'quit' to end the game.")
            print("Available paths: South (border of castle)")
            
            direction = get_direction(inventory)
            if direction == "south":
                current_location = "border of castle"
            else:
                print("You can only return to the castle border.")
                handle_quit(direction)
                
        elif current_location == "riko market":
            print("You are in market of riko kingdom, want to buy something?")
            print("There are 7 shops, but you don't have money, LOL :)")
            
            
            if not market_stone_taken:
                find_stone = input("You notice a peculiar red stone with a sun symbol on a merchant's table. Take it? (yes/no): ").lower().strip()
                if find_stone == "yes":
                    print("You discreetly take the Red Sun Stone when the merchant isn't looking.")
                    inventory.append("Red Sun Stone")
                    market_stone_taken = True
                else:
                    print("You decide to leave the stone where it is.")
                    market_stone_taken = False  
            else:
                print("You've already taken the Red Sun Stone from here.")
            
            print("Available paths: East (Riko kingdom), South (Old sage statue)")

            direction = get_direction(inventory)
            if direction == "east":
                current_location = "riko kingdom"
            elif direction == "south":
                current_location = "old sage statue"
            else:
                print("That path is blocked. Try another direction.")
                handle_quit(direction)

        elif current_location == "old sage statue":
            print("This is a statue of the old sage who protected the kingdom with his divine power.")
            
            if not ring_taken:
                print("You notice a shiny ring on the statue's finger.")
                take_ring = input("Do you want to take the ring? (yes/no): ").lower().strip()
                
                if take_ring == "yes":
                    print("You carefully take the ring from the statue's finger.")
                    print("It feels warm to the touch and glows with a faint light.")
                    inventory.append("Mysterious Ring")
                    ring_taken = True
                elif take_ring == "no":
                    print("You decide to leave the ring where it is.")
                else:
                    print("Invalid choice. The ring remains on the statue.")
            else:
                print("The statue stands tall, but the ring is no longer on its finger.")
            
            print("Available paths: North (riko market)")
            
            direction = get_direction(inventory)
            if direction == "north":
                current_location = "riko market"
            else:
                print("You can only go back to the market from here.")
                handle_quit(direction)
                
        elif current_location == "dyne city":
            print("Welcome to Dyne City! A bustling town with various shops and buildings.")
            print("Available paths: North (forest.), West (kindergarten), East (lucky draw), South (dyne city.)")
            
            direction = get_direction(inventory)
            if direction == "north":
                current_location = "forest."
            elif direction == "west":
                current_location = "kindergarten"
            elif direction == "east":
                current_location = "lucky draw"
            elif direction == "south":
                current_location = "dyne city."
            else:
                print("That path is blocked. Try another direction.")
                handle_quit(direction)
                
        elif current_location == "kindergarten":
            print("You enter a kindergarten school. Children are playing everywhere.")
            print("A teacher approaches you: 'Please stay away from the kids! This is a safe space for children.'")
            print("Available paths: East (dyne city)")
            
            direction = get_direction(inventory)
            if direction == "east":
                current_location = "dyne city"
            else:
                print("You can only return to Dyne City.")
                handle_quit(direction)
                
        elif current_location == "lucky draw":
            print("Welcome to the Lucky Draw Shop! Spin the wheel for a chance to win prizes.")
            
            if not lucky_draw_played:
                play_game = input("Would you like to play? It costs nothing! (yes/no): ").lower().strip()
                if play_game == "yes":
                    print("Spinning the wheel...")
                    result = random.choice(["white", "black"])
                    
                    if result == "white":
                        print("Congratulations! The white ball came out. You win a Red Sun Stone!")
                        inventory.append("Red Sun Stone")
                    else:
                        print("Sorry! The black ball came out. You didn't win anything this time.")
                    
                    lucky_draw_played = True
                else:
                    print("Maybe next time!")
            else:
                print("You've already played the lucky draw game. Come back another day!")
            
            print("Available paths: West (dyne city)")
            
            direction = get_direction(inventory)
            if direction == "west":
                current_location = "dyne city"
            else:
                print("You can only return to Dyne City.")
                handle_quit(direction)
                
        elif current_location == "dyne city.":
            print("You are in another part of Dyne City. This area has residential buildings.")
            print("Available paths: North (dyne city), West (witch tent), East (uncle john house), South (dyne city..)")
            
            direction = get_direction(inventory)
            if direction == "north":
                current_location = "dyne city"
            elif direction == "west":
                current_location = "witch tent"
            elif direction == "east":
                current_location = "uncle john house"
            elif direction == "south":
                current_location = "dyne city.."
            else:
                print("That path is blocked. Try another direction.")
                handle_quit(direction)
                
        elif current_location == "uncle john house":
            print("You meet Uncle John, an elderly man with a kind smile.")
            print("He invites you in for tea and tells you a story:")
            print("'Did you know the atomic bomb was created through the Manhattan Project during WWII?'")
            print("'Scientists like Oppenheimer worked on splitting the atom to create immense energy.'")
            print("'It changed the world forever, for better or worse.'")
            print("Available paths: West (dyne city.)")
            
            direction = get_direction(inventory)
            if direction == "west":
                current_location = "dyne city."
            else:
                print("You can only return to Dyne City.")
                handle_quit(direction)
                
        elif current_location == "witch tent":
            print("You enter a mysterious tent filled with potions and strange artifacts.")
            print("A witch approaches you: 'I can see you're on an important journey.'")
            
            if not witch_choice_made:
                print("I can offer you two choices:")
                print("a) I can transport you directly to the castle")
                print("b) I can give you a powerful shield for protection")
                
                choice = input("Which do you choose? (a/b): ").lower().strip()
                if choice == "a":
                    print("The witch waves her hands and chants a spell.")
                    print("You feel dizzy for a moment, and when you open your eyes, you're at the castle border!")
                    current_location = "border of castle"
                    witch_choice_made = True
                elif choice == "b":
                    print("The witch gives you a glowing shield. 'This will protect you on your journey.'")
                    print("'If you aren't busy, check the guards of the castle.'")
                    inventory.append("Powerful Shield")
                    witch_choice_made = True
                else:
                    print("The witch looks confused. 'That wasn't one of the options.'")
            else:
                print("The witch smiles. 'I've already helped you on your journey.'")
            
            if current_location == "witch tent":
                print("Available paths: East (dyne city.)")
                direction = get_direction(inventory)
                if direction == "east":
                    current_location = "dyne city."
                else:
                    print("You can only return to Dyne City.")
                    handle_quit(direction)
                
        elif current_location == "dyne city..":
            print("This is the southern part of Dyne City. It's quieter here.")
            print("Available paths: North (dyne city.), West (abandoned house), East (food shop), South (map edge)")
            
            direction = get_direction(inventory)
            if direction == "north":
                current_location = "dyne city."
            elif direction == "west":
                current_location = "abandoned house"
            elif direction == "east":
                current_location = "food shop"
            elif direction == "south":
                print("The map is locked. You cannot go further south.")
            else:
                print("That path is blocked. Try another direction.")
                handle_quit(direction)
                
        elif current_location == "food shop":
            print("You enter a food shop. The aroma of fresh bread fills the air.")
            print("The shopkeeper says: 'Everything looks delicious, but you don't have money to buy any food.'")
            print("Available paths: West (dyne city..)")
            
            direction = get_direction(inventory)
            if direction == "west":
                current_location = "dyne city.."
            else:
                print("You can only return to Dyne City.")
                handle_quit(direction)
                
        elif current_location == "abandoned house":
            print("You enter an abandoned house. Dust covers everything.")
            print("A note on the table reads: 'The owner of this house left years ago and became CEO of Google.'")
            print("Available paths: East (dyne city..)")
            
            direction = get_direction(inventory)
            if direction == "east":
                current_location = "dyne city.."
            else:
                print("You can only return to Dyne City.")
                handle_quit(direction)
                
        print()

def get_direction(inventory):
    while True:
        direction = input("Which direction do you want to go? (north/south/east/west): ").lower().strip()
        
        if direction in ["north", "south", "east", "west", "quit"]:
            return direction
        elif direction == "inventory":
            show_inventory(inventory)
        else:
            print("Invalid direction. Please choose north, south, east, or west.")

def show_inventory(inventory):
    if not inventory:
        print("Your inventory is empty.")
    else:
        print("Your inventory contains:")
        for item in inventory:
            print(f"- {item}")

def handle_quit(input_str):
    if input_str == "quit":
        print("Thanks for playing! Goodbye.")
        exit()

if __name__ == "__main__":
    main()