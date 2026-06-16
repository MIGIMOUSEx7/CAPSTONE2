import os
import django

# Set up the Django environment so this script can interact with the database
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'agriresq_backend.settings')
django.setup()

from api.models import CropBatch, Listing, Transaction

def seed_data():
    print("🌱 Starting database seeding...")

    # 1. Clear out any existing data to avoid duplicates
    print("Clearing old records...")
    CropBatch.objects.all().delete()
    Listing.objects.all().delete()
    Transaction.objects.all().delete()

    # 2. Create Fake Crop Batches (For the Dashboard & Batches page)
    print("Injecting Crop Batches...")
    batches = [
        {
            "batch_id": "#001", "node": "Stall 1 • Node 01", "icon": "🍆", "crop": "Eggplant", 
            "scientific": "Solanum melongena", "qty": "85 kg", "price": "₱18/kg", 
            "arrival": "Apr 24, 6:00 AM", "days": 2, "daysColor": "text-amber-500", 
            "temp": "33.4°C", "rh": "82% RH", "status": "At-Risk", 
            "statusBg": "bg-amber-100 text-amber-700", "statusColor": "bg-rose-100 text-rose-700"
        },
        {
            "batch_id": "#002", "node": "Stall 1 • Node 02", "icon": "🥒", "crop": "Cucumber", 
            "scientific": "Cucumis sativus", "qty": "60 kg", "price": "₱22/kg", 
            "arrival": "Apr 24, 8:00 AM", "days": 4, "daysColor": "text-amber-500", 
            "temp": "29.8°C", "rh": "78% RH", "status": "Monitoring", 
            "statusBg": "bg-amber-100 text-amber-700", "statusColor": "bg-amber-100 text-amber-700"
        },
        {
            "batch_id": "#003", "node": "Stall 1 • Node 03", "icon": "🥕", "crop": "Carrots", 
            "scientific": "Daucus carota", "qty": "120 kg", "price": "₱15/kg", 
            "arrival": "Apr 24, 5:30 AM", "days": 8, "daysColor": "text-emerald-600", 
            "temp": "24.5°C", "rh": "91% RH", "status": "Fresh", 
            "statusBg": "bg-emerald-100 text-emerald-700", "statusColor": "bg-emerald-100 text-emerald-700"
        }
    ]
    for b in batches:
        CropBatch.objects.create(**b)

    # 3. Create Fake Marketplace Listings
    print("Injecting Marketplace Listings...")
    listings = [
        {
            "crop": "Eggplant", "icon": "🍆", "batch": "Batch #001", "vendor": "Stall 1 • Marhean B.", 
            "status": "At-Risk", "statusBg": "bg-amber-100 text-amber-700", "qty": "85 kg", 
            "days": "2 days", "temp": "33.4°C", "rh": "82%", "priceType": "Rescue Price", 
            "price": "₱18 / kg", "inquiries": "3 buyers interested", "isAtRisk": True
        },
        {
            "crop": "Eggplant", "icon": "🍆", "batch": "Batch #004", "vendor": "Stall 1 • Marhean B.", 
            "status": "At-Risk", "statusBg": "bg-amber-100 text-amber-700", "qty": "40 kg", 
            "days": "1.5 days", "temp": "34.1°C", "rh": "60%", "priceType": "Rescue Price", 
            "price": "₱16 / kg", "inquiries": "1 buyer interested", "isAtRisk": True
        },
        {
            "crop": "Cucumber", "icon": "🥒", "batch": "Batch #002", "vendor": "Stall 1 • Marhean B.", 
            "status": "Fresh", "statusBg": "bg-emerald-100 text-emerald-700", "qty": "60 kg", 
            "days": "4 days", "temp": "29.8°C", "rh": "78%", "priceType": "Standard Price", 
            "price": "₱22 / kg", "inquiries": "2 buyers interested", "isAtRisk": False
        },
        {
            "crop": "Carrots", "icon": "🥕", "batch": "Batch #003", "vendor": "Stall 1 • Marhean B.", 
            "status": "Fresh", "statusBg": "bg-emerald-100 text-emerald-700", "qty": "120 kg", 
            "days": "8 days", "temp": "24.5°C", "rh": "91%", "priceType": "Standard Price", 
            "price": "₱15 / kg", "inquiries": "5 buyers interested", "isAtRisk": False
        }
    ]
    for l in listings:
        Listing.objects.create(**l)

    # 4. Create Fake Transactions
    print("Injecting Transactions...")
    transactions = [
        {
            "txn_id": "#TXN-041", "buyerName": "Maria Buenaflor", "buyerRole": "Restaurant owner", 
            "crop": "🍆 Eggplant", "batch": "Batch #001", "qty": "20 kg", "total": "₱360", 
            "type": "Rescue", "typeBg": "bg-amber-100 text-amber-700", "typeDot": "text-amber-500", 
            "status": "Confirmed", "statusBg": "bg-blue-50 text-blue-700", "statusDot": "text-blue-500", "time": "9:43 AM"
        },
        {
            "txn_id": "#TXN-040", "buyerName": "Jose Reyes", "buyerRole": "Sari-sari store", 
            "crop": "🥕 Carrots", "batch": "Batch #003", "qty": "15 kg", "total": "₱225", 
            "type": "Standard", "typeBg": "bg-emerald-100 text-emerald-700", "typeDot": "text-emerald-500", 
            "status": "Confirmed", "statusBg": "bg-blue-50 text-blue-700", "statusDot": "text-blue-500", "time": "8:30 AM"
        },
        {
            "txn_id": "#TXN-039", "buyerName": "Ana Perez", "buyerRole": "Food processor", 
            "crop": "🥒 Cucumber", "batch": "Batch #002", "qty": "25 kg", "total": "₱475", 
            "type": "Standard", "typeBg": "bg-emerald-100 text-emerald-700", "typeDot": "text-emerald-500", 
            "status": "Pending pickup", "statusBg": "bg-slate-100 text-slate-700", "statusDot": "text-slate-400", "time": "7:15 AM"
        }
    ]
    for t in transactions:
        Transaction.objects.create(**t)

    print("✅ Database successfully seeded with fake data!")

if __name__ == "__main__":
    seed_data()