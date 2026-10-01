def simple_reflex_vacuum_agent(location, status_a, status_b):
    print("\n--- Simple Reflex Vacuum Agent ---")
    current_status = status_a if location == 'A' else status_b
   
    print(f"Percept: Location = {location}, Current Room Status = {'Dirty' if current_status == 1 else 'Clean'}")
   
    if current_status == 1:
        action = "Suck"
    elif location == 'A':
        action = "Move Right"
    elif location == 'B':
        action = "Move Left"
       
    print(f"Action Taken: {action}")
    return action


if __name__ == "__main__":
    loc = input("Enter Vacuum Location (A/B): ").strip().upper()
    st_a = int(input("Enter Room A status (1 for Dirty, 0 for Clean): "))
    st_b = int(input("Enter Room B status (1 for Dirty, 0 for Clean): "))
    
    simple_reflex_vacuum_agent(loc, st_a, st_b)