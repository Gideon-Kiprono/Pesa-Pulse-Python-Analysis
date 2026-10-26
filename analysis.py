"""
Day 1 - API Data Analysis Using Python Structures
Squad Python Specialization - Data Science, AI & Analytics
"""

import matplotlib.pyplot as plt
import pandas as pd
import requests

API_URL = "https://jsonplaceholder.typicode.com/users"


def get_customers(url= API_URL):
    """Fetch the customer list. Report failures clearly instead of crashing."""
    try:
        response = requests.get(url, timeout = 10)

        response.raise_for_status()

        customers = response.json()

        if not isinstance(customers, list):
            print("Error: API did not return a customer list.")
            return []

        return customers


    except(requests.exceptions.RequestException) as error:
        print(f"Failed to retrieve customers: {error}")
        return []



def explore(record, indent = 0):
    """Print every key in a (possibly nested) record with its type, indented by depth."""
    for key, value in record.items():
        print(" " * indent + f"{key}: {type(value).__name__}")

        if isinstance(value, dict):
            explore(value, indent + 4)

        elif isinstance(value, list):
            for item in value:
                if isinstance(item, dict):
                    explore(item, indent + 4)
                
    


def extract_attributes(customers):
    """Return one flat dict per customer with the attributes listed in the task."""

    extracted_customers = []
    for customer in customers:

        customer_data = {
            "customer_id": customer["id"],
            "name": customer["name"],
            "username": customer["username"],
            "email": customer["email"],
            "email_domain": customer["email"].split(".")[-1].lower(),
            "phone": customer["phone"],
            "city": customer["address"]["city"],
            "zipcode": customer["address"]["zipcode"],
            "latitude": float(customer["address"]["geo"]["lat"]),
            "longitude": float(customer["address"]["geo"]["lng"]),
            "company": customer["company"]["name"],
            "website": customer["website"],
        }

        extracted_customers.append(customer_data)

    return extracted_customers


def unique_cities(customers):
    """Return the set of distinct cities."""
    cities = set()

    for customer in customers:
        city = customer["address"]["city"]
        cities.add(city)

    return cities


def city_counts(customers):
    """Count customers per city using a loop and/or a dict comprehension (no Counter, no pandas)."""

    counts = {}

    for customer in customers:

        city = customer["address"]["city"]

        if city in counts:
            counts[city] += 1
        else:
            counts[city] = 1

    return counts


def email_domain_counts(customers):
    """Count customers per email top-level domain (e.g. 'biz', 'tv')."""
    domains = [
        customer["email"].split(".")[-1].lower() for customer in customers
    ]

    unique_domains = set(domains)

    counts = {domain: domains.count(domain) for domain in unique_domains
    }

    return counts



def to_dataframe(rows):

    """Convert a list of dicts to a pandas DataFrame."""
    df = pd.DataFrame(rows)
    return df


def plot_distribution(counts, path, title = "Customer Distribution", xlabel = "Category") :
    """Save a labelled chart of the distribution to path."""

    categories = list(counts.keys())
    values = list(counts.values())

    plt.figure(figsize=(12, 6))

    plt.bar(categories, values, color='steelblue')

    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel("Number of Customers")

    plt.xticks(rotation=45, ha='right')

    plt.tight_layout()

    plt.savefig(path, dpi=300)

    plt.close()

    print(f"Chart saved to: {path}")



