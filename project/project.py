from datetime import datetime, time
import sys

# Emoji constants for better readability
EMOJIS = {
    'welcome': '🎉',
    'groceries': '🛒',
    'food': '🍕',
    'money': '💰',
    'bill': '💳',
    'movies': '🎬',
    'songs': '🎵',
    'success': '✅',
    'error': '❌',
    'star': '⭐',
    'arrow': '➡️',
    'check': '✔️',
    'clock': '⏰',
    'phone': '📱',
    'pizza': '🍕',
    'burger': '🍔',
    'samosa': '🥟',
    'tea': '🍵',
    'icecream': '🍨',
    'dress': '👗',
    'saree': '🧣',
    'jewelry': '💍',
    'house': '🏠',
    'laptop': '💻',
    'headphones': '🎧'
}

def print_emoji(text, emoji='⭐'):
    """Print text with emoji"""
    print(f"{EMOJIS.get(emoji, '⭐')} {text}")

def groceries_billing():
    categories = {
        "Dresses": {
            "colors": ["Red", "Blue", "Green", "Yellow", "Black"],
            "types": ["Casual", "Formal", "Party Wear","Embroidery","Ghagra Choli"]
        },
        "Saree": {
            "colors": ["Pink", "Purple", "Orange", "White", "Black"],
            "types": ["Georgette","Cotton", "Silk", "Chiffon","Banarasi","Kanchipuram"]
        },
        "Jewellery": ["Necklace", "Earrings", "Bangles", "Jummka"],
        "House Products": ["Detergent", "Utensils", "Cleaners", "Mop", "Bucket"],
        "Electronic Gadgets": {
            "Phones": ["iPhone", "Samsung", "Vivo", "Oppo"],
            "Laptops": ["Lenovo", "Dell", "Apple", "Thinkpad", "HP"],
            "Accessories": ["Boat Bluetooth", "Sony Bluetooth"]
        }
    }
    items = []
    print_emoji("🛒 Groceries Shopping Started!", 'groceries')
    
    while True:
        print(f"\n{EMOJIS['arrow']} Categories:")
        for idx, cat in enumerate(categories, 1):
            print(f"{idx}. {EMOJIS['star']} {cat}")
        cat_choice = input(f"{EMOJIS['arrow']} Choose category number (or 'q' to quit): ")
        if cat_choice.lower() == 'q':
            break
        if not cat_choice.isdigit():
            print_emoji("Invalid category choice.", 'error')
            continue
        cat_choice_num = int(cat_choice)
        if cat_choice_num < 1 or cat_choice_num > len(categories):
            print_emoji("Invalid category choice.", 'error')
            continue
        category = list(categories.keys())[cat_choice_num - 1]

        color = None
        dress_type = None
        gadget_type = None
        gadget_model = None

        if category in ["Dresses", "Saree"]:
            print(f"👗 Available types for {category}: {', '.join(categories[category]['types'])}")
            dress_type = input("Choose type: ").strip()
            if dress_type not in categories[category]['types']:
                print_emoji("Invalid type choice.", 'error')
                continue
            print(f"🌈 Available colors for {category}: {', '.join(categories[category]['colors'])}")
            color = input("Choose color: ").strip()
            if color not in categories[category]['colors']:
                print_emoji("Invalid color choice.", 'error')
                continue
        elif category == "Electronic Gadgets":
            print("💻 Available Gadget Types:")
            gadget_types = list(categories[category].keys())
            for i, gt in enumerate(gadget_types, 1):
                print(f"{i}. {gt}")
            gt_choice = input("Choose gadget type number: ").strip()
            if not gt_choice.isdigit() or int(gt_choice) < 1 or int(gt_choice) > len(gadget_types):
                print_emoji("Invalid gadget type choice.", 'error')
                continue
            gadget_type = gadget_types[int(gt_choice) - 1]
            print(f"📱 Available models for {gadget_type}: {', '.join(categories[category][gadget_type])}")
            gadget_model = input("Choose model/accessory: ").strip()
            if gadget_model not in categories[category][gadget_type]:
                print_emoji("Invalid model/accessory choice.", 'error')
                continue
        else:
            print(f"🏠 Available items for {category}: {', '.join(categories[category])}")

        item_name = input("📝 Enter item name (choose from above or add new): ").strip()
        if item_name == "":
            print_emoji("Item name cannot be empty.", 'error')
            continue
        price_input = input("💰 Enter item price (Rs): ").strip()
        if not (price_input.replace('.', '', 1).isdigit() and price_input.count('.') <= 1):
            print_emoji("Invalid price entered.", 'error')
            continue
        price = float(price_input)
        if price < 0:
            print_emoji("Invalid price entered.", 'error')
            continue

        items.append({
            "category": category,
            "type": dress_type,
            "color": color,
            "gadget_type": gadget_type,
            "gadget_model": gadget_model,
            "item": item_name,
            "price": price
        })
        desc = f"{EMOJIS['success']} Added: {item_name} ({category}"
        if dress_type:
            desc += f", Type: {dress_type}"
        if color:
            desc += f", Color: {color}"
        if gadget_type:
            desc += f", Gadget Type: {gadget_type}"
        if gadget_model:
            desc += f", Model: {gadget_model}"
        desc += f") - Rs {price}"
        print_emoji(desc)
    return items

