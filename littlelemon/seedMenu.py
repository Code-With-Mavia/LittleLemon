import os
import django

# Set up Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "littlelemon.settings")
django.setup()

from restaurant.models import Menu

# Optional: clear all existing data first
Menu.objects.all().delete()
print("🧹 Cleared existing menu items")

# Menu seed data
menu_items = [
    {
        "name": "Bruschetta",
        "price": 6.50,
        "menu_item_description": "Grilled bread topped with diced tomatoes, garlic, olive oil, and basil."
    },
    {
        "name": "Greek Salad",
        "price": 9.99,
        "menu_item_description": "Crisp lettuce, cucumbers, olives, and feta with lemon dressing."
    },
    {
        "name": "Grilled Fish",
        "price": 15.99,
        "menu_item_description": "Fresh fish fillet grilled and served with lemon butter sauce."
    },
    {
        "name": "Lava Cake",
        "price": 7.99,
        "menu_item_description": "Warm chocolate cake with molten chocolate center."
    },
    {
        "name": "Lemon Dessert",
        "price": 6.25,
        "menu_item_description": "Light lemon-flavored dessert topped with whipped cream."
    },
    {
        "name": "Wood-Fired Pepperoni Pizza",
        "price": 13.75,
        "menu_item_description": "Classic pepperoni pizza baked in a wood-fired oven."
    },
    {
        "name": "Wild Mushroom Risotto",
        "price": 12.75,
        "menu_item_description": "Creamy risotto with wild mushrooms and parmesan."
    },
    {
        "name": "Truffle Parmesan Fries",
        "price": 5.99,
        "menu_item_description": "Crispy fries tossed with truffle oil and parmesan cheese."
    },
    {
        "name": "Cheesecake with Berry Compote",
        "price": 8.50,
        "menu_item_description": "Creamy cheesecake with mixed berry topping."
    }
]

# Insert all menu items
for item in menu_items:
    Menu.objects.create(**item)
    print(f"✅ Added: {item['name']}")

print("🍋 Done seeding menu!")
