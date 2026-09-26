import random
import time

class VacuumEnvironment:
    def __init__(self):
        # Rooms can be "Clean" or "Dirty"
        self.locations = {"A": "Clean", "B": "Clean"}
        self.agent_location = random.choice(["A", "B"])
        self.performance_score = 0
        
    def randomize_dirt(self):
        """Randomly deposits dirt into the rooms."""
        for room in self.locations:
            if random.random() < 0.6:  # 60% chance to become dirty
                self.locations[room] = "Dirty"

    def get_percept(self):
        """Returns what the agent currently senses: (Location, Status)."""
        return self.agent_location, self.locations[self.agent_location]

    def display_status(self):
        """Prints the current world configuration state."""
        print(f"Agent Location: [{self.agent_location}] | Room A: {self.locations['A']} | Room B: {self.locations['B']} | Score: {self.performance_score}")


class ReflexVacuumAgent:
    def __init__(self):
        pass

    def act(self, percept):
        """
        Reflex Rules:
        1. If current room is Dirty -> Suck dirt.
        2. If in Room A and clean -> Move Right to B.
        3. If in Room B and clean -> Move Left to A.
        """
        location, status = percept
        
        if status == "Dirty":
            return "Suck"
        elif location == "A":
            return "Right"
        elif location == "B":
            return "Left"


# --- Simulation Loop ---
def run_simulation(steps=5):
    env = VacuumEnvironment()
    agent = ReflexVacuumAgent()
    
    print("Initial Environment Status:")
    env.randomize_dirt()
    env.display_status()
    print("-" * 50)

    for step in range(1, steps + 1):
        print(f"\n--- Time Step {step} ---")
        
        # 1. Agent senses the environment
        percept = env.get_percept()
        print(f"Agent perceives: Location {percept[0]} is {percept[1]}")
        
        # 2. Agent decides on an action based on rules
        action = agent.act(percept)
        print(f"Agent Action Decision: {action}")
        
        # 3. Environment processes the action consequences
        if action == "Suck":
            env.locations[env.agent_location] = "Clean"
            env.performance_score += 10  # Reward points for cleaning
        elif action == "Right":
            env.agent_location = "B"
            env.performance_score -= 1   # Small penalty for energy consumption
        elif action == "Left":
            env.agent_location = "A"
            env.performance_score -= 1   # Small penalty for energy consumption

        # Show results after action
        env.display_status()
        
        # Randomly spawn new dirt for the next round simulation challenge
        env.randomize_dirt()
        time.sleep(1)

if __name__ == "__main__":
    run_simulation(5)