def food_ordering():
    menu = {
        'Pizza': 150,
        'Burger': 100,
        'Samosa': 30,
        'Tea': 10,
        'Ice-Cream': {
            'Vanilla': 60,
            'Chocolate': 70,
            'Strawberry': 65,
            'Mango': 65,
            'Butterscotch': 75
        },
        'Chocolate': {
            'Dairy Milk': 80,
            'Munch': 10,
            '5Star': 10,
            'Perk': 10
        }
    }
    orders = {}
    print_emoji("🍕 Food Ordering Started!", 'food')
    print("\n🍕 Menu:")
    idx = 1
    item_index_map = {}
    for item, price in menu.items():
        if isinstance(price, dict):
            continue
        print(f"{idx}. {EMOJIS['pizza' if 'Pizza' in item else 'burger' if 'Burger' in item else 'samosa' if 'Samosa' in item else 'tea']} {item} - Rs {price}")
        item_index_map[idx] = (item, None)
        idx += 1
    for item, flavors in menu.items():
        if isinstance(flavors, dict):
            for flavor, price in flavors.items():
                print(f"{idx}. {item} ({flavor}) - Rs {price}")
                item_index_map[idx] = (item, flavor)
                idx += 1
    while True:
        choice = input(f"{EMOJIS['arrow']} Enter item number to order (or 'q' to quit): ")
        if choice.lower() == 'q':
            break
        if not choice.isdigit():
            print_emoji("Invalid choice.", 'error')
            continue
        choice_num = int(choice)
        if choice_num not in item_index_map:
            print_emoji("Invalid choice.", 'error')
            continue
        selected_item, selected_flavor = item_index_map[choice_num]
        qty_input = input(f"📦 Enter quantity for {selected_item}" + (f" ({selected_flavor})" if selected_flavor else "") + ": ")
        if not (qty_input.isdigit() and int(qty_input) >= 0):
            print_emoji("Invalid quantity.", 'error')
            continue
        qty = int(qty_input)
        if qty > 0:
            order_key = f"{selected_item} ({selected_flavor})" if selected_flavor else selected_item
            if order_key in orders:
                orders[order_key] += qty
            else:
                orders[order_key] = qty
        print_emoji(f"Added {qty} x {selected_item}" + (f" ({selected_flavor})" if selected_flavor else ""))
    flat_menu = {}
    for item, price in menu.items():
        if isinstance(price, dict):
            for flavor, p in price.items():
                flat_menu[f"{item} ({flavor})"] = p
        else:
            flat_menu[item] = price
    return orders, flat_menu

