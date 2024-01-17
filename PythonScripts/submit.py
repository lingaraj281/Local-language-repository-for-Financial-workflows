# submit.py
from neo4j import GraphDatabase
import os

NEO4J_URI = os.getenv("NEO4J_URI", "neo4j+s://<YOUR-NEO4J-AURA-INSTANCE>.databases.neo4j.io")
NEO4J_USER = os.getenv("NEO4J_USER", "<YOUR-NEO4J-AURA-USERNAME>")
NEO4J_PASSWORD = os.getenv("NEO4J_PASSWORD", "<YOUR-NEO4J-AURA-PASSWORD>")

def submit_to_neo4j(data):
    try:
        driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASSWORD))
        with driver.session() as session:
            # Customize this part to create Neo4j nodes with the survey data
            query = (
                "CREATE (survey:Survey {name: $name, date_time: $date_time, location: $location, time: $time, "
                "session_count: $session_count, name1: $name1, age: $age, gender: $gender, mobile_num: $mobile_num, "
                "languages: $languages, mobile: $mobile, family: $family, mobile1: $mobile1, address: $address, "
                "family_size: $family_size, education: $education, literacy: $literacy, prompt1: $prompt1, prompt2: $prompt2, "
                "Bank: $Bank, Post: $Post, Bank_detail: $Bank_detail, Banking_product: $Banking_product, "
                "gov_scheme: $gov_scheme, Internet_Banking: $Internet_Banking, Others: $Others, remote_family: $remote_family, "
                "Remote_family_money: $Remote_family_money, financial_notes: $financial_notes, prompt5a: $prompt5a, "
                "prompt5b: $prompt5b, prompt5c: $prompt5c, prompt5d: $prompt5d, prompt6a: $prompt6a, prompt6b: $prompt6b, "
                "prompt6c: $prompt6c, prompt6d: $prompt6d, prompt6e: $prompt6e, prompt6f: $prompt6f, upi: $upi, "
                "upi_apps: $upi_apps, upi_app_detail: $upi_app_detail, other_upi: $other_upi, wallets: $wallets, "
                "wallet_weekly: $wallet_weekly, counts: $counts, local_payment: $local_payment, QR: $QR, qr_counts: $qr_counts, "
                "Transport: $Transport, local_payment_transport: $local_payment_transport, BBPS: $BBPS, remote: $remote, "
                "common: $common, first_work: $first_work, first_workflow: $first_workflow, first_step: $first_step, "
                "second_step: $second_step, third_step: $third_step, fourth_step: $fourth_step})"
            )
            session.run(query, data)
        return True
    except Exception as e:
        print(f"Error submitting to Neo4j: {e}")
        return False
    finally:
        driver.close()

def main():
    # Example: Get form data from environment variables or another source
    form_data = {
        "name": os.getenv("INPUT_NAME"),
        "date_time": os.getenv("INPUT_DATE_TIME"),
        "location": os.getenv("INPUT_LOCATION"),
        "time": os.getenv("INPUT_TIME"),
        "session_count": os.getenv("INPUT_SESSION_COUNT"),
        # Add other form fields
    }

    if submit_to_neo4j(form_data):
        print("Data submitted successfully to Neo4j")
    else:
        print("Failed to submit data to Neo4j")

if __name__ == "__main__":
    main()
