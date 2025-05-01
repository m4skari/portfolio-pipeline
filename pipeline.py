import subprocess

print("📥 Loading data into database...")
subprocess.run(["python", "scripts/load_data.py"])

print("\n🧼 Preprocessing data...")
subprocess.run(["python", "scripts/preprocess.py"])

print("\n🧠 Performing feature engineering...")
subprocess.run(["python", "scripts/feature_engineering.py"])

print("\n✅ Pipeline execution complete.")