def show_groceries_bill(items):
    if not items:
        print_emoji("No groceries items added.", 'error')
        return 0, 0
    print_emoji("🛒 Groceries Bill:", 'groceries')
    total = 0
    for idx, i in enumerate(items, 1):
        details = f"{i['item']} ({i['category']}"
        if i.get('type'):
            details += f", Type: {i['type']}"
        if i.get('color'):
            details += f", Color: {i['color']}"
        if i.get('gadget_type'):
            details += f", Gadget Type: {i['gadget_type']}"
        if i.get('gadget_model'):
            details += f", Model: {i['gadget_model']}"
        details += ")"
        print(f"{idx}. {details} - Rs {i['price']}")
        total += i['price']
    print(f"{EMOJIS['success']} Total for Groceries: Rs {total}")
    return len(items), total

def show_food_bill(orders, menu):
    if not orders:
        print_emoji("No food orders placed.", 'error')
        return 0, 0
    print_emoji("🍕 Food Order Bill:", 'food')
    total = 0
    total_items = 0
    for idx, (item, qty) in enumerate(orders.items(), 1):
        price = menu[item] * qty
        print(f"{idx}. {item} x {qty} @ Rs {menu[item]} = Rs {price}")
        total += price
        total_items += qty
    print(f"{EMOJIS['success']} Total for Food: Rs {total}")
    return total_items, total

def payment_transfer():
    user_pin = "9966"
    print_emoji("💰 Money Transfer", 'money')
    while True:
        amount_input = input("💵 Enter amount to transfer (Rs): ").strip()
        if not (amount_input.replace('.', '', 1).isdigit() and amount_input.count('.') <= 1):
            print_emoji("Invalid amount.", 'error')
            continue
        amount = float(amount_input)
        if amount <= 0:
            print_emoji("Amount must be positive.", 'error')
            continue
        recipient = input("👤 Enter recipient ID: ").strip()
        if recipient == "":
            print_emoji("Recipient ID cannot be empty.", 'error')
            continue
        sender_name = input("✍️ Enter sender's name: ").strip()
        if sender_name == "":
            print_emoji("Sender's name cannot be empty.", 'error')
            continue
        pin = input("🔐 Enter your 4-digit PIN to authorize transfer: ").strip()
        if pin == user_pin:
            now = datetime.now()
            dt_string = now.strftime("%Y-%m-%d %H:%M:%S")
            print_emoji(f"Rs {amount} transferred successfully from {sender_name} to {recipient}!", 'success')
            print(f"{EMOJIS['clock']} Transfer Date & Time: {dt_string}")
            break
        else:
            print_emoji("Incorrect PIN! Transfer cancelled.", 'error')
            retry = input("Try again? (y/n): ").strip().lower()
            if retry != 'y':
                break

def bill_payments():
    payment_apps = ["PhonePe", "Paytm", "Google Pay", "Amazon Pay"]
    print_emoji("💳 Bill Payments", 'bill')
    print("Bill Payment Options:")
    for i, app in enumerate(payment_apps, 1):
        print(f"{i}. 📱 {app}")
    user_pin = "9966"
    while True:
        choice = input("Choose payment platform number (or 'q' to quit): ").strip()
        if choice.lower() == 'q':
            break
        if not choice.isdigit() or int(choice) < 1 or int(choice) > len(payment_apps):
            print_emoji("Invalid choice. Please select a valid platform.", 'error')
            continue
        
        app_selected = payment_apps[int(choice) - 1]
        sender_name = input("✍️ Enter sender's name: ").strip()
        if sender_name == "":
            print_emoji("Sender name cannot be empty.", 'error')
            continue

        amount_input = input(f"💰 Enter amount to pay via {app_selected} (Rs): ").strip()
        if not (amount_input.replace('.', '', 1).isdigit() and amount_input.count('.') <= 1):
            print_emoji("Invalid amount entered.", 'error')
            continue
        amount = float(amount_input)
        if amount <= 0:
            print_emoji("Amount must be positive.", 'error')
            continue
        
        biller_id = input(f"📋 Enter biller ID for {app_selected}: ").strip()
        if biller_id == "":
            print_emoji("Biller ID cannot be empty.", 'error')
            continue
        
        pin = input(f"🔐 Enter your 4-digit PIN to authorize payment of Rs {amount} via {app_selected}: ").strip()
        if pin == user_pin:
            now = datetime.now()
            dt_string = now.strftime("%Y-%m-%d %H:%M:%S")
            print_emoji(f"Payment of Rs {amount} from {sender_name} to biller {biller_id} via {app_selected} successful!", 'success')
            print(f"{EMOJIS['clock']} Payment Date & Time: {dt_string}")
            break
        else:
            print_emoji("Incorrect PIN! Payment cancelled.", 'error')
            retry = input("Try again? (y/n): ").strip().lower()
            if retry != 'y':
                break

