import random


car_models = {
    "Acura": ["RDX"],
    "Ford": ["Explorer", "Expedition"],
    "Chevrolet": ["Blazer", "Camaro",],
    "Lamborghini": ["Urus", "Aventador"],
    "Kia": ["Sorento", "Telluride"],
    "Honda": ["Passport", "Pilot"],
    "Toyota": ["RAV4", "4Runner", "Land Cruiser"],
    "Subaru": ["CrossTrek", "Solterra"],
    "Hyundai": ["Palisade"],
    "Land Rover": ["Range Rover", "Defender"],
    "Nissan": ["Pathfinder"],
    "Lexus": ["GX", "TX", "LX"], #Grand Crossover (GX), Touring Crossover (TX), Luxury Crossover (LX) 
}

def get_car():
    # Holds the names of makes
    car_makes = list(car_models.keys())
    
    # User message
    message = "I want to buy a"
    
    # Generates a make
    car_to_buy = random.choice(car_makes)
    
    # Generates and holds the model of a car make
    car_model = random.choice(car_models[car_to_buy])
    
    return(f"{message} {car_to_buy}, the {car_model} model.")

