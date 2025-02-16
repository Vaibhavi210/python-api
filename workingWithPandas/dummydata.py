from faker import Faker
import random
import pandas as pd


df=pd.read_csv("data.csv")
print(df)


fake = Faker()

# Generate random dummy data
def generate_fake_data(num_rows=10):
    data = []
    for _ in range(10):  # Change 100 to the desired number of rows
        fname = fake.first_name()
        lname = fake.last_name()
        email = fake.email()
        phone = fake.phone_number()
        
        data.append({
            "fname": fname,
            "lname": lname,
            "email": email,
           
            "segment_name": random.choice(["Sports", "christmas", "", None]),
            "segment_id": random.choice(["123", "456", "", None]),
            # "fname_hash": "",  # Empty for testing hash function
            # "lname_hash": "",
            # "email_hash": "",
            # "phone_hash": "",
             "phone": phone,

            
        })
    return pd.DataFrame(data)
if __name__ == "__main__":
    df = generate_fake_data(10)  # Generate 10 rows for testing
    print(df)  # Show first 5 rows
    #df.to_csv("data.csv",index=False)

# Create DataFrame