def show_movies():
    movies = [
        "1. 🎬 Mirai",
        "2. 🎬 Mahavatar Narsimha",
        "3. 🎬 Kalki 2898AD",
        "4. 🎬 Salaar Part-1",
        "5. 🎬 Mirchi",
        "6. 🎬 OG",
        "7. 🎬 Guntur Karam",
        "8. 🎬 Devara (Part-1)",
        "9. 🎬 Khaleja",
        "10. 🎬 SVSC"
    ]
    print_emoji("Latest Movies:", 'movies')
    for movie in movies:
        print(movie)

def show_songs():
    songs = [
        "1. 🎵 Peelings --> Pushpa 2",
        "2. 🎵 Ayudha pooja --> Devara(Part-1)",
        "3. 🎵 Neeve --> Draling",
        "4. 🎵 Pileche --> Khaleja",
        "5. 🎵 Galli lo Telinattu --> Jalsa",
        "6. 🎵 Pardesiya --> Param Sundari",
        "7. 🎵 Kollagottey --> Remo",
        "8. 🎵 Nenu Nuvvantu --> Orange",
        "9. 🎵 Halamaithi Habibo --> Beast",
        "10. 🎵 Sundari Nene Nuvvanta --> Dalapathi"
    ]
    print_emoji("Latest Songs:", 'songs')
    for song in songs:
        print(song)

def main():
    print(f"{EMOJIS['welcome']} Welcome to the Multi-feature Nandu App! {EMOJIS['welcome']}")
    groceries_items = []
    food_orders = {}
    food_menu = {}
    while True:
        print(f"\n{EMOJIS['star']} Menu:")
        print(f"1. 🛒 Groceries")
        print(f"2. 🍕 Food Ordering")
        print(f"3. 💰 View Groceries Bill and Total Price")
        print(f"4. 🍔 View Food Order Bill")
        print(f"5. 💸 Transfer Money (with Sender's Name and Timestamp)")
        print(f"6. 💳 Bill Payments (with Timestamp)")
        print(f"7. 🎬 Latest Movies")
        print(f"8. 🎵 Latest Songs")
        print(f"9. 🚪 Exit")
        choice = input("Select an option: ").strip()

        if choice == '1':
            groceries_items.extend(groceries_billing())
        elif choice == '2':
            orders, menu = food_ordering()
            food_orders.update(orders)
            food_menu = menu
        elif choice == '3':
            count, total = show_groceries_bill(groceries_items)
            if count > 0:
                print_emoji(f"Total price of groceries items: Rs {total}", 'success')
        elif choice == '4':
            show_food_bill(food_orders, food_menu)
        elif choice == '5':
            payment_transfer()
        elif choice == '6':
            bill_payments()
        elif choice == '7':
            show_movies()
        elif choice == '8':
            show_songs()
        elif choice == '9':
            groceries_count, groceries_total = show_groceries_bill(groceries_items)
            food_count, food_total = show_food_bill(food_orders, food_menu)
            total_items = groceries_count + food_count
            total_money = groceries_total + food_total

            print(f"{EMOJIS['success']} Grand Total: Rs {total_money}")
            print(f"{EMOJIS['welcome']} Thank you for using the app. Goodbye! {EMOJIS['welcome']}")
            break
        else:
            print_emoji("Invalid option. Please select again.", 'error')

if __name__ == "__main__":
    main()