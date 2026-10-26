
"""
Pesa Pulse - Customer API Data Analysis
Main application entry point
"""

from pathlib import Path

import pandas as pd

from analysis import (
    get_customers,
    explore,
    extract_attributes,
    unique_cities,
    city_counts,
    email_domain_counts,
    to_dataframe,
    plot_distribution,
)


def get_count(item):
    """Return the count from a dictionary item."""
    return item[1]


def main():

    # STEP 1: Retrieve customers
    customers = get_customers()

    if not customers:
        print("No customer data available. Analysis stopped.")
        return

    print(f"\nCustomers retrieved: {len(customers)}")

    # STEP 2: Explore nested data
    print("\nExploring the first customer:")
    explore(customers[0])

    # STEP 3: Extract customer attributes
    rows = extract_attributes(customers)

    print(f"\nCustomers extracted: {len(rows)}")

    # STEP 4: Find unique cities
    cities = unique_cities(customers)

    print(f"\nUnique cities: {len(cities)}")
    print(f"Total customers: {len(customers)}")

    # STEP 5: Count customers by city
    counts = city_counts(customers)

    sorted_cities = sorted(
        counts.items(),
        key=lambda item: (-item[1], item[0])  # Sort by count
    )

    print("\nCustomers by city:")

    for city, count in sorted_cities:
        print(f"{city}: {count}")

    # Count customers by email domain
    domain_counts = email_domain_counts(customers)

    sorted_domains = sorted(
        domain_counts.items(),
        key=lambda item: (-item[1], item[0])
    )

    print("\nCustomers by email domain:")

    for domain, count in sorted_domains:
        print(f"{domain}: {count}")

    # STEP 6: Convert records into pandas DataFrame
    df = to_dataframe(rows)

    print("\nDataFrame shape:")
    print(df.shape)

    print("\nDataFrame data types:")
    print(df.dtypes)

    # Validate Python counts against pandas counts
    pandas_counts = df["city"].value_counts().to_dict()

    print("\nDo pandas and Python counts agree?")
    print(pandas_counts == counts)

    # STEP 7: Export results to CSV
    output_dir = Path(__file__).resolve().parent / "output"
    output_dir.mkdir(exist_ok=True)

    customers_path = output_dir / "customers.csv"
    df.to_csv(customers_path, index=False)

    print(f"\nCustomers exported to: {customers_path}")

    city_df = pd.DataFrame(
        counts.items(),
        columns=["city", "customer_count"]
    )

    city_df = city_df.sort_values(
        by=["customer_count", "city"],
        ascending=[False, True]
    )

    city_counts_path = output_dir / "city_counts.csv"
    city_df.to_csv(city_counts_path, index=False)

    print(f"City counts exported to: {city_counts_path}")

    # STEP 8: Generate charts
    city_chart_path = output_dir / "customer_distribution.png"
    plot_distribution(
            counts,
            city_chart_path,
            title="Customers by City",
            xlabel="City"
    )

    email_chart_path = output_dir / "email_domain_distribution.png"

   
    plot_distribution(
        domain_counts,
        email_chart_path,
        title="Customers by Email Domain",
        xlabel="Email Top-Level Domain"
    )

    
    

    # Final summary
    print("\n========== PESA PULSE SUMMARY ==========")
    print(f"Customers retrieved : {len(customers)}")
    print(f"Unique cities       : {len(cities)}")

    highest_count = max(counts.values())

    top_cities = [
        city for city, count in counts.items()
        if count == highest_count
    ]
    if len(top_cities) == 1:
        print(f"Most common city    : {top_cities[0]} ({highest_count})")
    else:
        print(f"Most common city    : Tie between {len(top_cities)} cities ({highest_count} each)")
    
    print(f"Email domains       : {domain_counts}")
    print("Analysis completed successfully!")


if __name__ == "__main__":
    main()
