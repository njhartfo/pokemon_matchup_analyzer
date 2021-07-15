import tkinter as tk

#Pokemon
    #Moves
        #Move Slots
        #Move Types

# Establishes determining factors of each type
class Type:
    
    # Declare weaknesses and strengths
    def __init__(self):
        self.weak = []
        self.strong = []
        self.effective = 1
        self.non_effective = -1
        
    def set_weak(self, *args):
        for _ in args:
            self.weak.append(_)
            
    def set_strong(self, *args):
        for _ in args:
            self.strong.append(_)
            
    def get_weak(self):
        return self.weak
        
    def get_strong(self):
        return self.strong
        
    

# Class for each pokemon instance
class Pokemon(Type):
    
    def __init__(self, type1, type2=None):
        self.type1 = type1
        self.type2 = type2
        self.moves = []
        self.total_weak = type1.weak + type2.weak
        self.total_strong = type1.strong + type2.strong
        
    def set_all_moves(self, *args):
        for _ in args:
            self.moves.append(_)
            
    def get_all_moves(self):
        return self.moves
        
    def get_move1(self):
        return self.moves[0]
        
    def get_move2(self):
        return self.moves[1]
        
    def get_move3(self):
        return self.moves[2]
        
    def get_move4(self):
        return self.moves[3]
        
    def set_move1(self, move):
        self.moves[0] = move
        
    def set_move2(self, move):
        self.moves[1] = move

    def set_move3(self, move):
        self.moves[2] = move
    
    def set_move4(self, move):
        self.moves[3] = move
    
            
    def get_type1(self):
        return self.type1
        
    def set_type1(self, t):
        self.type1 = t
        
    def get_type2(self):
        return self.type2
        
    def set_type2(self, t):
        self.type2 = t
        
class Move:
    
    def __init__(self, bp, acc, typing):
        self.bp = bp
        self.acc = acc
        self.typing = typing
        
    def get_bp(self):
        return self.bp
    
    def set_bp(self, bp):
        self.bp = bp
        
    def get_acc(self):
        return self.acc
    
    def set_acc(self, acc):
        self.acc = acc

    def get_typing(self):
        return self.typing
        
    def set_typing(self, typing):
        self.typing = typing

# Compares the types of both pokemon and determines advantage
# Uses a basic counter system to measure the type comparison
def battle_calc(poke1, poke2):
    effective_counter = 0
    
    if poke1.type1 in poke2.total_strong or poke1.type2 in poke2.total_strong:
        effective_counter = effective_counter + 1
        
    if poke1.type1 in poke2.total_weak or poke1.type2 in poke2.total_weak:
        effective_counter = effective_counter - 1
        
    if effective_counter < 0:
        return "You have the advantage"
        
    elif effective_counter > 0:
        return "You have a disadvantage"
        
    return "Neutral state"
        
#------- Type Instantiation --------#       
normal   = Type()
fire     = Type()
water    = Type()
grass    = Type()
electric = Type()
ice      = Type()
fighting = Type()
poison   = Type()
ground   = Type()
flying   = Type()
psychic  = Type()
bug      = Type()
rock     = Type()
ghost    = Type()
dragon   = Type()
dark     = Type()
steel    = Type()
fairy    = Type()

#-------- Set Typings ---------#
normal.set_weak(fighting)

fire.set_weak(water, ground, rock)
fire.set_strong(grass, ice, bug, steel)

water.set_weak(electric, grass)
water.set_strong(fire, ground, rock)

grass.set_weak(fire, ice, poison, flying, bug)
grass.set_strong(water, ground, rock)

electric.set_weak(ground)
electric.set_strong(water, flying)

ice.set_weak(fire, fighting, rock, steel)
ice.set_strong(grass, ground, flying, dragon)

fighting.set_weak(flying, psychic, fairy)
fighting.set_strong(normal, ice, rock, dark, steel)

poison.set_weak(ground, psychic)
poison.set_strong(grass, fairy)

ground.set_weak(water, grass, ice)
ground.set_strong(fire, electric, poison, rock, steel)

flying.set_weak(electric, ice, rock)
flying.set_strong(grass, fighting, bug)

psychic.set_weak(bug, ghost, dark)
psychic.set_strong(fighting, poison)

bug.set_weak(fire, flying, rock)
bug.set_strong(grass, psychic, dark)

rock.set_weak(water, grass, fighting, ground, steel)
rock.set_strong(fire, ice, flying, bug)

ghost.set_weak(ghost, dark)
ghost.set_strong(ghost, psychic)

dragon.set_weak(ice, dragon, fairy)
dragon.set_strong(dragon)

dark.set_weak(fighting, bug, fairy)
dark.set_strong(psychic, ghost)

steel.set_weak(fire, fighting, ground)
steel.set_strong(ice, rock, fairy)

fairy.set_weak(poison, steel)
fairy.set_strong(fighting, dragon, dark)

#-------- Create Pokemon ------- #
charizard = Pokemon(fire, flying)
venasaur = Pokemon(grass, poison)
blastoise = Pokemon(water, None)

x = battle_calc(charizard, venasaur)
print(x)
