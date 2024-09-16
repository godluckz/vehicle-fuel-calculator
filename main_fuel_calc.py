#!/usr/bin/python 

def format_currency(p_amount):
    return 'R{:,.2f}'.format(p_amount)

def calculate_trip_cost(p_distance: int, 
                        p_litters_per_100km: int, 
                        w_fuel_price_per_litter: int) -> tuple[int,int]:
    w_100s       = p_distance/100
    w_litters    = w_100s * p_litters_per_100km
    w_total_cost = w_litters * w_fuel_price_per_litter

    return w_litters, w_total_cost


def main():
    w_distance          = int(input(f"What is the total trip distance (Km): "))
    w_litters_per_100km = int(input(f"What is vehicle's fuel consumption (L/100Km): "))
    w_fuel_price        = int(input(f"What is the current fuel price (per litter): "))
    

    w_total_litters, w_total_cost = calculate_trip_cost(p_distance = w_distance,
                                                        p_litters_per_100km = w_litters_per_100km,
                                                        w_fuel_price_per_litter = w_fuel_price)
    
    print(f"\n\nFor the given vehicle with a consumption of {w_litters_per_100km} Litters/100Km, Trip of {w_distance}Km will require at least:\nFuel: {w_total_litters} Litters\nCost: {format_currency(w_total_cost)} (in Fuel currency, e.g Rands).\n")



if __name__ == "__main__":
    print("****************************************")
    print("!!Welcome to Trip-Fuel-Cost calculator!!")
    print("****************************************")    
    print("\n")
    
    main()
    
    print("-----------------------------------------")
    print("-----------------------------------------")    
    print("Have a safe Trip 🛣️🛻💃📷\n\n")
    input('Press RETURN to finish')