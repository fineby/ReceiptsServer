import datetime
import math

def calculate_points(receipt):
    points = 0
    breakdown = []
    breakdown.append(f"Total Points: {points}")
    breakdown.append("Breakdown: ")

    # Rule 1: One point for every alphanumeric character in the retailer name.
    points += sum(c.isalnum() for c in receipt["retailer"])
    if points > 0:
        breakdown.append(f"    {points} points - retailer name has {points} characters")

    # Rule 2: 50 points if the total is a round dollar amount with no cents.
    if receipt["total"].endswith(".00"):
        points += 50
        breakdown.append("    50 points - total is a round dollar amount")

    # Rule 3: 25 points if the total is a multiple of 0.25.
    total_float = float(receipt["total"])
    if total_float % 0.25 == 0:
        points += 25
        breakdown.append("    25 points - total is a multiple of 0.25")

    # Rule 4: 5 points for every two items on the receipt.
    num_items = len(receipt["items"])
    item_points = (num_items // 2) * 5
    points += item_points 
    if item_points > 0:
        breakdown.append(f"    {item_points} points - {num_items} items ({num_items // 2} pairs @ 5 points each)")

    # Rule 5: If the trimmed length of the item description is a multiple of 3,
    # multiply the price by 0.2 and round up to the nearest integer.
    # The result is the number of points earned.
    for item in receipt["items"]:
        description = item["shortDescription"].strip()
        description_len = len(description)
        if description_len % 3 == 0:
            price = float(item["price"])
            item_points = int(math.ceil(price * 0.2))
            points += item_points
            breakdown.append(f"    {item_points} Points - \"{description}\" is {description_len} characters (a multiple of 3)")
          
    # Rule 6: 6 points if the day in the purchase date is odd.
    purchase_date = datetime.datetime.strptime(receipt["purchaseDate"], "%Y-%m-%d")
    if purchase_date.day % 2 != 0:
        points += 6
        breakdown.append("    6 points - purchase day is odd")

    # Rule 7: 10 points if the time of purchase is after 2:00pm and before 4:00pm.
    purchase_time = datetime.datetime.strptime(receipt["purchaseTime"], "%H:%M")
    if purchase_time >= datetime.datetime.strptime("14:00", "%H:%M") and \
       purchase_time < datetime.datetime.strptime("16:00", "%H:%M"):
        points += 10
        breakdown.append("    10 points - purchase time is between 2:00pm and 4:00pm")

    breakdown.append("  + ---------")
    breakdown.append(f"= {points} points")

    return [points, "\n".join(breakdown)]